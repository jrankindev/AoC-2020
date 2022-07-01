// * ADVENT OF CODE 2020 - DAY 6 - CUSTOM CUSTOMS *

#include <regex>

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
    helper::printTitle("2020", "6", "Custom Customs");

    // load puzzle input
    std::string puzzleString = helper::loadPuzzleInputString("inputs/day06/pie.txt");

    // remove all blank lines and put passport fields all on a single line
    puzzleString = std::regex_replace(puzzleString, std::regex("\r\n"), " ");
    puzzleString = std::regex_replace(puzzleString, std::regex("  "), "\n");

    // convert string into a string vector, delimitted on new line
    std::vector<std::string> puzzleVector;
    std::string line;
    std::stringstream stream(puzzleString);
    while (getline(stream, line, '\n')) {
        puzzleVector.push_back(line);
    }

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nWhat is the sum of those counts? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("What is the sum of those counts? ", std::to_string(answer));

    return 0;
}