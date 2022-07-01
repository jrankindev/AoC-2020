// * ADVENT OF CODE 2020 - DAY 5 - BINARY BOARDING *

#include <algorithm>

#include "helper/helper.h"

// * puzzle part 2 function
int puzzlePart2(std::vector<int> puzzleVector) {
    // seat tracking var
    int mySeat = 0;

    // loop through each element in vector
    for (unsigned long int i = 0; i < puzzleVector.size(); i++) {
        // check to see if the next element minus current element does not equal 1
        // if so, we have a missing value which should be our seat
        if ((puzzleVector[i + 1] - puzzleVector[i]) != 1) {
            mySeat = puzzleVector[i] + 1;
            break;
        }
    }

    // return answer
    return mySeat;
}

// * binary replace characters, convert to base 10, sort
std::vector<int> vecBinaryReplaceConvertSort(std::vector<std::string> puzzleVector) {
    // replace characters with binary equivalent
    for (unsigned long int i = 0; i < puzzleVector.size(); i++) {
        std::replace(puzzleVector[i].begin(), puzzleVector[i].end(), 'F', '0');
        std::replace(puzzleVector[i].begin(), puzzleVector[i].end(), 'B', '1');
        std::replace(puzzleVector[i].begin(), puzzleVector[i].end(), 'L', '0');
        std::replace(puzzleVector[i].begin(), puzzleVector[i].end(), 'R', '1');
    }

    // convert from string to base 2 (binary) int
    std::vector<int> puzzleVectorInt;
    for (auto line : puzzleVector) {
        puzzleVectorInt.push_back(std::stoi(line, nullptr, 2));
    }

    // sort to put largest seat id at end of list
    sort(puzzleVectorInt.begin(), puzzleVectorInt.end());

    // return new converted vector
    return puzzleVectorInt;
}

// * main function
int main() {
    // print title
    helper::printTitle("2020", "5", "Binary Boarding");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputStringVec("inputs/day05/pi.txt");

    // setup converted base 10 vector
    std::vector<int> puzzleVectorInt = vecBinaryReplaceConvertSort(puzzleVector);

    // solve part 1
    int answer = puzzleVectorInt.back();

    // print question and answer
    helper::printQuestionAnswer("\nWhat is the highest seat ID on a boarding pass? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVectorInt);

    // print question and answer
    helper::printQuestionAnswer("What is the ID of your seat? ", std::to_string(answer));

    return 0;
}