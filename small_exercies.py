import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print("execution time (in microseconds): ", (end - start).microseconds)

    return wrapper


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}


@execution_time
def solution_1(roll_number: list, sample_dict: dict):
    print("List: ", roll_number)
    print("Dictionnary: ", sample_dict)
    for element in roll_number:
        if element not in sample_dict.values():
            roll_number.remove(element)
    print("After removing unwanted elements from list:", roll_number)


@execution_time
def solution_2(roll_number: list, sample_dict: dict):
    print("List: ", roll_number)
    print("Dictionnary: ", sample_dict)
    roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
    print("After removing unwanted elements from list:", roll_number)


# solution_1(roll_number, sample_dict)
solution_2(roll_number, sample_dict)
