from __future__ import annotations

import datetime as dt

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_date(date_str: str) -> dt.date | None:
    datetime = parse_datetime(date_str, DATE_FORMAT)
    return datetime.date() if datetime else None


def parse_datetime(
    datetime_str: str,
    date_format: str = DATETIME_FORMAT,
) -> dt.datetime | None:
    if not datetime_str or datetime_str.startswith("0000-00-00"):
        return None
    return dt.datetime.strptime(datetime_str, date_format)
