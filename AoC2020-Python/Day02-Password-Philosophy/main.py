### ADVENT OF CODE 2020 DAY 2 PASSWORD PHILOSOPHY ###


import os


# color constants for print statements
COLOR_HEADER = "\033[95m" + "\033[1m"
COLOR_QUESTION = "\033[94m"
COLOR_ANSWER = "\033[92m"
COLOR_CLEAR = "\033[0m"


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


## * title printer
def print_title(year: str, day: str, title: str):
    print(f"{COLOR_HEADER} Advent of Code {year} ")
    print(f" Day {day} - {title} \n{COLOR_CLEAR}")


## * question and answer printer
def print_question_answer(question: str, answer: str):
    print(
        f"{COLOR_QUESTION}{question}", end="",
    )
    print(f"{COLOR_ANSWER} {str(answer)} \n {COLOR_CLEAR}")


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
    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    # print title
    print_title("2020", "2", "Password Philosophy")

    # get puzzle input
    puzzle_input = load_puzzle_input("pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    print_question_answer(
        "How many passwords are valid according to their policies? ",
        answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    print_question_answer(
        "How many passwords are valid according to the new interpretation of the policies? ",
        answer,
    )


if __name__ == "__main__":
    main()
