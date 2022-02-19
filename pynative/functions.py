# https://pynative.com/python-functions-exercise-with-solutions/
def ex1(name: str, age: int):
    return f"{name} is {age} years old!"


def test_ex1():
    assert ex1("yassine", 29), "yassine is 29 years old"


def ex2(*args):
    for arg in args:
        print(arg)


def test_ex2(capsys):
    ex2(20, 40, 60)
    captured = capsys.readouterr()
    assert captured.out == "20\n40\n60\n"


def ex4(name: str, salary: int = 9000) -> str:
    return f"Name: {name} salary: {salary}"


def test_ex4():
    assert ex4("Ben", 12000), "Name: Ben salary: 12000"
    assert ex4("Jessa"), "Name: Jessa salary: 9000"


def ex5(a: int, b: int) -> int:
    def addition(a, b):
        return a + b

    return addition(a, b) + 5


def test_ex5():
    assert ex5(2, 8), 15


def ex6(n: int) -> int:
    if n > 0:
        return n + ex6(n - 1)
    return 1


def test_ex6():
    assert ex6, 55
