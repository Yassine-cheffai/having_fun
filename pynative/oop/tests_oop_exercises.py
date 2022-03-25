import oop_exercises


def test_exercise_1():
    vehicle = oop_exercises.exercise_1()
    assert vehicle.max_speed == 180 and vehicle.mileage == 3000


def test_exercise_4():
    bus = oop_exercises.exercise_4()
    assert bus.capacity == 50


def test_exercise_5():
    vehicle = oop_exercises.exercise_1()
    assert vehicle.color == "white"


def test_equal():
    vehicle_1 = oop_exercises.Vehicle("v1", 160, 25000)
    vehicle_2 = oop_exercises.Vehicle("v2", 160, 25000)
    assert vehicle_1 == vehicle_2


def test_class():
    vehicle_1 = oop_exercises.Vehicle("v1", 180, 25000)
    assert type(vehicle_1) == oop_exercises.Vehicle


def test_isinstance():
    vehicle_1 = oop_exercises.Bus("B1", 120, 85000)
    assert isinstance(vehicle_1, oop_exercises.Vehicle)


def test_issubclass():
    assert issubclass(oop_exercises.Bus, oop_exercises.Vehicle)
