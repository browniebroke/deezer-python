import datetime as dt
from typing import Optional

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_date(date_str: str) -> Optional[dt.date]:
    datetime = parse_datetime(date_str, DATE_FORMAT)
    return datetime.date() if datetime else None


def parse_datetime(
    datetime_str: str,
    date_format: str = DATETIME_FORMAT,
) -> Optional[dt.datetime]:
    if not datetime_str or datetime_str.startswith("0000-00-00"):
        return None
    return dt.datetime.strptime(datetime_str, date_format)
