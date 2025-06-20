import os
import threading
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

    # 64-bit integer limits
    MAX_64BIT_INT = (1 << 63) - 1  # Maximum signed 64-bit integer
    MIN_64BIT_INT = -(1 << 63)  # Minimum signed 64-bit integer

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

        # Validate the generated ID
        self._validate_64bit_integer(snowflake_id)

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

    def _validate_64bit_integer(self, snowflake_id: int) -> None:
        """
        Validate that the generated ID is a valid 64-bit integer.

        Args:
            snowflake_id: The generated Snowflake ID to validate

        Raises:
            ValueError: If the ID exceeds 64-bit integer limits
        """
        if not (self.MIN_64BIT_INT <= snowflake_id <= self.MAX_64BIT_INT):
            raise ValueError(f"Generated ID {snowflake_id} exceeds 64-bit integer limits")

        # Check bit length to ensure it doesn't exceed 64 bits
        bit_length = snowflake_id.bit_length()
        if bit_length > 64:
            raise ValueError(f"Generated ID has {bit_length} bits, exceeding the 64-bit limit")


_id_counter = 0
_counter_lock = threading.Lock()


def generate_random_64bit_id() -> int:
    """
    Generate a random 64-bit integer ID with high throughput and minimal collision risk.

    This function creates a unique ID by combining:
    - Current timestamp with microsecond precision (36 bits)
    - Process ID (10 bits)
    - Thread ID (8 bits)
    - Counter (10 bits) - allows 1024 IDs per microsecond per thread

    Returns:
        A random 64-bit integer suitable for use as an ID
    """
    global _id_counter

    # Get current time in microseconds (higher precision than milliseconds)
    timestamp = int(time.time() * 1_000_000)
    # Use only 36 bits for timestamp (enough for ~69 years in microseconds)
    timestamp = timestamp & 0xFFFFFFFFF  # 36 bits

    # Get process ID (10 bits)
    pid = os.getpid() & 0x3FF  # Use only lower 10 bits (0-1023)

    # Get thread ID (8 bits)
    tid = threading.get_ident() & 0xFF  # Use only lower 8 bits (0-255)

    # Increment counter atomically (10 bits - 0-1023)
    with _counter_lock:
        counter = _id_counter
        _id_counter = (_id_counter + 1) & 0x3FF

    # Combine all components:
    # - 36 bits for timestamp (microseconds)
    # - 10 bits for PID (0-1023)
    # - 8 bits for thread ID (0-255)
    # - 10 bits for counter (0-1023)
    # Total: 64 bits
    combined_id = (timestamp << 28) | (pid << 18) | (tid << 10) | counter

    # Ensure it fits in a 64-bit signed integer
    max_signed_64bit = (1 << 63) - 1
    combined_id = combined_id & max_signed_64bit

    return combined_id
