### ADVENT OF CODE 2020 DAY 1 REPORT REPAIR ###


import os


# color constants for print statements
COLOR_HEADER = "\033[95m" + "\033[1m"
COLOR_QUESTION = "\033[94m"
COLOR_ANSWER = "\033[92m"
COLOR_CLEAR = "\033[0m"


## * input loader
# return_type 1 is to load into list, otherwise load in variable
# line_type 1 is to load each line as an int, otherwise load as string
def load_puzzle_input(puzzle_file_input: str, return_type=1, line_type=1):
    if return_type:
        puzzle_input = []
        with open(puzzle_file_input, encoding="UTF-8") as file:
            for line in file:
                if line_type:
                    line = int(line.strip())
                else:
                    line = line.strip()
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
    # loop through puzzle input finding entries that match 2020 - entry
    entries = []
    for element in puzzle_input:
        searcher = 2020 - element
        if searcher in puzzle_input:
            entries.append(element)

    # calculate answer
    return entries[0] * entries[1]


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    # loop through puzzle input twice on different numbers finding entries that
    # match 2020 for both entries
    entries = []
    for element in puzzle_input:
        for element2 in puzzle_input:
            if element != element2:
                both_inputs = element + element2
                searcher = 2020 - both_inputs
                if searcher in puzzle_input and element2 in puzzle_input:
                    entries.append(element)
                    entries.append(element2)
                    entries.append(searcher)

    # calculate answer
    return entries[0] * entries[1] * entries[2]


## * main function
def main():
    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    # print title
    print_title("2020", "1", "Report Repair")

    # get puzzle input
    puzzle_input = load_puzzle_input("pi.txt")

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    print_question_answer(
        "Find the two entries that sum to 2020; what do you get if you multiply them together? ",
        answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    print_question_answer(
        "In your expense report, what is the product of the three entries that sum to 2020?",
        answer,
    )


if __name__ == "__main__":
    main()
