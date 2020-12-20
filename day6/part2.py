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


def all_persons_have_letter(group: List[str], letter: str) -> bool:
    for person in group:
        if letter not in person:
            return False
    return True


def sum_of_yes(groups: List[List[str]]) -> int:
    count = 0
    for group in groups:
        letters = {c for c in "".join(group)}
        for letter in letters:
            if all_persons_have_letter(group, letter):
                count += 1
    return count


def test():
    data = read_data(Path("example"))
    groups = make_group(data)
    assert sum_of_yes(groups) == 6


def run():
    data = read_data(Path("inputs"))
    groups = make_group(data)
    print(sum_of_yes(groups))


if __name__ == "__main__":
    test()
    run()
