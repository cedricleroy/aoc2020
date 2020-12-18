import re
from pathlib import Path
from typing import List, Dict


ALLOWED_CHARACTERS = [c for c in "0123456789abcdef"]


def read_data(path: Path) -> List[str]:
    with open(path) as f:
        return [s.strip() for s in f]


def check_fields(fields: Dict[str, str]) -> int:
    byr = int(fields["byr"])
    if byr < 1920 or byr > 2002:
        return 0
    iyr = int(fields["iyr"])
    if iyr < 2010 or iyr > 2020:
        return 0
    eyr = int(fields["eyr"])
    if eyr < 2020 or eyr > 2030:
        return 0
    hgt = fields["hgt"]
    height = int(re.findall(r"\d+", hgt)[0])
    if "cm" in hgt:
        if height < 150 or height > 193:
            return 0
    else:
        if height < 59 or height > 76:
            return 0
    hcl = fields["hcl"]
    if "#" not in hcl:
        return 0
    for c in hcl.split("#")[1]:
        if c not in ALLOWED_CHARACTERS:
            return 0
    ecl = fields["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return 0
    pid = fields["pid"]
    if len(pid) != 9:
        return 0
    return 1


def get_nb_good_passports(passports: List[Dict[str, str]]) -> int:
    good = 0
    for passport in passports:
        len_passport = len(passport)
        if len_passport == 8 or (len_passport == 7 and "cid" not in passport):
            is_good = check_fields(passport)
            good += is_good
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
