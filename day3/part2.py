from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def number_of_trees(right: int, down: int) -> int:
    grid = []
    for row in read_data(Path(__file__).parent / "inputs"):
        grid.append(row)
    grid_height = len(grid)
    grid_width = len(grid[0])
    i = 0
    j = 0
    trees = 0
    while True:
        i += right
        j += down
        if j >= grid_height:
            break
        if i >= grid_width:
            i -= grid_width
        if grid[j][i] == "#":
            trees += 1
    return trees


def run():
    answer = 1
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    for right, down in slopes:
        answer *= number_of_trees(right, down)
    print(answer)


if __name__ == "__main__":
    run()
