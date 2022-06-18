### ADVENT OF CODE 2020 DAY 3 TOBOGGAN TRAJECTORY ###


import os
import math


## * input loader
# return_type 1 is to load into list, otherwise load in variable
# line_type 1 is to load each line as an string, otherwise load as int
def load_puzzle_input(puzzle_file_input: str, return_type=1, line_type=1):
    if return_type:
        puzzle_input = []
        with open(puzzle_file_input, encoding="UTF-8") as file:
            for line in file:
                if line_type:
                    line = line.strip()
                else:
                    line = int(line.strip())
                puzzle_input.append(line)
        return puzzle_input
    else:
        with open(puzzle_file_input, encoding="UTF-8") as file:
            puzzle_input = file.read()
        return puzzle_input


## * title printer
def print_title(year: str, day: str, title: str):
    color_header = "\033[95m" + "\033[1m"
    color_clear = "\033[0m"
    print(f"{color_header} Advent of Code {year} ")
    print(f" Day {day} - {title} \n{color_clear}")


## * question and answer printer
def print_question_answer(question: str, answer: str):
    color_question = "\033[94m"
    color_answer = "\033[92m"
    color_clear = "\033[0m"
    print(
        f"{color_question}{question}",
        end="",
    )
    print(f"{color_answer} {str(answer)} \n {color_clear}")


## * calculate how many trees you would hit on the puzzle_input given a down and right value
def find_trees(puzzle_input, right: int, down: int):
    # get width of one input line (they are all the same width)
    hill_width = len(puzzle_input[0])

    # count trees for given slope
    start_position = 0
    trees = 0
    for element in puzzle_input[::down]:  # :: is slice operator to skip by down value
        # modulus can be used for wrap around functionality
        if element[(start_position % hill_width)] == "#":
            trees += 1
        start_position += right

    return trees


## * main function
def main():
    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    # print title
    print_title("2020", "3", "Toboggan Trajectory")

    # get puzzle input
    puzzle_input = load_puzzle_input("pi.txt")

    # solve puzzle part 1 and 2 in list
    tree_count_list = []
    tree_count_list.append(find_trees(puzzle_input, 1, 1))
    tree_count_list.append(find_trees(puzzle_input, 3, 1))
    tree_count_list.append(find_trees(puzzle_input, 5, 1))
    tree_count_list.append(find_trees(puzzle_input, 7, 1))
    tree_count_list.append(find_trees(puzzle_input, 1, 2))

    # part 1 print QA
    answer = tree_count_list[1]
    print_question_answer(
        "Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? ",
        answer,
    )

    # solve part 2 and print QA
    answer = str(math.prod(tree_count_list))
    print_question_answer(
        "What do you get if you multiply together the number of trees encountered on each of the listed slopes? ",
        answer,
    )


if __name__ == "__main__":
    main()
