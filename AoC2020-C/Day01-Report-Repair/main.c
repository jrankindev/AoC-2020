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

    // print title in bold purple
    printf("%s\n     Advent of Code %s\n     Day %s - %s\n\n%s", COLOR_TITLE, TITLEYEAR, TITLEDAY, TITLENAME, COLOR_CLEAR);
    // printf("%s\nBlue Text\n\n%s", COLOR_QUESTION, COLOR_CLEAR);
    // printf("%s\nGreen Text\n\n%s", COLOR_ANSWER, COLOR_CLEAR);

    // puzzle file to open
    char puzzleInput[] = "pie.txt";

    return 0;
}