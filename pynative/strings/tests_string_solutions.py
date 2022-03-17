import solution

def test_problem(capsys):
    solution.Solution.problem()

    captured = capsys.readouterr()
    out, _ = captured.out, captured.err
    expected_out = "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n"

    assert out == expected_out
