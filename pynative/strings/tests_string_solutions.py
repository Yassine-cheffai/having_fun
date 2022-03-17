from string_solutions import Solution


def test_problem_2(capsys):
    Solution.problem_2()

    captured = capsys.readouterr()
    out, _ = captured.out, captured.err
    expected_out = "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n"

    assert out == expected_out


def test_problem_3():
    expected_result = 55
    input = 10
    assert Solution.problem_3(input) == expected_result


def test_problem_4(capsys):
    Solution.problem_4()
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n"

    assert out == expected_result


def test_problem_5(capsys):
    numbers = [12, 75, 150, 180, 145, 525, 50]
    Solution.problem_5(numbers)
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "75\n150\n145\n"

    assert out == expected_result


def test_problem_6():
    assert Solution.problem_6(75869) == 5


def test_problem_7(capsys):
    Solution.problem_7()
    expected_result = "5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"
    captured = capsys.readouterr()
    out = captured.out
    assert out == expected_result


def test_problem_8(capsys):
    input_list = [10, 20, 30, 40, 50]
    Solution.problem_8(input_list)
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "50\n40\n30\n20\n10\n"

    assert out == expected_result


def test_problem_9(capsys):
    Solution.problem_9()
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "-10\n-9\n-8\n-7\n-6\n-5\n-4\n-3\n-2\n-1\n"

    assert out == expected_result


def test_problem10(capsys):
    Solution.problem_10()
    captured = capsys.readouterr()
    out = captured.out
    expected_result = "0\n1\n2\n3\n4\n5\nDone!\n"

    assert out == expected_result


def test_problem11():
    expected_result = [29, 31, 37, 41, 43, 47]
    assert Solution.problem_11(25, 50) == expected_result


def test_problem12():
    fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert Solution.problem_12() == fib_seq


def test_problem13():
    assert Solution.problem_13(5) == 120


def test_problem14():
    assert Solution.problem_14(76542) == 24567
