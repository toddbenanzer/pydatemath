from datetime import datetime
import datemath


def test_datestr_to_datetime():
    assert datemath.datestr_to_datetime('2023-01-01') == datetime(2023, 1, 1)


def test_datetime_to_datestr():
    assert datemath.datetime_to_datestr(datetime(2023, 1, 1)) == '2023-01-01'


def test_start_of_month():
    assert datemath.start_of_month('2023-01-15') == '2023-01-01'
    assert datemath.start_of_month('2023-02-28') == '2023-02-01'
    assert datemath.start_of_month('2023-02-01') == '2023-02-01'


def test_start_of_prev_month():
    assert datemath.start_of_prev_month('2023-01-15') == '2022-12-01'
    assert datemath.start_of_prev_month('2024-03-15') == '2024-02-01'
    assert datemath.start_of_prev_month('2024-02-29') == '2024-01-01'


def test_start_of_next_month():
    assert datemath.start_of_next_month('2023-01-15') == '2023-02-01'
    assert datemath.start_of_next_month('2023-01-31') == '2023-02-01'
    assert datemath.start_of_next_month('2022-12-31') == '2023-01-01'
    assert datemath.start_of_next_month('2024-02-29') == '2024-03-01'


def test_end_of_month():
    assert datemath.end_of_month('2023-01-15') == '2023-01-31'
    assert datemath.end_of_month('2023-02-15') == '2023-02-28'
    assert datemath.end_of_month('2023-03-15') == '2023-03-31'
    assert datemath.end_of_month('2023-04-15') == '2023-04-30'
    assert datemath.end_of_month('2023-05-15') == '2023-05-31'
    assert datemath.end_of_month('2023-06-15') == '2023-06-30'
    assert datemath.end_of_month('2023-07-15') == '2023-07-31'
    assert datemath.end_of_month('2023-08-15') == '2023-08-31'
    assert datemath.end_of_month('2023-09-15') == '2023-09-30'
    assert datemath.end_of_month('2023-10-15') == '2023-10-31'
    assert datemath.end_of_month('2023-11-15') == '2023-11-30'
    assert datemath.end_of_month('2023-12-15') == '2023-12-31'
    assert datemath.end_of_month('2024-02-01') == '2024-02-29'


def test_end_of_next_month():
    assert datemath.end_of_next_month('2023-01-15') == '2023-02-28'
    assert datemath.end_of_next_month('2023-02-15') == '2023-03-31'
    assert datemath.end_of_next_month('2023-03-15') == '2023-04-30'
    assert datemath.end_of_next_month('2023-04-15') == '2023-05-31'
    assert datemath.end_of_next_month('2023-05-15') == '2023-06-30'
    assert datemath.end_of_next_month('2023-06-15') == '2023-07-31'


def test_end_of_prev_month():
    assert datemath.end_of_prev_month('2023-01-15') == '2022-12-31'
    assert datemath.end_of_prev_month('2023-02-15') == '2023-01-31'
    assert datemath.end_of_prev_month('2023-03-15') == '2023-02-28'
    assert datemath.end_of_prev_month('2023-04-15') == '2023-03-31'
    assert datemath.end_of_prev_month('2023-11-15') == '2023-10-31'
    assert datemath.end_of_prev_month('2023-12-15') == '2023-11-30'
    assert datemath.end_of_prev_month('2024-03-01') == '2024-02-29'


def test_add_months():
    assert datemath.add_months('2023-01-15', 1) == '2023-02-28'
    assert datemath.add_months('2023-01-15', 2) == '2023-03-31'
    assert datemath.add_months('2023-01-15', 16) == '2024-05-31'
    assert datemath.add_months('2023-01-15', -1) == '2022-12-31'
    assert datemath.add_months('2023-01-15', -2) == '2022-11-30'
    assert datemath.add_months('2023-01-15', -14) == '2021-11-30'
    assert datemath.add_months('2023-01-15', 0) == '2023-01-31'


def test_get_previous_xday():
    assert datemath.get_previous_xday('2023-06-25', 'Sunday') == '2023-06-25'
    assert datemath.get_previous_xday('2023-06-25', 'Saturday') == '2023-06-24'
    assert datemath.get_previous_xday('2023-06-25', 'Friday') == '2023-06-23'
    assert datemath.get_previous_xday('2023-06-25', 'Thursday') == '2023-06-22'
    assert datemath.get_previous_xday('2023-06-25', 'Wednesday') == '2023-06-21'
    assert datemath.get_previous_xday('2023-06-25', 'Tuesday') == '2023-06-20'
    assert datemath.get_previous_xday('2023-06-25', 'Monday') == '2023-06-19'


def test_start_of_week():
    assert datemath.start_of_week('2023-06-24') == '2023-06-24'
    assert datemath.start_of_week('2023-06-25') == '2023-06-24'
    assert datemath.start_of_week('2023-06-26') == '2023-06-24'
    assert datemath.start_of_week('2023-06-27') == '2023-06-24'
    assert datemath.start_of_week('2023-06-28') == '2023-06-24'
    assert datemath.start_of_week('2023-06-29') == '2023-06-24'
    assert datemath.start_of_week('2023-06-30') == '2023-06-24'
    assert datemath.start_of_week('2023-07-01') == '2023-07-01'


def test_end_of_week():
    assert datemath.end_of_week('2023-06-24') == '2023-06-30'
    assert datemath.end_of_week('2023-06-25') == '2023-06-30'
    assert datemath.end_of_week('2023-06-26') == '2023-06-30'
    assert datemath.end_of_week('2023-06-27') == '2023-06-30'
    assert datemath.end_of_week('2023-06-28') == '2023-06-30'
    assert datemath.end_of_week('2023-06-29') == '2023-06-30'
    assert datemath.end_of_week('2023-06-30') == '2023-06-30'
    assert datemath.end_of_week('2023-07-01') == '2023-07-07'


def test_end_of_prev_week():
    assert datemath.end_of_prev_week('2023-06-24') == '2023-06-23'
    assert datemath.end_of_prev_week('2023-06-25') == '2023-06-23'
    assert datemath.end_of_prev_week('2023-06-29') == '2023-06-23'
    assert datemath.end_of_prev_week('2023-06-30') == '2023-06-23'
    assert datemath.end_of_prev_week('2023-07-01') == '2023-06-30'
    assert datemath.end_of_prev_week('2023-07-02') == '2023-06-30'


def test_start_of_prev_week():
    assert datemath.start_of_prev_week('2023-06-24') == '2023-06-17'
    assert datemath.start_of_prev_week('2023-07-01') == '2023-06-24'


def test_end_of_next_week():
    assert datemath.end_of_next_week('2023-06-24') == '2023-07-07'
    assert datemath.end_of_next_week('2023-06-25') == '2023-07-07'
    assert datemath.end_of_next_week('2023-07-01') == '2023-07-14'


def test_start_of_next_week():
    assert datemath.start_of_next_week('2023-06-24') == '2023-07-01'
    assert datemath.start_of_next_week('2023-07-01') == '2023-07-08'


def test_add_weeks():
    assert datemath.add_weeks('2023-06-24', 0) == '2023-06-30'
    assert datemath.add_weeks('2023-06-24', 1) == '2023-07-07'
    assert datemath.add_weeks('2023-06-24', 12) == '2023-09-22'
    assert datemath.add_weeks('2023-06-24', -1) == '2023-06-23'
    assert datemath.add_weeks('2023-06-24', -3) == '2023-06-09'
    assert datemath.add_weeks('2023-06-24', -12) == '2023-04-07'


def test_start_of_year():
    assert datemath.start_of_year('2023-06-24') == '2023-01-01'


def test_end_of_year():
    assert datemath.end_of_year('2023-06-24') == '2023-12-31'


def test_start_of_prev_year():
    assert datemath.start_of_prev_year('2023-06-24') == '2022-01-01'


def test_end_of_prev_year():
    assert datemath.end_of_prev_year('2023-06-24') == '2022-12-31'


def test_start_of_next_year():
    assert datemath.start_of_next_year('2023-06-24') == '2024-01-01'


def test_end_of_next_year():
    assert datemath.end_of_next_year('2023-06-24') == '2024-12-31'


def test_add_years():
    assert datemath.add_years('2023-06-24', 0) == '2023-12-31'
    assert datemath.add_years('2023-06-24', 1) == '2024-12-31'
    assert datemath.add_years('2023-06-24', 2) == '2025-12-31'
    assert datemath.add_years('2023-06-24', -1) == '2022-12-31'
    assert datemath.add_years('2023-06-24', -2) == '2021-12-31'


def test_get_mob1():
    assert datemath.get_mob1('2023-06-24') == '2023-06-30'


def test_get_mob3():
    assert datemath.get_mob3('2023-06-24') == '2023-08-31'


def test_get_mob6():
    assert datemath.get_mob6('2023-06-24') == '2023-11-30'


def test_get_mob12():
    assert datemath.get_mob12('2023-06-24') == '2024-05-31'


def test_get_mobn1():
    assert datemath.get_mobn1('2023-06-24') == '2023-05-31'


def test_get_wob1():
    assert datemath.get_wob1('2023-06-24') == '2023-06-30'


def test_get_wobn1():
    assert datemath.get_wobn1('2023-06-24') == '2023-06-23'


def test_today():
    assert datemath.today() == datetime.now().strftime('%Y-%m-%d')