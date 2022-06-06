""" * ADVENT OF CODE 2020 - DAY 1 - REPORT REPAIR * """


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
print(f" Day 1 - Report Repair \n{COLOR_CLEAR}")

# grab puzzle input and store in list
puzzle_input = []
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    for line in file:
        line = int(line.strip())
        puzzle_input.append(line)


# * ------------ PUZZLE PART 1 ------------ *

# loop through puzzle input finding entries that match 2020 - entry
entries = []
for element in puzzle_input:
    searcher = 2020 - element
    if searcher in puzzle_input:
        entries.append(element)

# calculate answer
answer = entries[0] * entries[1]

# write question and answer for part 1
print(
    f"{COLOR_QUESTION}Find the two entries that sum to 2020; what do you get if you"
    + " multiply them together? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(answer)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# loop through puzzle input twice on different numbers finding entries that match 2020
# both entries
entries.clear()
for element in puzzle_input:
    for element2 in puzzle_input:
        if element != element2:
            both_inputs = element + element2
            searcher = 2020 - both_inputs
            if searcher in puzzle_input and element2 in puzzle_input:
                entries.append(element)
                entries.append(element2)
                entries.append(searcher)

# calculate answer
answer = entries[0] * entries[1] * entries[2]

# write question and answer for part 2
print(
    f"{COLOR_QUESTION}In your expense report, what is the product of the three"
    + " entries that sum to 2020? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(answer)} \n {COLOR_CLEAR}")
