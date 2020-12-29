from collections import defaultdict
from copy import copy
from pathlib import Path
from typing import List, Optional


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def transform(data: List[str]) -> List[int]:
    return [int(d) for d in data]


def compute(data: List[int]) -> Optional[int]:
    data = copy(data)
    data.append(max(data) + 3)
    max_jolt = max(data)
    differences = defaultdict(int)
    allowed_jolts = (1, 2, 3)
    jolt = 0
    while True:
        for adapter_jolt in allowed_jolts:
            if (jolt + adapter_jolt) in data:
                differences[adapter_jolt] += 1
                jolt += adapter_jolt
                break
        else:
            return None
        if jolt == max_jolt:
            break
    return differences[1] * differences[3]


def test():
    data = transform(read_data(Path("example1")))
    result = compute(data)
    assert result == 35
    data = transform(read_data(Path("example2")))
    result = compute(data)
    assert result == 220


def run():
    data = transform(read_data(Path("inputs")))
    print(compute(data))


if __name__ == "__main__":
    test()
    run()
