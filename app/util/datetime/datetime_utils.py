import datetime

def current_datetime() -> datetime.datetime :
    return datetime.datetime.utcnow()

def datetime_to_iso(dt):
    return dt.isoformat()

def iso_to_datetime(iso_str):
    return datetime.datetime.fromisoformat(iso_str)

def compare_datetime(dt1, dt2):
    if dt1 < dt2:
        return -1
    elif dt1 == dt2:
        return 0
    else:
        return 1


