### ADVENT OF CODE 2020 DAY 5 BINARY BOARDING ###


import helper.helper as helper


## * puzzle part 1
def puzzle_part_1(puzzle_input):
    # replace characters with binary equivalent
    binary_puzzle_input = [
        x.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        for x in puzzle_input
    ]

    # convert from string to base 2 (binary) int
    seats = [int(x, 2) for x in binary_puzzle_input]

    # sort to put largest seat id at end of list
    seats.sort()

    # return answer
    return seats[-1], seats


## * puzzle part 2
def puzzle_part_2(seat_list):
    # find seat missing from list in puzzle 1
    my_seat = 0
    seats = seat_list
    for i in range(len(seats)):
        if seats[i + 1] - seats[i] != 1:
            my_seat = seats[i] + 1
            break

    # return answer
    return my_seat


## * main function
def main():
    # print title
    helper.print_title("2020", "5", "Binary Boarding")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day05/pi.txt")

    # solve part 1 and print QA
    answer, seat_list = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "What is the highest seat ID on a boarding pass? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(seat_list)
    helper.print_question_answer(
        "What is the ID of your seat? ", answer,
    )


if __name__ == "__main__":
    main()
