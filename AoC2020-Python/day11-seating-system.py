### ADVENT OF CODE 2020 DAY 11 SEATING SYSTEM ###


import helper.helper as helper
import numpy as np
from scipy.ndimage import convolve


## * puzzle part 1
def puzzle_part_1(seat_grid):

    # setup convolve kernel for adjacent seats
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    # copy of seat grid for current iteration
    current_seats = np.copy(seat_grid)

    # loop through until there are no changes to seats
    while True:
        # copy of current seat grid to compare against and break loop
        previous_seats = np.copy(current_seats)

        # convolve current seat grid using kernel
        convolved_seats = convolve(
            np.where(current_seats == 2, 1, 0), kernel, mode="constant"
        )

        # apply seating rules
        current_seats[(current_seats == 1) & (convolved_seats == 0)] = 2
        current_seats[(current_seats == 2) & (convolved_seats >= 4)] = 1

        # check to see if we need to break loop
        if (previous_seats == current_seats).all():
            break

    # return count of occupied seats
    return np.count_nonzero(current_seats == 2)


## * puzzle part 2
def puzzle_part_2(seat_grid):

    # setup list of every direction
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # np array of coordinates
    neighbors = np.array(
        [
            [
                [closest_seat_coord((x, y), d, seat_grid) for d in directions]
                for y, c in enumerate(r)
            ]
            for x, r in enumerate(seat_grid)
        ]
    )
    neighbors = np.rollaxis(neighbors + 1, -1)
    padded_seats = np.zeros((seat_grid.shape[0] + 2, seat_grid.shape[1] + 2))

    # loop through until there are no changes to seats
    while True:
        # copy of seat grid to compare against and break loop
        previous_seats = np.copy(seat_grid)

        padded_seats[1:-1, 1:-1] = seat_grid
        neighbor_vals = np.take(
            padded_seats, np.ravel_multi_index(neighbors, padded_seats.shape)
        )
        res = np.sum(neighbor_vals == 2, axis=2)

        # apply seating rules
        seat_grid[(seat_grid == 1) & (res == 0)] = 2
        seat_grid[(seat_grid == 2) & (res >= 5)] = 1

        # check to see if we need to break loop
        if (previous_seats == seat_grid).all():
            break

    # return count of occupied seats
    return np.count_nonzero(seat_grid == 2)


## * find closest seat coordinates
def closest_seat_coord(coord, offset, seat_grid):
    # setup location
    current_location = (coord[0] + offset[0], coord[1] + offset[1])

    # loop through locations making sure current location is in boundaries
    while (
        0 <= current_location[0] < len(seat_grid)
        and 0 <= current_location[1] < len(seat_grid[current_location[0]])
        and seat_grid[current_location] == 0
    ):

        current_location = (
            current_location[0] + offset[0],
            current_location[1] + offset[1],
        )

    return current_location


## * main function
def main():
    # print title
    helper.print_title("2020", "11", "Seating System")

    # get puzzle input
    puzzle_input = helper.load_puzzle_input("inputs/day11/pi.txt")

    # setup np array
    # use translation mask to convert characters to numerics
    translation_mask = str.maketrans(".L#", "012")
    seat_grid = np.array(
        [[int(x) for x in list(r.translate(translation_mask))] for r in puzzle_input]
    )

    # solve part 1 and print QA
    answer = puzzle_part_1(seat_grid)
    helper.print_question_answer(
        "How many seats end up occupied? ", answer,
    )

    # solve part 2 and print QA
    answer = puzzle_part_2(seat_grid)
    helper.print_question_answer(
        "Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied? ",
        answer,
    )


if __name__ == "__main__":
    main()
