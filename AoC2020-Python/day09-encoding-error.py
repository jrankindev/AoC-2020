### ADVENT OF CODE 2020 DAY 9 ENCODING ERROR ###


import helper.helper as helper


## * puzzle part 1
def puzzle_part_1(puzzle_input, preamble):
    # loop through every line of the puzzle input
    good_input_found = False
    bad_input = []
    for i in range(len(puzzle_input)):

        # if line is not in the preamble
        if i > preamble:
            scan_range = range(i - preamble, i)
            good_input_found = False

            # loop through each position in the scan range (based on preamble)
            for position in scan_range:
                position = int(position)

                # inner loop through each element in the scan range
                # check to see if current position and element sum to the first loop line value
                # if so, a good input is found, set boolean
                for element in puzzle_input[scan_range[0] : scan_range[-1]]:
                    current_position = int(puzzle_input[position])
                    current_element = int(element)
                    upper_value = int(puzzle_input[i])
                    if (
                        current_position + current_element == upper_value
                        and current_position != current_element
                    ):
                        # sum good
                        good_input_found = True

            # no good input was found, so add first loop line value to list
            if good_input_found == False:
                bad_input.append(puzzle_input[i])

    # return list, should only contain one value
    return bad_input


## * puzzle part 2
def puzzle_part_2(puzzle_input, solution):
    # loop through puzzle input tracking index
    for x in range(len(puzzle_input)):

        # create a blank list for tracking current number sequence
        working_list = []

        # loop through each element in puzzle input starting at index x
        # add the current element to the working list and then sum all values in the working list
        # compare the sum to the solution, it match, return working list as correct sequence
        for element in puzzle_input[x:]:
            working_list.append(int(element))
            current_sum = sum(working_list)
            if current_sum == int(solution) and len(working_list) >= 2:
                return working_list


## * main function
def main():
    # print title
    helper.print_title("2020", "9", "Encoding Error")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day09/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input, 25)[0]
    helper.print_question_answer(
        "What is the first number that does not have this property? ", answer,
    )

    # solve part 2 and print QA
    number_sequence = puzzle_part_2(puzzle_input, answer)
    number_sequence.sort()
    answer = number_sequence[0] + number_sequence[-1]
    helper.print_question_answer(
        "What is the encryption weakness in your XMAS-encrypted list of numbers? ",
        answer,
    )


if __name__ == "__main__":
    main()
