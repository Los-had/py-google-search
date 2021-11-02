from typing import Optional

def http_error(error: str) -> dict:
    return {
        "Message": f"A http_error(error: {error}) ocurred, try again."
    }

def connection_error(error: Optional[str] = None) -> dict:
    return {
        "Message": f"A connection_error(error: {error}) ocurred, try again."
    }

def default_error() -> dict:
    return {
        "Message": "An error ocurred, try again."
    }

def dynamic_error(error: str) -> dict:
    return {
        "Message": "An error ocurred, try again.",
        "Error": error
    }