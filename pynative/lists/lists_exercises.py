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
