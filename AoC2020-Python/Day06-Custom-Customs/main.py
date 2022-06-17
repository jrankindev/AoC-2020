### ADVENT OF CODE 2020 DAY 6 CUSTOM CUSTOMS ###


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
        return puzzle_input


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
    # store all customs answers per group in a set
    # the set will give unique values, so just add them up
    total_answers = 0
    for element in puzzle_input:
        customs_set = set(element)
        total_answers += len(customs_set)

    # return answer
    return total_answers


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    # first, figure out how many are in each group
    # then put all letters into a set to determine the unique letters
    # loop on each unique letter and count how many of them there are
    # if the count of each letter is the same as number in each group, then add to answer
    total_answers = 0
    for element in puzzle_input:
        group_list = element.split(" ")
        group_count = len(group_list)

        element = element.replace(" ", "")
        repeated_letters = set()
        for char in element:
            repeated_letters.add(char)

        for char in repeated_letters:
            character_count = element.count(char)
            if character_count == group_count:
                total_answers += 1

    # return answer
    return total_answers


## * main function
def main():
    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    # print title
    print_title("2020", "6", "Custom Customs")

    # get puzzle input
    puzzle_input = load_puzzle_input("pi.txt", 0)

    # get rid of blank lines
    puzzle_input = puzzle_input.split("\n\n")

    # move customs info to single line and remove spaces
    puzzle_input_p1 = [
        line.replace("\n", " ").replace(" ", "") for line in puzzle_input
    ]

    # move customs info to single line and keep spaces for part 2
    puzzle_input_p2 = [line.replace("\n", " ") for line in puzzle_input]

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input_p1)
    print_question_answer(
        "What is the sum of those counts? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input_p2)
    print_question_answer(
        "What is the sum of those counts? ", answer,
    )


if __name__ == "__main__":
    main()
