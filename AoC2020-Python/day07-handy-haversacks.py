### ADVENT OF CODE 2020 DAY 7 HANDY HAVERSACKS ###


import helper.helper as helper


## * puzzle part 1
def puzzle_part_1(puzzle_input, bag_set, target_bag):
    # loop through all of the bag rules and split out the primary bag from the secondary bags
    # then check if the target bag is contained in the secondary bag list, if so, add to the bag set and recurse
    for element in puzzle_input:
        primary_bag, secondary_bags = element.split("contain ")
        primary_bag = primary_bag.split(" bags")[0]
        if target_bag in secondary_bags:
            bag_set.add(primary_bag)
            puzzle_part_1(puzzle_input, bag_set, primary_bag)

    return bag_set


## * puzzle part 2
def puzzle_part_2(puzzle_input, target_bag):
    # loop through all of the bag rules and split out the primary bag from the secondary bags
    bag_count = 0
    for element in puzzle_input:
        primary_bag, secondary_bags = element.split("contain ")
        primary_bag = primary_bag.split(" bags")[0]
        # check if the target bag is the primary bag and has secondary bags, if so, convert to list
        if target_bag == primary_bag and "no other bags" not in secondary_bags:
            secondary_bags_list = secondary_bags.split(", ")
            for bag in secondary_bags_list:
                # split out only the first word, which is the number of bags
                secondary_count = int(bag.split(" ")[0])
                # add the secondary_count found to the total bag_count
                bag_count += secondary_count
                # split out the secondary bag colors
                bag_color = bag.split(" bag")[0][2:]
                # recurse to find nested bags and add to bag_count
                bag_count += secondary_count * puzzle_part_2(puzzle_input, bag_color)

    return bag_count


## * main function
def main():
    # print title
    helper.print_title("2020", "7", "Handy Haversacks")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day07/pi.txt")

    # solve part 1 and print QA
    possible_bags = set()
    possible_bags = puzzle_part_1(puzzle_input, possible_bags, "shiny gold")
    answer = len(possible_bags)
    helper.print_question_answer(
        "How many bag colors can eventually contain at least one shiny gold bag? ",
        answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(puzzle_input, "shiny gold")
    helper.print_question_answer(
        "How many individual bags are required inside your single shiny gold bag? ",
        answer,
    )


if __name__ == "__main__":
    main()
