""" * ADVENT OF CODE 2020 - DAY 2 - PASSWORD PHILOSOPHY * """


# * ------------ PRE-PUZZLE CODE ------------ *

# imports
from os import system

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
print(f" Day 2 - Password Philosophy \n{COLOR_CLEAR}")

# grab puzzle input and store in list
puzzle_input = []
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    for line in file:
        line = line.strip()
        puzzle_input.append(line)


# * ------------ PUZZLE PART 1 ------------ *

# loop through each line and split out policy rules from password
# then check if password is correct and if so, add it to CORRECT_COUNT
CORRECT_COUNT = 0
for element in puzzle_input:
    split_element = element.split()

    password = split_element[2]  # set password
    letter = split_element[1][
        :-1
    ]  # set letter, remove last character of string to clean up colon

    split_rules = split_element[0].split("-")
    min_uses = int(split_rules[0])  # set minimum uses
    max_uses = int(split_rules[1])  # set maximum uses

    # check if password is correct
    if password.count(letter) >= min_uses and password.count(letter) <= max_uses:
        CORRECT_COUNT += 1


# write question and answer for part 1
print(
    f"{COLOR_QUESTION}How many passwords are valid according to their policies? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(CORRECT_COUNT)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# loop through each line and split out new policy rules from password
# check if password is correct and if so, add it to CORRECT_COUNT
CORRECT_COUNT = 0
for element in puzzle_input:
    split_element = element.split()

    password = split_element[2]  # set password
    letter = split_element[1][
        :-1
    ]  # set letter, remove last character of string to clean up colon

    split_rules = split_element[0].split("-")
    first_position = (
        int(split_rules[0]) - 1
    )  # set first position, adjust for non zero index
    second_position = (
        int(split_rules[1]) - 1
    )  # set second position, adjust for non zero index

    # check if password is correct by first checking if more than one position is correct
    # (which is wrong)
    if password[first_position] == letter and password[second_position] != letter:
        CORRECT_COUNT += 1
    elif password[first_position] != letter and password[second_position] == letter:
        CORRECT_COUNT += 1

# write question and answer for part 2
print(
    f"{COLOR_QUESTION}How many passwords are valid according to the new interpretation"
    + " of the policies? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(CORRECT_COUNT)} \n {COLOR_CLEAR}")
