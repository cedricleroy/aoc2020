from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def transform(data: List[str]) -> List[int]:
    return [int(d) for d in data]


def find_encryption_weakness(data: List[int], base: int, target: int) -> int:
    for i, number in enumerate(data):
        candidates = data[i - base : i]
        if not candidates:
            continue
        print(candidates)
        if sum(candidates) == target:
            print(candidates)
            return min(candidates) + max(candidates)


def compute(data: List[int], target: int) -> int:
    for base in range(2, 100):
        result = find_encryption_weakness(data, base, target)
        if result is not None:
            return result


def test():
    data = transform(read_data(Path("example")))
    result = compute(data, 127)
    print(result)
    assert result == 62


def run():
    data = transform(read_data(Path("inputs")))
    print(compute(data, 1721308972))


if __name__ == "__main__":
    test()
    run()
