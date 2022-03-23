from typing import List, Set


class Solution:
    @staticmethod
    def exercise_1(sample_set: Set[str], sample_list: List[str]) -> Set[str]:
        sample_set.update(sample_list)
        return sample_set
