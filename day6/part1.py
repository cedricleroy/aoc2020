from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def make_group(data: List[str]) -> List[List[str]]:
    groups = []
    group = []
    for d in data:
        if d == "":
            groups.append(group)
            group = []
            continue
        group.append(d)
    groups.append(group)
    return groups


def sum_of_yes(groups: List[List[str]]) -> int:
    return sum([len({c for c in "".join(g)}) for g in groups])


def test():
    data = read_data(Path("example"))
    groups = make_group(data)
    assert sum_of_yes(groups) == 11


def run():
    data = read_data(Path("inputs"))
    groups = make_group(data)
    print(sum_of_yes(groups))


if __name__ == "__main__":
    test()
    run()
