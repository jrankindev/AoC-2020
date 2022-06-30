// * ADVENT OF CODE 2020 - DAY 4 - PASSPORT PROCESSING *

#include "helper/helper.h"

int main() {
    // print title
    helper::printTitle("2020", "4", "Passport Processing");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputString("inputs/day04/pie.txt");

    // TODO solve part 1
    for (auto line : puzzleVector) {
        std::cout << "-> " << line << std::endl;
    }

    // print question and answer
    helper::printQuestionAnswer("\nIn your batch file, how many passports are valid? ", std::to_string(0));

    // TODO solve part 2

    // print question and answer
    helper::printQuestionAnswer("\nIn your batch file, how many passports are valid? ", std::to_string(0));

    return 0;
}