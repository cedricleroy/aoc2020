from pathlib import Path

from day5.part1 import read_data, decode_all


def run():
    data = read_data(Path(__file__).parent / "inputs")
    seats = {decode_all(d) for d in data}
    all_seats = set(range((8 * 128) - 1))
    candidates = all_seats - seats
    for candidate in candidates:
        if (candidate - 1) in seats and (candidate + 1) in seats:
            print(candidate)


if __name__ == "__main__":
    run()
