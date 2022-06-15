// * ADVENT OF CODE 2020 - DAY 1 - REPORT REPAIR *

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // setup for title
    const char TITLEYEAR[] = "2020";
    const char TITLEDAY[] = "1";
    const char TITLENAME[] = "Report Repair";

    // setup for colors
    const char COLOR_TITLE[] = "\033[1;95m";
    const char COLOR_QUESTION[] = "\033[1;34m";
    const char COLOR_ANSWER[] = "\033[1;32m";
    const char COLOR_CLEAR[] = "\033[0m";

    // clear screen
    system("clear");

    // print title
    printf("%s\n     Advent of Code %s\n     Day %s - %s\n\n%s", COLOR_TITLE,
           TITLEYEAR, TITLEDAY, TITLENAME, COLOR_CLEAR);

    // puzzle file to open
    char puzzleInput[] = "pi.txt";

    // open file and store in array
    // first find number of lines in file, then create the array, then store the line data
    FILE *filePointer;
    char lineData[50];
    int fileLineCount = 0;

    filePointer = fopen(puzzleInput, "r");

    if (filePointer == NULL)
    {
        printf("ERROR: File failed to open.\n\n");
        return 0;
    }
    else
    {
        // count number of lines in file
        for (char c = getc(filePointer); c != EOF; c = getc(filePointer))
        {
            if (c == '\n')
            {
                fileLineCount++;
            }
        }
        fileLineCount++; // needed to catch all lines
    }

    // create array now that we have total line value
    int puzzleInputArr[fileLineCount];

    // store data from file in array
    rewind(filePointer);
    for (int i = 0; i < fileLineCount; i++)
    {
        puzzleInputArr[i] = atoi(fgets(lineData, 50, filePointer));
    }

    // close file
    fclose(filePointer);

    // * puzzle part 1
    // loop through puzzle input finding entries that match 2020 - entry
    int entries[2];
    int entriesArrayPos = 0;
    for (int i = 0; i < fileLineCount; i++)
    {
        int searcher = 2020 - puzzleInputArr[i];
        for (int x = 0; x < fileLineCount; x++)
        {
            if (puzzleInputArr[x] == searcher)
            {
                entries[entriesArrayPos] = puzzleInputArr[i];
                entriesArrayPos++;
            }
        }
    }

    // calc answer
    int answer = entries[0] * entries[1];

    // print question and answer
    printf(
        "%s\nFind the two entries that sum to 2020; what do you get if you "
        "multiply them together? %s%d\n%s",
        COLOR_QUESTION, COLOR_ANSWER, answer, COLOR_CLEAR);

    // * puzzle part 2
    // loop through puzzle input twice on different numbers finding entries that
    // match 2020 for both entries
    int entries2[3];
    for (int i = 0; i < fileLineCount; i++)
    {
        for (int x = 0; x < fileLineCount; x++)
        {
            int elementSum = puzzleInputArr[i] + puzzleInputArr[x];
            int searcher = 2020 - elementSum;
            for (int n = 0; n < fileLineCount; n++)
            {
                if (puzzleInputArr[n] == searcher)
                {
                    entries2[0] = puzzleInputArr[i];
                    entries2[1] = puzzleInputArr[x];
                    entries2[2] = searcher;
                }
            }
        }
    }

    // calc answer
    answer = entries2[0] * entries2[1] * entries2[2];

    // print question and answer
    printf(
        "\n%sIn your expense report, what is the product of the three entries "
        "that sum to 2020? %s%d\n\n%s",
        COLOR_QUESTION, COLOR_ANSWER, answer, COLOR_CLEAR);

    return 0;
}