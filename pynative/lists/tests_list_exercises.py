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


def test_exercise_5(capsys):
    expected_result = "10 400\n20 300\n30 200\n40 100\n"
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    Solution.exercise_5(list1, list2)
    captured = capsys.readouterr()
    out = captured.out
    assert out == expected_result


def test_exercise_9():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    number = 20
    new_number = 200
    expected_result = [5, 10, 15, 200, 25, 50, 20]
    assert Solution.exercise_9(list1, number, new_number) == expected_result


def test_exercise_10():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    expected_result = [5, 15, 25, 50]
    number_to_remove = 20
    assert Solution.exercise_10(list1, number_to_remove) == expected_result
