class CustomError(Exception):
    """Exception raised for application-specific error conditions."""
    def __init__(self, msg: str) -> None:
        """Initialize the exception with a descriptive message."""
        super().__init__(msg)


class C:
    """ANSI escape code constants for colored terminal output."""
    H = "\033[95m"  # Header
    B = "\033[94m"  # Blue
    C = "\033[96m"  # Cyan
    G = "\033[92m"  # Green
    W = "\033[93m"  # Warning
    F = "\033[91m"  # Fail
    E = "\033[0m"  # End
    Bo = "\033[1m"  # Bold
    U = "\033[4m"

    def msg(self, color: str, msg: str) -> None:
        """Print a message wrapped in the given ANSI color code."""
        print(getattr(self, color) + msg + C.E)
