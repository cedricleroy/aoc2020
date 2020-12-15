from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def run():
    data = [int(d) for d in read_data(Path(__file__).parent / "inputs")]
    for m in data:
        for n in data:
            if m + n == 2020:
                print(m * n)


if __name__ == "__main__":
    run()
