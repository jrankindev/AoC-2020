// * ADVENT OF CODE 2020 - DAY 4 - PASSPORT PROCESSING *

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

int main()
{
    // setup for title
    const std::string TITLEYEAR = "2020";
    const std::string TITLEDAY = "4";
    const std::string TITLENAME = "Passport Processing";

    // setup for colors
    const std::string COLOR_TITLE = "\033[1;95m";
    const std::string COLOR_QUESTION = "\033[1;34m";
    const std::string COLOR_ANSWER = "\033[1;32m";
    const std::string COLOR_CLEAR = "\033[0m";

    // puzzle file
    const std::string PUZZLE_INPUT = "pie.txt";

    // clear screen for readability
    system("clear");

    // print title
    std::cout << COLOR_TITLE << "\n     Advent of Code " << TITLEYEAR << std::endl;
    std::cout << "     Day " << TITLEDAY << " - " << TITLENAME << COLOR_CLEAR << std::endl;

    // open puzzle file and store lines in vector
    std::vector<std::string> puzzleVector;
    std::string passport;
    std::ifstream file(PUZZLE_INPUT);
    if (file.is_open())
    {
        std::string line;
        while (getline(file, line))
        {
            if (line.empty()) // !!!!! this isn't working right
            {
                puzzleVector.push_back(passport);
                passport = "";
                continue;
            }
            if (line != "\r")
            {
                passport = line + " " + passport;
            }
        }
    }

    file.close();

    // * puzzle part 1
    for (auto line : puzzleVector)
    {
        std::cout << "-> " << line << std::endl;
    }

    // print question and answer
    std::cout << COLOR_QUESTION << "\nIn your batch file, how many passports are valid? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << 0 << COLOR_CLEAR << std::endl;

    // * puzzle part 2

    // print question and answer
    std::cout << COLOR_QUESTION << "\nIn your batch file, how many passports are valid? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << 0 << "\n"
              << COLOR_CLEAR << std::endl;

    return 0;
}