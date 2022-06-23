### ADVENT OF CODE 2020 DAY 2 PASSWORD PHILOSOPHY ###


import helper.helper as helper


## * puzzle part 1
def puzzle_part_1(puzzle_input):
    # loop through each line and split out policy rules from password
    # then check if password is correct and if so, add it to correct_count
    correct_count = 0
    for element in puzzle_input:
        split_element = element.split()

        password = split_element[2]  # set password
        # set letter, remove last character of string to clean up colon
        letter = split_element[1][:-1]

        split_rules = split_element[0].split("-")
        min_uses = int(split_rules[0])  # set minimum uses
        max_uses = int(split_rules[1])  # set maximum uses

        # check if password is correct
        if password.count(letter) >= min_uses and password.count(letter) <= max_uses:
            correct_count += 1

    # return answer
    return correct_count


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    # loop through each line and split out new policy rules from password
    # check if password is correct and if so, add it to correct_count
    correct_count = 0
    for element in puzzle_input:
        split_element = element.split()

        password = split_element[2]  # set password
        # set letter, remove last character of string to clean up colon
        letter = split_element[1][:-1]

        split_rules = split_element[0].split("-")
        # set first position, adjust for non zero index
        first_position = int(split_rules[0]) - 1
        # set second position, adjust for non zero index
        second_position = int(split_rules[1]) - 1

        # check if password is correct by first checking if more than one position is correct
        # (which is wrong)
        if password[first_position] == letter and password[second_position] != letter:
            correct_count += 1
        elif password[first_position] != letter and password[second_position] == letter:
            correct_count += 1

    # return answer
    return correct_count


## * main function
def main():
    # print title
    helper.print_title("2020", "2", "Password Philosophy")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day02/pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "How many passwords are valid according to their policies? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "How many passwords are valid according to the new interpretation of the policies? ",
        answer,
    )


if __name__ == "__main__":
    main()
