from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def is_valid(line: str) -> bool:
    rule, password = line.split(":")
    password = password.strip()
    indexes, letter = rule.split(" ")
    index1, index2 = indexes.split("-")
    policy1_status = password[int(index1) - 1] == letter
    policy2_status = password[int(index2) - 1] == letter
    return policy1_status ^ policy2_status


def run():
    data = read_data(Path(__file__).parent / "inputs")
    valid = 0
    for line in data:
        if is_valid(line):
            valid += 1
    print(valid)


if __name__ == "__main__":
    run()
