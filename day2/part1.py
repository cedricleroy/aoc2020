from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def is_valid(line: str) -> bool:
    rule, password = line.split(":")
    occurrences_boundaries, letter = rule.split(" ")
    low, high = occurrences_boundaries.split("-")
    occurrences = sum([1 if c == letter else 0 for c in password])
    if int(low) <= occurrences <= int(high):
        return True
    return False


def run():
    data = read_data(Path(__file__).parent / "inputs")
    valid = 0
    for line in data:
        if is_valid(line):
            valid += 1
    print(valid)


if __name__ == "__main__":
    run()
