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


def contains_shinny_gold(bag_name: str, bags: Dict[str, List[Bag]]) -> bool:
    if not bags.get(bag_name):
        return False
    for bag in bags.get(bag_name):
        if bag.name == "shiny gold":
            return True
        if contains_shinny_gold(bag.name, bags):
            return True
    return False


def count(data: Dict[str, List[Bag]], nb: int = 0) -> int:
    for bag_name, bags in data.items():
        if bag_name == "shiny gold":
            continue
        for bag in bags:
            if "shiny gold" == bag.name:
                nb += 1
                break
            if contains_shinny_gold(bag.name, data):
                nb += 1
                break
    return nb


def compute(data: List[str]) -> int:
    bags = {}
    for rule in data:
        parsed = parse(rule)
        bags.update(parsed)
    return count(bags)


def test():
    data = read_data(Path("example"))
    assert compute(data) == 4


def run():
    data = read_data(Path("inputs"))
    print(compute(data))


if __name__ == "__main__":
    test()
    run()
