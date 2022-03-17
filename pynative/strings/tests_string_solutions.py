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
