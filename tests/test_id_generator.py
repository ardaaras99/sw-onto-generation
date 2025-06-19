import unittest

from sw_onto_generation.base.id_generator import SnowflakeGenerator


class TestSnowflakeGenerator(unittest.TestCase):
    """Test suite for the SnowflakeGenerator class."""

    def test_generate_64bit_ids(self) -> None:
        """Test that generated IDs are valid 64-bit integers."""
        # Initialize generator with different machine IDs
        generators = [
            SnowflakeGenerator(machine_id=0),
            SnowflakeGenerator(machine_id=512),
            SnowflakeGenerator(machine_id=1023),  # Max machine ID
        ]

        # Generate 100 IDs from each generator
        for generator in generators:
            for _ in range(100):
                snowflake_id = generator.generate_id()

                # Test that ID is an integer
                self.assertIsInstance(snowflake_id, int)

                # Test that ID is within 64-bit signed integer range
                self.assertLessEqual(snowflake_id, (1 << 63) - 1)  # Max signed 64-bit
                self.assertGreaterEqual(snowflake_id, 0)  # Our IDs should be positive

                # Test that ID bit length doesn't exceed 64 bits
                self.assertLessEqual(snowflake_id.bit_length(), 64)

                # Additional check: ID should be positive since our timestamp is after epoch
                self.assertGreater(snowflake_id, 0)

    def test_id_uniqueness(self) -> None:
        """Test that generated IDs are unique."""
        generator = SnowflakeGenerator(machine_id=1)

        # Generate 100 IDs and check uniqueness
        ids = set()
        for _ in range(100):
            new_id = generator.generate_id()
            self.assertNotIn(new_id, ids, "Generated ID is not unique")
            ids.add(new_id)

    def test_id_components(self) -> None:
        """Test that ID components (timestamp, machine ID, sequence) are correctly encoded."""
        # Use specific machine ID for testing
        machine_id = 42
        generator = SnowflakeGenerator(machine_id=machine_id)

        # Generate an ID
        snowflake_id = generator.generate_id()

        # Extract components
        sequence = snowflake_id & ((1 << generator.SEQUENCE_BITS) - 1)
        extracted_machine_id = (snowflake_id >> generator.MACHINE_ID_SHIFT) & ((1 << generator.MACHINE_ID_BITS) - 1)
        timestamp = (snowflake_id >> generator.TIMESTAMP_SHIFT) + generator.EPOCH

        # Verify machine ID is correctly encoded
        self.assertEqual(extracted_machine_id, machine_id)

        # Verify sequence is within valid range
        self.assertGreaterEqual(sequence, 0)
        self.assertLessEqual(sequence, generator.MAX_SEQUENCE)

        # Verify timestamp is reasonable (after epoch, before "now" + 1 second)
        current_time = generator._current_timestamp()
        self.assertGreaterEqual(timestamp, generator.EPOCH)
        self.assertLessEqual(timestamp, current_time + 1000)


if __name__ == "__main__":
    unittest.main()
