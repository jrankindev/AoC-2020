// * ADVENT OF CODE 2020 - DAY 2 - PASSWORD PHILOSOPHY *

#include "helper/helper.h"

// * puzzle part 1 function
int puzzlePart1(std::vector<std::string> puzzleVector) {
    // loop through each line and split out policy rules from password
    // then check if password is correct and if so, add it to correctCount
    int correctCount = 0;
    for (auto line : puzzleVector) {
        // split out password rules and password from string using string manip
        int lineLength = line.length();

        // split out password
        std::string password = line.substr(line.find(':') + 2, lineLength);

        // split out rule letter
        std::string ruleLetter = line.substr(line.find(':') - 1, 1);
        char ruleLetterChar = ruleLetter[0];

        // split out min and max uses
        int minUses = stoi(line.substr(0, line.find('-')));
        std::string maxCut = line.erase(0, line.find('-') + 1);
        int maxUses = stoi(maxCut.erase(maxCut.find(' '), maxCut.length()));

        // count occurences of ruleLetter in password and compare it to min and max rules
        int ruleLetterOccurences = 0;
        for (unsigned int i = 0; i < password.size(); i++) {
            if (password[i] == ruleLetterChar) {
                ruleLetterOccurences++;
            }
        }
        if (ruleLetterOccurences >= minUses && ruleLetterOccurences <= maxUses) {
            correctCount++;
        }
    }

    return correctCount;
}

// * puzzle part 2 function
int puzzlePart2(std::vector<std::string> puzzleVector) {
    // loop through each line and split out new policy rules from password
    // check if password is correct and if so, add it to correctCount
    int correctCount = 0;
    for (auto line : puzzleVector) {
        // split out password rules and password from string using string manip
        int lineLength = line.length();

        // split out password
        std::string password = line.substr(line.find(':') + 2, lineLength);

        // split out rule letter
        std::string ruleLetter = line.substr(line.find(':') - 1, 1);
        char ruleLetterChar = ruleLetter[0];

        // split out min and max uses
        int firstPosition = stoi(line.substr(0, line.find('-')));
        std::string maxCut = line.erase(0, line.find('-') + 1);
        int secondPosition = stoi(maxCut.erase(maxCut.find(' '), maxCut.length()));

        // check ruleLetterChar positions against new rules
        if ((password[firstPosition - 1] == ruleLetterChar && password[secondPosition - 1] != ruleLetterChar) || (password[firstPosition - 1] != ruleLetterChar && password[secondPosition - 1] == ruleLetterChar)) {
            correctCount++;
        }
    }

    return correctCount;
}

int main() {
    // print title
    helper::printTitle("2020", "2", "Passport Philosophy");

    // load puzzle input
    std::vector<std::string> puzzleVector = helper::loadPuzzleInputString("inputs/day02/pi.txt");

    // solve part 1
    int answer = puzzlePart1(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("\nHow many passwords are valid according to their policies? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("How many passwords are valid according to the new interpretation of the policies? ", std::to_string(answer));

    return 0;
}