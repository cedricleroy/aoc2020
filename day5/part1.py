from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def decode(info: str, upper: str, lower: str) -> int:
    nb = list(range(2 ** len(info)))
    for i in info:
        half = int(len(nb) / 2)
        if i == lower:
            nb = nb[:half]
        elif i == upper:
            nb = nb[half:]
    assert len(nb) == 1
    return nb[0]


def decode_all(boarding_pass: str) -> int:
    row = decode(boarding_pass[:7], "B", "F")
    column = decode(boarding_pass[7:], "R", "L")
    return row * 8 + column


def run():
    data = read_data(Path(__file__).parent / "inputs")
    print(max(decode_all(d) for d in data))


def tests():
    assert decode_all("FBFBBFFRLR") == 357
    assert decode_all("BFFFBBFRRR") == 567
    assert decode_all("FFFBBBFRRR") == 119
    assert decode_all("BBFFBBFRLL") == 820


if __name__ == "__main__":
    tests()
    run()
