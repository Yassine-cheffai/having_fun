from typing import Dict
import json
from dataclasses import dataclass


@dataclass
class Vehicle:
    name: str
    engine: str
    price: int

    def as_json(self):
        return json.dumps(self.__dict__, indent=2)

    @classmethod
    def from_json(cls, input_json: str):
        data = json.loads(input_json)
        return cls(name=data["name"], engine=data["engine"], price=data["price"])


def exercise_1(data: Dict[str, str]) -> str:
    return json.dumps(data)


def exercise_2(sample_json: str) -> str:
    return json.loads(sample_json)["key2"]


def exercise_4(sample_json: Dict):
    sorted_dict = {}
    for key in sorted(sample_json.keys()):
        sorted_dict[key] = sample_json[key]
    with open("test_file.txt", "w") as f:
        content = json.dumps(sorted_dict, indent=2)
        f.write(content)
