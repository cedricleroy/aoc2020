from pathlib import Path
from typing import List, Tuple


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def transform(data: List[str]) -> List[int]:
    return [int(d) for d in data]


def can_sum(candidates: List[int], number: int) -> bool:
    length = len(candidates)
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            if candidates[i] + candidates[j] == number:
                return True
    return False


def compute(data: List[int], base: int) -> int:
    for i, number in enumerate(data):
        candidates = data[i - base : i]
        if not candidates:
            continue
        if not can_sum(candidates, number):
            return number


def test():
    data = transform(read_data(Path("example")))
    result = compute(data, 5)
    assert result == 127


def run():
    data = transform(read_data(Path("inputs")))
    print(compute(data, 25))


if __name__ == "__main__":
    test()
    run()
