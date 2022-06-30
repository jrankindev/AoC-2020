// * ADVENT OF CODE 2020 - DAY 1 - REPORT REPAIR *

#include <algorithm>

#include "helper/helper.h"

// * puzzle part 1 function
int puzzlePart1(std::vector<int> puzzleVector) {
    // loop through puzzle input finding entries that match 2020 - entry
    std::vector<int> entries;
    for (int element : puzzleVector) {
        int searcher = 2020 - element;
        if (find(puzzleVector.begin(), puzzleVector.end(), searcher) != puzzleVector.end()) {
            entries.push_back(element);
        }
    }

    // calc answer
    int answer = entries[0] * entries[1];

    return answer;
}

// * puzzle part 2 function
int puzzlePart2(std::vector<int> puzzleVector) {
    // loop through puzzle input twice on different numbers finding entries that
    // match 2020 for both entries
    std::vector<int> entries;
    for (int element : puzzleVector) {
        for (int innerElement : puzzleVector) {
            if (element != innerElement) {
                int elementSum = element + innerElement;
                int searcher = 2020 - elementSum;
                if (find(puzzleVector.begin(), puzzleVector.end(), searcher) != puzzleVector.end() && find(puzzleVector.begin(), puzzleVector.end(), innerElement) != puzzleVector.end()) {
                    entries.push_back(element);
                    entries.push_back(innerElement);
                    entries.push_back(searcher);
                }
            }
        }
    }

    // calc answer
    int answer = entries[0] * entries[1] * entries[2];

    return answer;
}

// * main function
int main() {
    // print title
    helper::printTitle("2020", "1", "Report Repair");

    // load puzzle input
    std::vector<int> puzzleVector = helper::loadPuzzleInputVec("inputs/day01/pi.txt");

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nFind the two entries that sum to 2020; what do you get if you multiply them together? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("In your expense report, what is the product of the three entries that sum to 2020? ", std::to_string(answer));

    return 0;
}