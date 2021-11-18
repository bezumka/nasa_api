from utils.time_utils import current_date_plus_1

date_max_plus_1_day = {
    'date-max': '+1'
}

date_max_plus_100_years = {
    'date-max': '+36525'
}

date_more_than_100_years = {
    'date-max': '+36526'
}

static_date = {
    'date-max': current_date_plus_1()
}

wrong_static_date = {
    'date-max': '02021-01-01'
}

empty_static_date = {
    'date-max': ''
}

integer_value = {
    'date-max': 20211018
}

double_date_max = {
    'date-max': [current_date_plus_1(), current_date_plus_1()]
}