### ADVENT OF CODE 2020 DAY 8 HANDHELD HALTING ###


import os


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
    color_header = "\033[95m" + "\033[1m"
    color_clear = "\033[0m"
    print(f"{color_header} Advent of Code {year} ")
    print(f" Day {day} - {title} \n{color_clear}")


## * question and answer printer
def print_question_answer(question: str, answer: str):
    color_question = "\033[94m"
    color_answer = "\033[92m"
    color_clear = "\033[0m"
    print(
        f"{color_question}{question}",
        end="",
    )
    print(f"{color_answer} {str(answer)} \n {color_clear}")


## * puzzle part 1
def puzzle_part_1(puzzle_input):
    # first check to see if position is greater or equal to the puzzle input length
    # then check that position has not been seen before
    # then pull instruction and values from the current input line position
    # then run instruction
    global accumulator, previous_positions, position, loop_detected

    if position >= len(puzzle_input):
        loop_detected = False
    elif position not in previous_positions:
        previous_positions.add(position)
        input_line = puzzle_input[position]
        input_line = input_line.split()
        instruction = input_line[0]
        value = int(input_line[1])
        if instruction == "nop":
            nop()
            puzzle_part_1(puzzle_input)
        if instruction == "acc":
            acc(value)
            puzzle_part_1(puzzle_input)
        if instruction == "jmp":
            jmp(value)
            puzzle_part_1(puzzle_input)
    else:
        # loop was detected
        loop_detected = True


## * no operation instruction
def nop():
    global position
    position += 1


## * jump operation instruction
def jmp(value):
    global position
    position += value


## * accumulate operation instruction
def acc(value):
    global accumulator, position
    accumulator += value
    position += 1


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    global accumulator, previous_positions, position, loop_detected
    for i, input_line in enumerate(puzzle_input):

        # reset vars
        accumulator = 0
        previous_positions = set()
        position = 0
        loop_detected = False

        # copy puzzle for modification
        modified_puzzle_input = puzzle_input.copy()
        split_line = input_line.split()
        instruction = split_line[0]
        if instruction == "nop" or instruction == "jmp":
            swapped_instruction = swap_instruction(input_line)
            modified_puzzle_input[i] = swapped_instruction

        # run part 1 again
        puzzle_part_1(modified_puzzle_input)

        # if no loop detected, then return
        if loop_detected == False:
            return accumulator


## * function to swap corrupt instruction for puzzle part 2
def swap_instruction(input_line):
    input_line = input_line.split()
    instruction = input_line[0]
    if instruction == "nop":
        new_line = "jmp " + input_line[1]
    else:
        new_line = "nop " + input_line[1]

    return new_line


## * main function
def main():
    # clear screen for readability (check to see if windows - nt)
    os.system("cls" if os.name == "nt" else "clear")

    # print title
    print_title("2020", "8", "Handheld Halting")

    # get puzzle input
    puzzle_input = load_puzzle_input("pi.txt")

    # solve part 1 and print QA
    global accumulator, previous_positions, position, loop_detected
    accumulator = 0
    previous_positions = set()
    position = 0
    loop_detected = False
    puzzle_part_1(puzzle_input)
    print(loop_detected)
    print_question_answer(
        "Immediately before any instruction is executed a second time, what value is in the accumulator? ",
        accumulator,
    )

    # solve part 2 and print QA
    puzzle_part_2(puzzle_input)
    print_question_answer(
        "What is the value of the accumulator after the program terminates? ",
        accumulator,
    )


if __name__ == "__main__":
    main()
