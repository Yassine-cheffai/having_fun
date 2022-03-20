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


def test_exercise_5():
    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    expected_result = {"name": "Kelly", "salary": 8000}

    assert Solution.exercise_5(sample_dict, keys) == expected_result


def test_exercise_6():
    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

    # Keys to remove
    keys = ["name", "salary"]
    expected_result = {"city": "New york", "age": 25}

    assert Solution.exercise_6(sample_dict, keys) == expected_result


def test_exercise_8():
    # rename dict key
    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
    key = "city"
    new_key = "location"
    expected_result = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "location": "New york",
    }

    assert Solution.exercise_8(sample_dict, key, new_key) == expected_result


def test_exercise_9():
    sample_dict = {"Physics": 82, "Math": 65, "history": 75}

    expected_result = "Math"
    assert Solution.exercise_9(sample_dict) == expected_result
