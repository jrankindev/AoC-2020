### ADVENT OF CODE 2020 DAY 1 REPORT REPAIR ###


import helper.helper as helper


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
    # print title
    helper.print_title("2020", "1", "Report Repair")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day01/pi.txt", 1, 0)

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "Find the two entries that sum to 2020; what do you get if you multiply them together? ",
        answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "In your expense report, what is the product of the three entries that sum to 2020? ",
        answer,
    )


if __name__ == "__main__":
    main()
