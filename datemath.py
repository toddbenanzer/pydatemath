from datetime import datetime, timedelta, timezone


# constants
START_OF_WEEK = 'Saturday'


# conversion functions
def today():
    """Returns a date string for today."""
    utc_time = datetime.now(timezone.utc)
    nyc_timezone = timezone(timedelta(hours=-5), name="EST")
    return datetime_to_datestr(utc_time.astimezone(nyc_timezone).date())


def datestr_to_datetime(datestr):
    """Converts a date string in yyyy-mm-dd format to a datetime object."""
    return datetime.strptime(datestr, '%Y-%m-%d')


def datetime_to_datestr(date):
    """Converts a datetime object to a date string in yyyy-mm-dd format."""
    return date.strftime('%Y-%m-%d')


def datetime_to_monthstr(date):
    """Converts a datetime object to a date string in yyyymm format."""
    return date.strftime('%Y%m')


def monthstr_to_datetime(monthstr):
    """Converts a month string in yyyymm format to a datetime object."""
    year = int(monthstr[:4])
    month = int(monthstr[4:])
    day = 1
    date = datetime(year, month, day)
    return end_of_month(datetime_to_datestr(date))


# month transformations
def start_of_month(datestr):
    """Returns a date string for the beginning of the month."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(day=1))


def start_of_prev_month(datestr):
    """Returns a date string for the beginning of the previous month."""
    date = datestr_to_datetime(datestr)
    date = (date.replace(day=1) - timedelta(days=1)).replace(day=1)
    return datetime_to_datestr(date)


def start_of_next_month(datestr):
    """Returns a date string for the beginning of the next month."""
    date = datestr_to_datetime(datestr)
    date = (date.replace(day=1) + timedelta(days=32)).replace(day=1)
    return datetime_to_datestr(date)


def end_of_month(datestr):
    """Returns a date string for the end of the month."""
    date = datestr_to_datetime(start_of_next_month(datestr))
    return datetime_to_datestr(date - timedelta(days=1))


def end_of_prev_month(datestr):
    """Returns a date string for the end of the previous month."""
    return end_of_month(start_of_prev_month(datestr))


def end_of_next_month(datestr):
    """Returns a date string for the end of the next month."""
    return end_of_month(start_of_next_month(datestr))


def add_months(datestr, months):
    """Returns a date string for the beginning of the next month."""
    if months == 0:
        return end_of_month(datestr)
    elif months < 0:
        for i in range(abs(months)):
            datestr = end_of_prev_month(datestr)
    else:
        for i in range(months):
            datestr = end_of_next_month(datestr)
    return datestr


# week transformations
def get_previous_xday(datestr, dow='Sunday'):
    """Returns a date string for the previous Sunday."""
    dow_num = {
        'Sunday': 6, 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5
    }[dow]
    date = datestr_to_datetime(datestr)
    if date.weekday() == dow_num:
        return datetime_to_datestr(date)
    while date.weekday() != dow_num:
        date -= timedelta(days=1)
    return datetime_to_datestr(date)


def start_of_week(datestr):
    """Returns a date string for the beginning of the week."""
    return get_previous_xday(datestr, dow=START_OF_WEEK)


def end_of_week(datestr):
    """Returns a date string for the end of the week."""
    date = datestr_to_datetime(start_of_week(datestr))
    return datetime_to_datestr(date + timedelta(days=6))


def end_of_prev_week(datestr):
    """Returns a date string for the end of the previous week."""
    date = datestr_to_datetime(start_of_week(datestr))
    return datetime_to_datestr(date - timedelta(days=1))


def start_of_prev_week(datestr):
    """Returns a date string for the beginning of the previous week."""
    return start_of_week(end_of_prev_week(datestr))


def end_of_next_week(datestr):
    """Returns a date string for the end of the next week."""
    date = datestr_to_datetime(end_of_week(datestr))
    return datetime_to_datestr(date + timedelta(days=7))


def start_of_next_week(datestr):
    """Returns a date string for the beginning of the next week."""
    date = datestr_to_datetime(end_of_week(datestr))
    return datetime_to_datestr(date + timedelta(days=1))


def add_weeks(datestr, weeks):
    """Returns a date string for the beginning of the next week."""
    if weeks == 0:
        return end_of_week(datestr)
    elif weeks < 0:
        for i in range(abs(weeks)):
            datestr = end_of_prev_week(datestr)
    else:
        for i in range(weeks):
            datestr = end_of_next_week(datestr)
    return datestr


# year transformations
def start_of_year(datestr):
    """Returns a date string for the beginning of the year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(month=1, day=1))


def end_of_year(datestr):
    """Returns a date string for the end of the year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(month=12, day=31))


def start_of_prev_year(datestr):
    """Returns a date string for the beginning of the previous year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(year=date.year - 1, month=1, day=1))


def end_of_prev_year(datestr):
    """Returns a date string for the end of the previous year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(year=date.year - 1, month=12, day=31))


def start_of_next_year(datestr):
    """Returns a date string for the beginning of the next year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(year=date.year + 1, month=1, day=1))


def end_of_next_year(datestr):
    """Returns a date string for the end of the next year."""
    date = datestr_to_datetime(datestr)
    return datetime_to_datestr(date.replace(year=date.year + 1, month=12, day=31))


def add_years(datestr, years):
    """Returns a date string for the beginning of the next year."""
    if years == 0:
        return end_of_year(datestr)
    elif years < 0:
        for i in range(abs(years)):
            datestr = end_of_prev_year(datestr)
    else:
        for i in range(years):
            datestr = end_of_next_year(datestr)
    return datestr


# common transformations
def get_mob1(datestr):
    """Returns a date string for the end of the month in which the date occurs"""
    return end_of_month(datestr)


def get_mob3(datestr):
    """Returns a date string for the end of the month, two months after the date occurs"""
    return add_months(datestr, 2)


def get_mob6(datestr):
    """Returns a date string for the end of the month, five months after the date occurs"""
    return add_months(datestr, 5)


def get_mob12(datestr):
    """Returns a date string for the end of the month, eleven months after the date occurs"""
    return add_months(datestr, 11)


def get_mobn1(datestr):
    """Returns a date string for the end of the month prior to the date provided"""
    return add_months(datestr, -1)


def get_wob1(datestr):
    """Returns a date string for the end of the week in which the date occurs"""
    return end_of_week(datestr)


def get_wobn1(datestr):
    """Returns a date string for the end of the week prior to the date provided"""
    return add_weeks(datestr, -1)