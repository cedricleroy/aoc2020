from pathlib import Path
from typing import List


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def run():
    grid = []
    for row in read_data(Path(__file__).parent / "inputs"):
        grid.append(row)
    grid_height = len(grid)
    grid_width = len(grid[0])
    i = 0
    j = 0
    trees = 0
    while True:
        i += 3
        j += 1
        if j >= grid_height:
            break
        if i >= grid_width:
            i -= grid_width
        if grid[j][i] == "#":
            trees += 1
    print(trees)


if __name__ == "__main__":
    run()
