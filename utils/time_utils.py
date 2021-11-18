import datetime


def current_date():
    return datetime.datetime.now().strftime("%Y-%b-%d")


def current_date_plus_1():
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def date_abbr_month_and_time_minus_day():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%b-%d %H:%m")


def date_abbr_month_plus_100_years():
    return (datetime.datetime.now() + datetime.timedelta(days=36524)).strftime("%Y-%b-%d")

