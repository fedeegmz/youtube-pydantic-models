class QuotaException(Exception):
    def __init__(self) -> None:
        super("unavailable quota")


class InvalidArgException(Exception):
    def __init__(self) -> None:
        super("invalid arg")


class RequiredArgException(Exception):
    def __init__(self, name: str) -> None:
        super(f"{name} arg is required")
