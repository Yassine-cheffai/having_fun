from dict_solutions import Solution


def test_exercise_1():
    keys = ["Ten", "Twenty", "Thirty"]
    values = [10, 20, 30]
    expected_result = {"Ten": 10, "Twenty": 20, "Thirty": 30}
    assert Solution.exercise_1(keys, values) == expected_result


def test_exercise_2():
    dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
    dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}
    expected_result = {"Ten": 10, "Twenty": 20, "Thirty": 30, "Fourty": 40, "Fifty": 50}

    assert Solution.exercise_2(dict1, dict2) == expected_result


def test_exercise_4():
    expected_result = {
        "Kelly": {"designation": "Developer", "salary": 8000},
        "Emma": {"designation": "Developer", "salary": 8000},
    }
    employees = ["Kelly", "Emma"]
    defaults = {"designation": "Developer", "salary": 8000}

    assert Solution.exercise_4(employees, defaults) == expected_result
