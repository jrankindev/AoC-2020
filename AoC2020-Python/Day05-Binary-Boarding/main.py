""" * ADVENT OF CODE 2020 - DAY 5 - BINARY BOARDING * """


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
print(f" Day 5 - Binary Boarding \n{COLOR_CLEAR}")

# grab puzzle input and store in list
puzzle_input = []
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    for line in file:
        line = line.strip()
        puzzle_input.append(line)


# * ------------ PUZZLE PART 1 ------------ *

# replace characters with binary equivalent
binary_puzzle_input = [
    x.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    for x in puzzle_input
]

# convert from string to base 2 (binary) int
seats = [int(x, 2) for x in binary_puzzle_input]

# sort to find largest seat id
seats.sort()

# write question and answer for part 1
print(f"{COLOR_QUESTION}What is the highest seat ID on a boarding pass? ", end="")
print(f"{COLOR_ANSWER} {str(seats[-1])} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

# find seat missing from list
MY_SEAT = 0
for i, seat_ID in enumerate(seats):
    if seats[i + 1] - seats[i] != 1:
        MY_SEAT = seats[i] + 1
        break

# write question and answer for part 2
print(f"{COLOR_QUESTION}What is the ID of your seat? ", end="")
print(f"{COLOR_ANSWER} {str(MY_SEAT)} \n {COLOR_CLEAR}")
