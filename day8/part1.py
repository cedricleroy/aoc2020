from pathlib import Path
from typing import List, Tuple


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def get_hash(operation: str, argument: int, index: int) -> str:
    return f"{operation} - {argument} - {index}"


def compute(instructions: List[Tuple[str, int]]) -> int:
    index = 0
    acc = 0
    already = set()
    while True:
        operation, argument = instructions[index]
        hashed = get_hash(operation, argument, index)
        print(operation, argument)
        if hashed in already:
            break
        if operation == "acc":
            acc += argument
            index += 1
        elif operation == "jmp":
            index += argument
        elif operation == "nop":
            index += 1
        print(acc)
        already.add(hashed)
    return acc


def transform(data: List[str]) -> List[Tuple[str, int]]:
    return [(d.split(" ")[0], int(d.split(" ")[1].replace("+", ""))) for d in data]


def test():
    data = transform(read_data(Path("example")))
    result = compute(data)
    assert result == 5


def run():
    data = transform(read_data(Path("inputs")))
    print(compute(data))


if __name__ == "__main__":
    test()
    run()
