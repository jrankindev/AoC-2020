""" * ADVENT OF CODE 2020 - DAY 4 - PASSPORT PROCESSING * """


# * ------------ PRE-PUZZLE CODE ------------ *

# imports
from os import system
import re

# clear screen for readability
system("cls")

# the input file we are using for this puzzle
PUZZLE_FILE_INPUT = "pi.txt"

# colors for print statements
COLOR_HEADER = "\033[95m" + "\033[1m"
COLOR_QUESTION = "\033[94m"
COLOR_ANSWER = "\033[92m"
COLOR_CLEAR = "\033[0m"

# write title and day
print(f"{COLOR_HEADER} Advent of Code 2020 ")
print(f" Day 4 - Passport Processing \n{COLOR_CLEAR}")

# grab puzzle input and store in variable
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    puzzle_input = file.read()

# get rid of blank lines
puzzle_input = puzzle_input.split("\n\n")

# move passport info to single line
puzzle_input = [line.replace("\n", " ") for line in puzzle_input]


# * ------------ PUZZLE PART 1 ------------ *

# store all required fields in list
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# check each passport for required fields
VALID_PASSPORTS = 0
for passport in puzzle_input:
    if all(field in passport for field in required_fields):
        VALID_PASSPORTS += 1

# write question and answer for part 1
print(f"{COLOR_QUESTION}In your batch file, how many passports are valid? ", end="")
print(f"{COLOR_ANSWER} {str(VALID_PASSPORTS)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# check each passport for validation in required fields using regex
VALID_PASSPORTS = 0
for passport in puzzle_input:
    if (
        re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport)
        and re.search(r"iyr:201\d|iyr:20[1-2]0", passport)
        and re.search(r"eyr:202\d|eyr:20[2-3]0", passport)
        and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport)
        and re.search(r"pid:\d{9}\b", passport)
        and re.search(r"hcl:#[A-Fa-f0-9]{6}", passport)
        and re.search(
            r"hgt:15\dcm|hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in",
            passport,
        )
    ):
        VALID_PASSPORTS += 1

# write question and answer for part 2
print(f"{COLOR_QUESTION}In your batch file, how many passports are valid? ", end="")
print(f"{COLOR_ANSWER} {str(VALID_PASSPORTS)} \n {COLOR_CLEAR}")
