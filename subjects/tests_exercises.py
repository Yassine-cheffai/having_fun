from exercises import func


def test_exercise_1(capsys):

    result = func(4, 4, 4)
    captured = capsys.readouterr()
    out = captured.out
    expected_result = 6
    expected_out = "you called func(4, 4, 4)\nit returned 6\n6\n"

    assert expected_result == result
    assert expected_out == out
