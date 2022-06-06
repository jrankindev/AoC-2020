""" * ADVENT OF CODE 2020 - DAY 6 - CUSTOM CUSTOMS * """


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
print(f" Day 6 - Custom Customs \n{COLOR_CLEAR}")

# grab puzzle input and store in variable
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    puzzle_input = file.read()

# get rid of blank lines
puzzle_input = puzzle_input.split("\n\n")

# move customs info to single line and remove spaces
puzzle_input_p1 = [line.replace("\n", " ").replace(" ", "") for line in puzzle_input]

# move customs info to single line and keep spaces for part 2
puzzle_input_p2 = [line.replace("\n", " ") for line in puzzle_input]


# * ------------ PUZZLE PART 1 ------------ *

# store all customs info per group in a set
# the set will give unique values, so just add them up
ANSWER = 0
for element in puzzle_input_p1:
    customs_set = set(element)
    ANSWER += len(customs_set)

# write question and answer for part 1
print(f"{COLOR_QUESTION}What is the sum of those counts? ", end="")
print(f"{COLOR_ANSWER} {str(ANSWER)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# first, figure out how many are in each group
# then put all letters into a set to determine the unique letters
# loop on each unique letter and count how many of them there are
# if the count of each letter is the same as number in each group, then add to answer
ANSWER = 0
for element in puzzle_input_p2:
    group_list = element.split(" ")
    group_count = len(group_list)

    element = element.replace(" ", "")
    repeated_letters = set()
    for char in element:
        repeated_letters.add(char)

    for char in repeated_letters:
        character_count = element.count(char)
        if character_count == group_count:
            ANSWER += 1

# write question and answer for part 2
print(f"{COLOR_QUESTION}What is the sum of those counts? ", end="")
print(f"{COLOR_ANSWER} {str(ANSWER)} \n {COLOR_CLEAR}")
