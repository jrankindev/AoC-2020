### ADVENT OF CODE 2020 DAY 4 PASSPORT PROCESSING ###


import helper.helper as helper
import re


## * puzzle part 1
def puzzle_part_1(puzzle_input):
    # store all required fields in list
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # check each passport for required fields
    valid_passports = 0
    for passport in puzzle_input:
        if all(field in passport for field in required_fields):
            valid_passports += 1

    # return answer
    return valid_passports


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    # check each passport for validation in required fields using regex
    valid_passports = 0
    for passport in puzzle_input:
        if (
            re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport)
            and re.search(r"iyr:201\d|iyr:20[1-2]0", passport)
            and re.search(r"eyr:202\d|eyr:20[2-3]0", passport)
            and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport)
            and re.search(r"pid:\d{9}\b", passport)
            and re.search(r"hcl:#[A-Fa-f0-9]{6}", passport)
            and re.search(
                r"hgt:15\dcm|hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in",
                passport,
            )
        ):
            valid_passports += 1

    # return answer
    return valid_passports


## * main function
def main():
    # print title
    helper.print_title("2020", "4", "Passport Processing")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day04/pi.txt", 0, 1)

    # get rid of blank lines
    puzzle_input = puzzle_input.split("\n\n")

    # move passport info to single line
    puzzle_input = [line.replace("\n", " ") for line in puzzle_input]

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "In your batch file, how many passports are valid? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "In your batch file, how many passports are valid? ", answer,
    )


if __name__ == "__main__":
    main()
