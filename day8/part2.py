from copy import copy
from pathlib import Path
from typing import List, Tuple, Optional


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def get_hash(operation: str, argument: int, index: int) -> str:
    return f"{operation} - {argument} - {index}"


def compute(instructions: List[Tuple[str, int]]) -> Optional[int]:
    index = 0
    acc = 0
    already = set()
    nb_instructions = len(instructions)
    while True:
        operation, argument = instructions[index]
        hashed = get_hash(operation, argument, index)
        if hashed in already:
            return None
        if operation == "acc":
            acc += argument
            index += 1
        elif operation == "jmp":
            index += argument
        elif operation == "nop":
            index += 1
        already.add(hashed)
        if index == nb_instructions:
            break
    return acc


def fix(instructions: List[Tuple[str, int]]) -> int:
    for i, instruction in enumerate(instructions):
        operation, argument = instruction
        if operation == "acc":
            continue
        if operation == "jmp":
            operation = "nop"
        elif operation == "nop":
            operation = "jmp"
        new_instructions = copy(instructions)
        new_instructions[i] = (operation, argument)
        result = compute(new_instructions)
        if result is not None:
            return result


def transform(data: List[str]) -> List[Tuple[str, int]]:
    return [(d.split(" ")[0], int(d.split(" ")[1].replace("+", ""))) for d in data]


def test():
    data = transform(read_data(Path("example")))
    result = fix(data)
    assert result == 8


def run():
    data = transform(read_data(Path("inputs")))
    print(fix(data))


if __name__ == "__main__":
    test()
    run()
