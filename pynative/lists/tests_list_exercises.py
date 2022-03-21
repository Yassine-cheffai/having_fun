from lists_exercises import Solution


def test_exercise_1():
    list1 = [100, 200, 300, 400, 500]
    expected_result = [500, 400, 300, 200, 100]
    assert Solution.exercise_1(list1) == expected_result


def test_exercise_2():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    expected_result = ["My", "name", "is", "Kelly"]

    assert Solution.exercise_2(list1, list2) == expected_result


def test_exercise_3():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    expected_result = [1, 4, 9, 16, 25, 36, 49]

    assert Solution.exercise_3(numbers) == expected_result


def test_exercise_4():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    expected_result = ["Hello Dear", "Hello Sir", "take Dear", "take Sir"]

    assert Solution.exercise_4(list1, list2) == expected_result
