from typing import List, Dict


class Solution:
    @staticmethod
    def exercise_1(keys: List[str], values: List[int]) -> Dict[str, int]:
        result = {}
        for key, value in zip(keys, values):
            result[key] = value
        return result

    @staticmethod
    def exercise_2(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
        return {**dict1, **dict2}

    @staticmethod
    def exercise_4(employees: List[str], default: Dict) -> Dict[str, Dict]:
        return dict.fromkeys(employees, default)
