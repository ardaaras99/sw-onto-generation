import time


class SnowflakeGenerator:
    """
    Generates Snowflake IDs in 64-bit integer format.

    Structure:
    - 41 bits for timestamp (milliseconds since epoch)
    - 10 bits for machine ID
    - 12 bits for sequence number

    This gives us:
    - Uniqueness across distributed systems
    - Time-sortable IDs
    - ~70 years of timestamps from epoch
    - 1024 different machine IDs
    - 4096 IDs per millisecond per machine
    """

    # Epoch time (2023-01-01 00:00:00 UTC)
    EPOCH = 1672531200000

    # Bit lengths
    TIMESTAMP_BITS = 41
    MACHINE_ID_BITS = 10
    SEQUENCE_BITS = 12

    # Maximum values
    MAX_MACHINE_ID = (1 << MACHINE_ID_BITS) - 1
    MAX_SEQUENCE = (1 << SEQUENCE_BITS) - 1

    # Shift amounts
    MACHINE_ID_SHIFT = SEQUENCE_BITS
    TIMESTAMP_SHIFT = SEQUENCE_BITS + MACHINE_ID_BITS

    def __init__(self, machine_id: int = 1):
        """
        Initialize the Snowflake ID generator.

        Args:
            machine_id: An ID representing this machine/process (0-1023)
        """
        if machine_id < 0 or machine_id > self.MAX_MACHINE_ID:
            raise ValueError(f"Machine ID must be between 0 and {self.MAX_MACHINE_ID}")

        self.machine_id = machine_id
        self.last_timestamp = -1
        self.sequence = 0

    def generate_id(self) -> int:
        """
        Generate a new Snowflake ID.

        Returns:
            A 64-bit integer Snowflake ID
        """
        timestamp = self._current_timestamp()

        # Handle clock moving backwards
        if timestamp < self.last_timestamp:
            raise RuntimeError(f"Clock moved backwards. Refusing to generate ID for {self.last_timestamp - timestamp} milliseconds")

        # If same millisecond as last time, increment sequence
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.MAX_SEQUENCE
            # If sequence exhausted in this millisecond, wait for next millisecond
            if self.sequence == 0:
                timestamp = self._wait_next_millisecond()
        else:
            # Reset sequence for new millisecond
            self.sequence = 0

        self.last_timestamp = timestamp

        # Compose the ID from its components
        snowflake_id = ((timestamp - self.EPOCH) << self.TIMESTAMP_SHIFT) | (self.machine_id << self.MACHINE_ID_SHIFT) | self.sequence

        return snowflake_id

    def _current_timestamp(self) -> int:
        """Get current timestamp in milliseconds."""
        return int(time.time() * 1000)

    def _wait_next_millisecond(self) -> int:
        """Wait until next millisecond and return its timestamp."""
        timestamp = self._current_timestamp()
        while timestamp <= self.last_timestamp:
            timestamp = self._current_timestamp()
        return timestamp
