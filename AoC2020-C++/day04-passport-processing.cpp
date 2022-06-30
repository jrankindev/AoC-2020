// * ADVENT OF CODE 2020 - DAY 4 - PASSPORT PROCESSING *

#include <regex>

#include "helper/helper.h"

// * puzzle part 1 function
int puzzlePart1(std::vector<std::string> puzzleVector) {
    // tracker for valid passports
    int validPassports = 0;

    // loop through each passport and check for a match of all required fields using regex
    // add one to validPassports if regex match is true
    for (auto passport : puzzleVector) {
        if (std::regex_match(passport, std::regex("^(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$"))) {
            validPassports++;
        }
    }

    // return total number of valid passports
    return validPassports;
}

// * puzzle part 2 function
int puzzlePart2(std::vector<std::string> puzzleVector) {
    // tracker for valid passports
    int validPassports = 0;

    // loop through each passport and check for all passport validation rules in regex
    // add one to validPassports if regex matches are true
    for (auto passport : puzzleVector) {
        if (std::regex_match(passport, std::regex(R"(.*(?=.*byr:(19[2-9][0-9]|200[0-2])\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*iyr:(201[0-9]|2020)\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*eyr:(202[0-9]|2030)\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*pid:\d{9}\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*hcl:#[\d|a-f]{6}\b).*)")) &&
            std::regex_match(passport, std::regex(R"(.*(?=.*hgt:((59|6\d|7[0-6])in|(1[5-8]\d|19[0-3])cm)\b).*)"))) {
            validPassports++;
        }
    }

    // return total number of valid passports
    return validPassports;
}

// * main function
int main() {
    // print title
    helper::printTitle("2020", "4", "Passport Processing");

    // load puzzle input
    std::string puzzleString = helper::loadPuzzleInputString("inputs/day04/pi.txt");

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
    helper::printQuestionAnswer("\nIn your batch file, how many passports are valid? ", std::to_string(answer));

    // solve part 2
    answer = puzzlePart2(puzzleVector);

    // print question and answer
    helper::printQuestionAnswer("In your batch file, how many passports are valid? ", std::to_string(answer));

    return 0;
}