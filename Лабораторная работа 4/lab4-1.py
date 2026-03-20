# TODO решите задачу
import json


def task() -> float:
    total = 0.0

    with open("input.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for item in data:
            total += item["score"] * item["weight"]

    return round(total, 3)

print(task())
