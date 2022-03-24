from sets_exercises import Solution


def test_exercise_1():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    expected_result = {"Green", "Yellow", "Black", "Orange", "Red", "Blue"}
    assert Solution.exercise_1(sample_set, sample_list) == expected_result


def test_exercise_2():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    expected_result = {40, 50, 30}

    assert Solution.exercise_2(set1, set2) == expected_result


def test_exercise_3():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    expected_result = {70, 40, 10, 50, 20, 60, 30}

    assert Solution.exercise_3(set1, set2) == expected_result


def test_exercise_4():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    expected_result = {10, 30}

    assert Solution.exercise_4(set1, set2) == expected_result


def test_exercise_5():
    set1 = {10, 20, 30, 40, 50}
    to_remove = {10, 20, 30}
    expected_result = {40, 50}

    assert Solution.exercise_5(set1, to_remove) == expected_result


def test_exercise_6():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    expected_result = {20, 70, 10, 60}

    assert Solution.exercise_6(set1, set2) == expected_result
