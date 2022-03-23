from sets_exercises import Solution


def test_exercise_1():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    expected_result = {"Green", "Yellow", "Black", "Orange", "Red", "Blue"}
    assert Solution.exercise_1(sample_set, sample_list) == expected_result
