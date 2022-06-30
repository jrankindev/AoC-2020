// * ADVENT OF CODE 2020 - DAY 3 - TOBOGGAN TRAJECTORY *

#include "helper/helper.h"

// function to find trees you would hit on given right and down values
int findTrees(std::vector<std::string> hillVector, int right, int down) {
    // get width of one of the input lines since they are all the same width
    int hillWidth = hillVector[0].length() - 1;  // remove one for the new line character

    // count trees starting at the top left of the hill using given right and down
    int startPosition = 0;
    int trees = 0;
    for (std::size_t i = 0; i < hillVector.size(); i = i + down) {
        std::string hillLine = hillVector[i];
        if (hillLine[startPosition % hillWidth] == '#') {
            trees++;
        }
        startPosition = startPosition + right;
    }

    return trees;
}

int main() {
    // print title
    helper::printTitle("2020", "3", "Toboggan Trajectory");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputString("inputs/day03/pi.txt");

    // solve part 1
    int answer = findTrees(puzzleVector, 3, 1);

    // print question and answer
    helper::printQuestionAnswer("\nStarting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? ", std::to_string(answer));

    // solve part 2
    int slope1 = findTrees(puzzleVector, 1, 1);
    int slope2 = findTrees(puzzleVector, 3, 1);
    int slope3 = findTrees(puzzleVector, 5, 1);
    int slope4 = findTrees(puzzleVector, 7, 1);
    int slope5 = findTrees(puzzleVector, 1, 2);

    answer = slope1 * slope2 * slope3 * slope4 * slope5;

    // print question and answer
    helper::printQuestionAnswer("What do you get if you multiply together the number of trees encountered on each of the listed slopes? ", std::to_string(answer));

    return 0;
}