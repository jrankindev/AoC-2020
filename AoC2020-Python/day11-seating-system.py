### ADVENT OF CODE 2020 DAY 11 SEATING SYSTEM ###


import helper.helper as helper

## * puzzle part 1
def puzzle_part_1(puzzle_input):
    print("p1")


## * main function
def main():
    # print title
    helper.print_title("2020", "11", "Seating System")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day10/pi.txt")

    # solve part 1 and print QA
    puzzle_part_1(puzzle_input)
    answer = 0
    helper.print_question_answer(
        "How many seats end up occupied? ",
        answer,
    )

    # solve part 2 and print QA
    answer = 0
    helper.print_question_answer(
        "Unknown ",
        answer,
    )


if __name__ == "__main__":
    main()
