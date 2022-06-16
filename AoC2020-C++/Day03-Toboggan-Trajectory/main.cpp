// * ADVENT OF CODE 2020 - DAY 3 - TOBOGGAN TRAJECTORY *

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

// function to find trees you would hit on given right and down values
int findTrees(std::vector<std::string> hillVector, int right, int down)
{
    // get width of one of the input lines since they are all the same width
    int hillWidth = hillVector[0].length() - 1; // remove one for the new line character

    // count trees starting at the top left of the hill using given right and down
    int startPosition = 0;
    int trees = 0;
    for (std::size_t i = 0; i < hillVector.size(); i = i + down)
    {
        std::string hillLine = hillVector[i];
        if (hillLine[startPosition % hillWidth] == '#')
        {
            trees++;
        }
        startPosition = startPosition + right;
    }

    return trees;
}

int main()
{
    // setup for title
    const std::string TITLEYEAR = "2020";
    const std::string TITLEDAY = "3";
    const std::string TITLENAME = "Toboggan Trajectory";

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
    int answer = findTrees(puzzleVector, 3, 1);

    // print question and answer
    std::cout << COLOR_QUESTION << "\nStarting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << answer << COLOR_CLEAR << std::endl;

    // * puzzle part 2
    int slope1 = findTrees(puzzleVector, 1, 1);
    int slope2 = findTrees(puzzleVector, 3, 1);
    int slope3 = findTrees(puzzleVector, 5, 1);
    int slope4 = findTrees(puzzleVector, 7, 1);
    int slope5 = findTrees(puzzleVector, 1, 2);

    answer = slope1 * slope2 * slope3 * slope4 * slope5;

    // print question and answer
    std::cout << COLOR_QUESTION << "\nWhat do you get if you multiply together the number of trees encountered on each of the listed slopes? " << COLOR_CLEAR;
    std::cout << COLOR_ANSWER << answer << "\n"
              << COLOR_CLEAR << std::endl;

    return 0;
}