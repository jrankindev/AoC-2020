### ADVENT OF CODE 2020 DAY 6 CUSTOM CUSTOMS ###


import helper.helper as helper


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
    # print title
    helper.print_title("2020", "6", "Custom Customs")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day06/pi.txt", 0)

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
    helper.print_question_answer(
        "What is the sum of those counts? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input_p2)
    helper.print_question_answer(
        "What is the sum of those counts? ", answer,
    )


if __name__ == "__main__":
    main()
