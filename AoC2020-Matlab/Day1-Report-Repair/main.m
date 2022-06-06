% * ADVENT OF CODE 2020 - DAY 1 - REPORT REPAIR *


% * ------------ PRE-PUZZLE CODE ------------ *

% clear screen for readability and cleanup vars/figures
clear all;
close all;
clc;

%function to make colored messages in terminal
function cMsg(msg, type)
    if (type == 1)
        fprintf(1, [char(27), '[94m' msg, char(27), '[0m\n']);
    elseif (type == 2)
        fprintf(1, [char(27), '[95m' msg, char(27), '[0m\n']);
    elseif (type == 3)
        fprintf(1, [char(27), '[92m' msg, char(27), '[0m\n']);
    else
        error('BAD TYPE');
    endif
endfunction

% write title and day
% fprintf('Score=%d\n', userInput);
cMsg(' Advent of Code 2020', 1)
cMsg(' Day 1 - Report Repair\n\n', 1)

%get puzzle input
inputFile = 'pi.txt';
puzzleInput = dlmread (inputFile, '\n');


% * ------------ PUZZLE PART 1 ------------ *

% loop through puzzle input finding entries that sum to 2020
% for every match found, add it to answerVector
answerVector = [];
for i = 1:length(puzzleInput)
    searcher = 2020 - puzzleInput(i);
    [booleanMatches] = ismember (searcher, puzzleInput);
    if (booleanMatches == 1)
        answerVector = horzcat(answerVector, [puzzleInput(i)]);
    endif
endfor

% calculate answer
answer = answerVector(1) * answerVector(2);

% write question and answer for part 1
cMsg('-> Question:', 2)
cMsg('-> Find the two entries that sum to 2020; what do you get if you multiply them together?', 2);
cMsg('-> Answer:', 3)
fprintf('-> %d\n\n', answer);


% * ------------ PUZZLE PART 2 ------------ *

% loop through puzzle input twice finding two entries that sum to 2020
% for every match found, add it to answerVector
answerVector = [];
for i = 1:length(puzzleInput)
    for x = 1:length(puzzleInput)
        searcher = 2020 - (puzzleInput(i) + puzzleInput(x));
        [booleanMatches] = ismember (searcher, puzzleInput);
        if (booleanMatches == 1)
            answerVector = horzcat(answerVector, [puzzleInput(i)]);
        endif
    endfor
endfor

% since we had to use two loops, we have duplicates
% get the unique values only
answerVector = unique(answerVector);

% calculate answer
answer = answerVector(1) * answerVector(2) * answerVector(3);

% write question and answer for part 2
cMsg('-> Question:', 2)
cMsg('-> In your expense report, what is the product of the three entries that sum to 2020?', 2);
cMsg('-> Answer:', 3)
fprintf('-> %d\n\n', answer);