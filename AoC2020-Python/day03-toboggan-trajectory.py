### ADVENT OF CODE 2020 DAY 3 TOBOGGAN TRAJECTORY ###


import helper.helper as helper
import math


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
    # print title
    helper.print_title("2020", "3", "Toboggan Trajectory")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day03/pi.txt")

    # solve puzzle part 1 and 2 in list
    tree_count_list = []
    tree_count_list.append(find_trees(puzzle_input, 1, 1))
    tree_count_list.append(find_trees(puzzle_input, 3, 1))
    tree_count_list.append(find_trees(puzzle_input, 5, 1))
    tree_count_list.append(find_trees(puzzle_input, 7, 1))
    tree_count_list.append(find_trees(puzzle_input, 1, 2))

    # part 1 print QA
    answer = tree_count_list[1]
    helper.print_question_answer(
        "Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? ",
        answer,
    )

    # solve part 2 and print QA
    answer = str(math.prod(tree_count_list))
    helper.print_question_answer(
        "What do you get if you multiply together the number of trees encountered on each of the listed slopes? ",
        answer,
    )


if __name__ == "__main__":
    main()
