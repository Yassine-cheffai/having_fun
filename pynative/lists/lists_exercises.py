from typing import List


class Solution:
    @staticmethod
    def exercise_1(list1: List) -> List:
        # return list(reversed(list1))
        return list1[::-1]

    @staticmethod
    def exercise_2(list1: List[str], list2: List[str]) -> List:
        return [i + j for i, j in zip(list1, list2)]

    @staticmethod
    def exercise_3(numbers: List[int]) -> List[int]:
        return [n * n for n in numbers]

    @staticmethod
    def exercise_4(list1: List[str], list2: List[str]) -> List[str]:
        result = []
        for l1 in list1:
            for l2 in list2:
                result.append(f"{l1.strip()} {l2.strip()}")

        return result

    @staticmethod
    def exercise_5(list1: List[int], list2: List[int]):
        for l1, l2 in zip(list1, reversed(list2)):
            print(f"{l1} {l2}")

    @staticmethod
    def exercise_9(list1: List[int], number: int, new_number: int) -> List[int]:
        try:
            index = list1.index(number)
            list1[index] = new_number
            return list1
        except ValueError:
            return list1

    @staticmethod
    def exercise_10(list1: List[int], number_to_remove: int) -> List[int]:
        # slow
        # while number_to_remove in list1:
        # list1.remove(number_to_remove)
        # return list1

        return [i for i in list1 if i != number_to_remove]
