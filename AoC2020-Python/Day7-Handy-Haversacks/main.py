""" * ADVENT OF CODE 2020 - DAY 7 - HANDY HAVERSACKS * """


# * ------------ PRE-PUZZLE CODE ------------ *

# imports
from os import system

# clear screen for readability
system("cls")

# the input file we are using for this puzzle
PUZZLE_FILE_INPUT = "pie.txt"

# colors for print statements
COLOR_HEADER = "\033[95m" + "\033[1m"
COLOR_QUESTION = "\033[94m"
COLOR_ANSWER = "\033[92m"
COLOR_CLEAR = "\033[0m"

# write title and day
print(f"{COLOR_HEADER} Advent of Code 2020 ")
print(f" Day 7 - Handy Haversacks \n{COLOR_CLEAR}")

# grab puzzle input and store in list
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    puzzle_input = file.read().split(".\n")[:-1]


# * ------------ PUZZLE PART 1 ------------ *     --> STILL A WIP

TARGET_BAG = "shiny gold"
for element in puzzle_input:
    x = element.lower().find(TARGET_BAG)
    if x != -1:
        print(element)
        print("good")

# write question and answer for part 1
print(
    f"{COLOR_QUESTION}How many bag colors can eventually contain at least one shiny gold bag? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(0)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# write question and answer for part 2
print(
    f"{COLOR_QUESTION}How many individual bags are required inside your single shiny gold bag? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(0)} \n {COLOR_CLEAR}")
