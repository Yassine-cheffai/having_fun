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

    @staticmethod
    def exercise_5(sample_dict: Dict, keys: List[str]) -> Dict:
        return {k: sample_dict[k] for k in keys}

    @staticmethod
    def exercise_6(sample_dict: Dict, keys: List[str]) -> Dict:
        for key in keys:
            sample_dict.pop(key)
        return sample_dict

    @staticmethod
    def exercise_8(sample_dict: Dict, key: str, new_key: str) -> Dict:
        sample_dict[new_key] = sample_dict.pop(key)
        return sample_dict

    @staticmethod
    def exercise_9(sample_dict: Dict) -> str:
        return min(sample_dict, key=sample_dict.get)
