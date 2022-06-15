// * ADVENT OF CODE 2020 - DAY 2 - PASSWORD PHILOSOPHY *

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

int main()
{
    // setup for title
    const std::string TITLEYEAR = "2020";
    const std::string TITLEDAY = "2";
    const std::string TITLENAME = "Password Philosophy";

    // setup for colors
    const std::string COLOR_TITLE = "\033[1;95m";
    const std::string COLOR_QUESTION = "\033[1;34m";
    const std::string COLOR_ANSWER = "\033[1;32m";
    const std::string COLOR_CLEAR = "\033[0m";

    // puzzle file
    const std::string PUZZLE_INPUT = "pi.txt";

    // clear screen for readability
    system("clear");

    // print title
    std::cout << COLOR_TITLE << "\n     Advent of Code " << TITLEYEAR << std::endl;
    std::cout << "     Day " << TITLEDAY << " - " << TITLENAME << COLOR_CLEAR << std::endl;

    // open puzzle file and store lines in vector
    std::vector<std::string> puzzleVector;
    std::ifstream file(PUZZLE_INPUT);
    if (file.is_open())
    {
        std::string line;
        while (getline(file, line))
            puzzleVector.push_back(line);
    }
    file.close();

    // * puzzle part 1
    // loop through each line and split out policy rules from password
    // then check if password is correct and if so, add it to correctCount
    int correctCount = 0;
    for (auto line : puzzleVector)
    {
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
        for (unsigned int i = 0; i < password.size(); i++)
        {
            if (password[i] == ruleLetterChar)
            {
                ruleLetterOccurences++;
            }
        }
        if (ruleLetterOccurences >= minUses && ruleLetterOccurences <= maxUses)
        {
            correctCount++;
        }
    }

    // print question and answer
    std::cout << COLOR_QUESTION << "\nHow many passwords are valid according to their policies? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << correctCount << COLOR_CLEAR << std::endl;

    // * puzzle part 2
    // loop through each line and split out new policy rules from password
    // check if password is correct and if so, add it to correctCount
    correctCount = 0;
    for (auto line : puzzleVector)
    {
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
        if ((password[firstPosition - 1] == ruleLetterChar && password[secondPosition - 1] != ruleLetterChar) || (password[firstPosition - 1] != ruleLetterChar && password[secondPosition - 1] == ruleLetterChar))
        {
            correctCount++;
        }
    }

    // print question and answer
    std::cout << COLOR_QUESTION << "\nHow many passwords are valid according to the new interpretation of the policies? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << correctCount << "\n"
              << COLOR_CLEAR << std::endl;

    return 0;
}