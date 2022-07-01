// * ADVENT OF CODE 2020 - DAY 6 - CUSTOM CUSTOMS *

#include <bits/stdc++.h>

#include <regex>

#include "helper/helper.h"

// * puzzle part 1 function
int puzzlePart1(std::vector<std::string> puzzleVector) {
    // declare unordered set to track questions for each group
    std::unordered_set<char> questionSet;

    // variable to track the total answered questions for all groups
    int totalAnswers = 0;

    // loop through each group
    for (auto line : puzzleVector) {
        // loop through each answer in the gruop
        for (auto character : line) {
            // if not a blank character, then insert character into set
            if (character != ' ') {
                questionSet.insert(character);
            }
        }

        // add the size of the set to total answers and then clear the set for next group
        totalAnswers += questionSet.size();
        questionSet.clear();
    }

    // return total questions answered
    return totalAnswers;
}

// * puzzle part 2 function
int puzzlePart2(std::vector<std::string> puzzleVector) {
    // declare unordered set to track questions for each group
    std::unordered_set<char> questionSet;

    // variable to track the total answered questions for the group
    int totalAnswers = 0;

    // loop through each group
    for (auto line : puzzleVector) {
        // total number of people in the group
        size_t groupCount = std::count(line.begin(), line.end(), ' ') + 1;

        // loop through each answer in the group
        for (auto character : line) {
            // if not a blank character, then insert character into set
            if (character != ' ') {
                questionSet.insert(character);
            }
        }

        // loop through each answered question in the set
        for (auto character : questionSet) {
            // total number of each question answered in the group
            size_t characterOccurences = std::count(line.begin(), line.end(), character);

            // if all members of the group answered yes then add one to total answers
            if (groupCount == characterOccurences) {
                totalAnswers++;
            }
        }

        // clear the set for the next group
        questionSet.clear();
    }

    // return total
    return totalAnswers;
}

// * main function
int main() {
    // print title
    helper::printTitle("2020", "6", "Custom Customs");

    // load puzzle input
    std::string puzzleString = helper::loadPuzzleInputString("inputs/day06/pi.txt");

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