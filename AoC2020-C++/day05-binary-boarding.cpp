// * ADVENT OF CODE 2020 - DAY 5 - BINARY BOARDING *

#include "helper/helper.h"

// * puzzle part 1 function
int puzzlePart1(std::vector<std::string> puzzleVector) {
    for (auto line : puzzleVector) {
        std::cout << line << std::endl;
    }
    return 0;
}

// * puzzle part 2 function
int puzzlePart2(std::vector<std::string> puzzleVector) {
    return 0;
}

// * main function
int main() {
    // print title
    helper::printTitle("2020", "5", "Binary Boarding");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputStringVec("inputs/day05/pie.txt");

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nIn your batch file, how many passports are valid? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("In your batch file, how many passports are valid? ", std::to_string(answer));

    return 0;
}