import json_exercises


def test_import_json():
    import json

    assert "json" in locals()


def test_exercise_1():
    data = {"key1": "value1", "key2": "value2"}
    expected_result = '{"key1": "value1", "key2": "value2"}'

    assert json_exercises.exercise_1(data) == expected_result


def test_exercise_2():
    sample_json = """{"key1": "value1", "key2": "value2"}"""
    expected_result = "value2"
    assert json_exercises.exercise_2(sample_json) == expected_result


def test_exercise_4():
    sample_json = {"id": 1, "name": "value2", "age": 29}
    json_exercises.exercise_4(sample_json)
    with open("test_file.txt", "r") as f:
        file_result = f.read()

    expected_result = '{\n  "age": 29,\n  "id": 1,\n  "name": "value2"\n}'
    assert file_result == expected_result


def test_exercise_6():
    expected_result = (
        '{\n  "name": "Toyota Rav4",\n  "engine": "2.5L",\n  "price": 32000\n}'
    )
    vehicle = json_exercises.Vehicle("Toyota Rav4", "2.5L", 32000)
    assert vehicle.as_json() == expected_result
