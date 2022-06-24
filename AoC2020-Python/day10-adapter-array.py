### ADVENT OF CODE 2020 DAY 10 ADAPTER ARRAY ###


import helper.helper as helper


## * puzzle part 1
def puzzle_part_1(puzzle_input):
    print("p1")


## * main function
def main():
    # print title
    helper.print_title("2020", "10", "Adapter Array")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day10/pie.txt")

    # solve part 1 and print QA
    puzzle_part_1(puzzle_input)
    answer = 0
    helper.print_question_answer(
        "What is the number of 1-jolt differences multiplied by the number of 3-jolt differences? ", answer,
    )

    # solve part 2 and print QA
    answer = 0
    helper.print_question_answer(
        "Unkown ",
        answer,
    )


if __name__ == "__main__":
    main()
