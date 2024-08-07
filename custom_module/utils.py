from datetime import datetime
from .exceptions import PackageBuildingException


def get_date_format() -> str:
    return "%Y-%m-%d %H:%M:%S"


def get_current_datetime(date_format=None) -> str:
    try:
        current_datetime = datetime.now()
        return current_datetime.strftime("%Y %m %d %H:%M:%S" if date_format is None else date_format)
    except Exception as e:
        print("Exception at: get_current_datetime function")
        raise PackageBuildingException(f"Could not get current datetime due to exception occurred, Exception: {e}")
