from typing import List, Set


class Solution:
    @staticmethod
    def exercise_1(sample_set: Set[str], sample_list: List[str]) -> Set[str]:
        sample_set.update(sample_list)
        return sample_set

    @staticmethod
    def exercise_2(set1: Set[int], set2: Set[int]) -> Set[int]:
        return set1.intersection(set2)

    @staticmethod
    def exercise_3(set1: Set[int], set2: Set[int]) -> Set[int]:
        return set1.union(set2)

    @staticmethod
    def exercise_4(set1: Set[int], set2: Set[int]) -> Set[int]:
        return set1.difference(set2)

    @staticmethod
    def exercise_5(set1: Set[int], to_remove: Set[int]) -> Set[int]:
        return set1.difference(to_remove)

    @staticmethod
    def exercise_6(set1: Set[int], set2: Set[int]) -> Set[int]:
        # intersection = set1.intersection(set2)
        # s = set()
        # s.update(set1.difference(intersection))
        # s.update(set2.difference(intersection))

        # return s

        return set1.symmetric_difference(set2)
