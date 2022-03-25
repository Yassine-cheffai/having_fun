import datetime
from dates_exercises import Solution


def test_exercise_1(capsys):
    Solution.exercise_1()
    captured = capsys.readouterr()
    out = captured.out
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    assert out == now


def test_exercise_2(capsys):
    date_string = "Feb 25 2020 4:20PM"
    Solution.exercise_2(date_string)
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "2020-02-25 16:20:00"
    assert out == expected_result


def test_exercise_3():
    given_date = datetime.datetime(2020, 2, 25)
    days_to_substract = 7
    expected_result = datetime.datetime(2020, 2, 18)
    assert Solution.exercise_3(given_date, days_to_substract) == expected_result


def test_exercise_4():
    given_date = datetime.datetime(2020, 2, 25)
    expected_output = "Tuesday 25 February 2020"
    assert Solution.exercise_4(given_date) == expected_output


def test_exercise_5():
    given_date = datetime.datetime(2020, 7, 26)
    expected_result = "Sunday"
    assert Solution.exercise_5(given_date) == expected_result


def test_exercise_6():
    # 2020-03-22 10:00:00
    given_date = datetime.datetime(2020, 3, 22, 10, 0, 0)
    expected_result = "2020-03-29 22:00:00"

    assert Solution.exercise_6(given_date) == expected_result


def test_exercise_9():
    # 2020-02-25
    given_date = datetime.datetime(2020, 2, 25).date()
    expected_result = "2020-06-25"
    months_to_add = 4
    assert Solution.exercise_9(given_date, months_to_add) == expected_result
