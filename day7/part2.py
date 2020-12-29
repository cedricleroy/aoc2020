from pprint import pprint
from pathlib import Path
from typing import List, Dict
from collections import namedtuple

Bag = namedtuple("Bag", ["name", "qty"])


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def parse(rule: str) -> Dict[str, List[Bag]]:
    target, contains = rule.split(" bags contain ")
    contains = contains.replace(" bags", "").replace(" bag", "")
    print(target, "->", contains)
    c = {}
    for contain in contains.split(", "):
        if "no other" in contain:
            continue
        l = c.setdefault(target, [])
        l.append(
            Bag(
                " ".join(contain.split(" ")[1:]).replace(".", ""),
                int(contain.split(" ")[0]),
            )
        )
    return c


def count(name: str, bags: Dict[str, List[Bag]]) -> int:
    nb = 0
    bags_list = bags.get(name)
    if not bags_list:
        return 0
    for bag in bags_list:
        nb += bag.qty
        nb += bag.qty * count(bag.name, bags)
    return nb


def compute(data: List[str]) -> int:
    bags = {}
    for rule in data:
        parsed = parse(rule)
        bags.update(parsed)
    nb = count("shiny gold", bags)
    return nb


def test():
    data = read_data(Path("example"))
    assert compute(data) == 32
    data = read_data(Path("example2"))
    assert compute(data) == 126


def run():
    data = read_data(Path("inputs"))
    print(compute(data))


if __name__ == "__main__":
    test()
    run()
