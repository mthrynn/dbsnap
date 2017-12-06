import time

import datetime

from dateutil.tz import tzutc

def datetime_to_timestamp(dt):
    return time.mktime(dt.timetuple())

def timestamp_to_datetime(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=tzutc())

def now_timestamp():
    return time.time()

def now_datetime():
    return timestamp_to_datetime(now_timestamp())

def today_datetime():
    now_dt = now_datetime()
    return datetime.datetime(now_dt.year, now_dt.month, now_dt.day, tzinfo=tzutc())

def today_timestamp():
    return datetime_to_timestamp(today_datetime())

def add_days_to_datetime(dt, amount_of_days):
    return (dt + datetime.timedelta(days=amount_of_days))

def subtract_days_from_datetime(dt, amount_of_days):
    return (dt - datetime.timedelta(days=amount_of_days))

def datetime_to_date_str(dt):
    return dt.strftime("%Y-%m-%d")
