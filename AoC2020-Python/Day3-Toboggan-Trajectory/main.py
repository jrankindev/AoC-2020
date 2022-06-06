""" * ADVENT OF CODE 2020 - DAY 3 - TOBOGGAN TRAJECTORY * """


# * ------------ PRE-PUZZLE CODE ------------ *

# imports
from os import system
import math

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
print(f" Day 3 - Toboggan Trajectory \n{COLOR_CLEAR}")

# grab puzzle input and store in list
puzzle_input = []
with open(PUZZLE_FILE_INPUT, encoding="UTF-8") as file:
    for line in file:
        line = line.strip()
        puzzle_input.append(line)


# * ------------ PUZZLE PART 1 ------------ *


def find_trees(rise, run):
    """function to calculate how many trees you would hit in a given slope"""

    # get width of one input line (they are all the same width)
    hill_width = len(puzzle_input[0])

    # count trees for given slope
    start_position = 0
    trees = 0
    for element in puzzle_input[::rise]:  #:: is slice operator to skip by rise value
        if (
            element[(start_position % hill_width)] == "#"
        ):  # modulus can be used for wrap around functionality
            trees += 1
        start_position += run

    return trees


TREE_COUNT = find_trees(1, 3)

# write question and answer for part 1
print(
    f"{COLOR_QUESTION}Starting at the top-left corner of your map and following a slope"
    + " of right 3 and down 1, how many trees would you encounter? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(TREE_COUNT)} \n {COLOR_CLEAR}")


# * ------------ PUZZLE PART 2 ------------ *

tree_count_list = []
tree_count_list.append(find_trees(1, 1))
tree_count_list.append(find_trees(1, 3))
tree_count_list.append(find_trees(1, 5))
tree_count_list.append(find_trees(1, 7))
tree_count_list.append(find_trees(2, 1))

# write question and answer for part 2
print(
    f"{COLOR_QUESTION}What do you get if you multiply together the number of trees"
    + " encountered on each of the listed slopes? ",
    end="",
)
print(f"{COLOR_ANSWER} {str(math.prod(tree_count_list))} \n {COLOR_CLEAR}")
