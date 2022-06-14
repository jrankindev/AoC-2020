// * ADVENT OF CODE 2020 - DAY 1 - REPORT REPAIR *

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    // setup for title
    const string TITLEYEAR = "2020";
    const string TITLEDAY = "1";
    const string TITLENAME = "Report Repair";

    // setup for colors
    const string COLOR_TITLE = "\033[1;95m";
    const string COLOR_QUESTION = "\033[1;34m";
    const string COLOR_ANSWER = "\033[1;32m";
    const string COLOR_CLEAR = "\033[0m";

    // puzzle file
    const string PUZZLE_INPUT = "pi.txt";

    // clear screen for readability
    system("clear");

    // print title
    cout << COLOR_TITLE << "\n     Advent of Code " << TITLEYEAR;
    cout << "\n     Day " << TITLEDAY << " - " << TITLENAME << COLOR_CLEAR << "\n\n";

    // open puzzle file and store lines in vector
    vector<int> puzzleVector;
    ifstream file(PUZZLE_INPUT);
    if (file.is_open())
    {
        string line;
        while (getline(file, line))
            puzzleVector.push_back(stoi(line));
    }
    file.close();

    // * puzzle part 1
    // loop through puzzle input finding entries that match 2020 - entry
    vector<int> entries;
    for (int element : puzzleVector)
    {
        int searcher = 2020 - element;
        if (find(puzzleVector.begin(), puzzleVector.end(), searcher) != puzzleVector.end())
            entries.push_back(element);
    }

    // calc answer
    int answer = entries[0] * entries[1];

    // print question and answer
    cout << COLOR_QUESTION << "Find the two entries that sum to 2020; what do you get if you multiply them together? " << COLOR_CLEAR;
    cout << COLOR_ANSWER << answer << "\n\n"
         << COLOR_CLEAR;

    // * puzzle part 2
    // loop through puzzle input twice on different numbers finding entries that
    // match 2020 for both entries
    entries.clear();
    for (int element : puzzleVector)
    {
        for (int innerElement : puzzleVector)
        {
            if (element != innerElement)
            {
                int elementSum = element + innerElement;
                int searcher = 2020 - elementSum;
                if (find(puzzleVector.begin(), puzzleVector.end(), searcher) != puzzleVector.end() && find(puzzleVector.begin(), puzzleVector.end(), innerElement) != puzzleVector.end())
                {
                    entries.push_back(element);
                    entries.push_back(innerElement);
                    entries.push_back(searcher);
                }
            }
        }
    }

    // calc answer
    answer = entries[0] * entries[1] * entries[2];

    // print question and answer
    cout << COLOR_QUESTION << "In your expense report, what is the product of the three entries that sum to 2020? " << COLOR_CLEAR;
    cout << COLOR_ANSWER << answer << "\n\n"
         << COLOR_CLEAR;

    return 0;
}