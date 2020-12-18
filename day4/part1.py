from pathlib import Path
from typing import List, Dict


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def get_nb_good_passports(passports: List[Dict[str, str]]) -> int:
    good = 0
    for passport in passports:
        if len(passport) == 8:
            good += 1
        elif len(passport) == 7 and "cid" not in passport:
            good += 1
    return good


def run():
    data = read_data(Path(__file__).parent / "inputs")
    passports = []
    passport = {}
    for i, line in enumerate(data):
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            for key_value in line.split(" "):
                key, value = key_value.split(":")
                passport[key] = value
        if i == len(data) - 1:
            passports.append(passport)
            passport = {}
    nb_good_passports = get_nb_good_passports(passports)
    print(nb_good_passports)


if __name__ == "__main__":
    run()
