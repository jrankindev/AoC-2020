### ADVENT OF CODE 2020 DAY 10 ADAPTER ARRAY ###


import helper.helper as helper
from collections import Counter

## * puzzle part 1
def puzzle_part_1(puzzle_input):
    # create a new list of sorted adapters from puzzle input
    sorted_adapters = sorted(puzzle_input)

    # setup the adapter range
    # needs to start at 0 and end at the largest value in the list + 3
    device_jolt_needs = max(sorted_adapters) + 3
    adapter_range = [0] + sorted_adapters + [device_jolt_needs]

    # calculate subtraction from previous adapter in range to currrent adapter in range
    # store in a list
    jolt_differences = [
        adapter_range[i] - adapter_range[i - 1] for i in range(1, len(adapter_range))
    ]

    # use Counter to find total value of each 1 or 3 jolt change
    jolt_differences_dict = dict(Counter(jolt_differences))

    answer = jolt_differences_dict[1] * jolt_differences_dict[3]
    return answer


## * puzzle part 2
def puzzle_part_2(puzzle_input):
    # create a new list of sorted adapters from puzzle input
    sorted_adapters = sorted(puzzle_input)

    # add device jolt requirements to end of adapter list
    device_jolt_needs = max(sorted_adapters) + 3
    sorted_adapters.append(device_jolt_needs)

    # create a dictionary to count how many ways to reach each adapter
    # key 0 can only be reached 1 way, so start with that
    adapter_counter = {0: 1}

    # loop through each adapter list and check if previous 1-3 adapters are in counter dictionary
    # if so, set possible way to that specific value, if not, defaults to 0
    for adapter in sorted_adapters:
        possible_way1 = adapter_counter.get(adapter - 3, 0)
        possible_way2 = adapter_counter.get(adapter - 2, 0)
        possible_way3 = adapter_counter.get(adapter - 1, 0)

        # add up all possible ways
        total_ways = possible_way1 + possible_way2 + possible_way3

        # add total ways to that specific adapter in the dictionary
        adapter_counter[adapter] = total_ways

    # answer is the total count for the final adapter (device jolt needs)
    answer = adapter_counter[sorted_adapters[-1]]
    return answer


## * main function
def main():
    # print title
    helper.print_title("2020", "10", "Adapter Array")

    # get puzzle input
    # list of ints
    puzzle_input = helper.load_puzzle_input("inputs/day10/pi.txt", 1, 0)

    # solve part 1 and print QA
    answer = puzzle_part_1(puzzle_input)
    helper.print_question_answer(
        "What is the number of 1-jolt differences multiplied by the number of 3-jolt differences? ",
        answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input)
    helper.print_question_answer(
        "What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device? ",
        answer,
    )


if __name__ == "__main__":
    main()
