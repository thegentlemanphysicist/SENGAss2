#!/usr/bin/env python3

import fileinput
import sys



excludedWords = []
lines2BIndexed = []

def readInFile():
    '''This iputs the file into the exclusion word array and 
    to be indexed array.'''
    caseNumber = 0
    for line in fileinput.input():
        # print(line)
        # print(caseNumber)
        if line.rstrip() =="::":
            caseNumber+=1
        else :
            if caseNumber==1:
                #Fill the list with excluded words
                excludedWords.append(line.rstrip())

            if caseNumber==2:
                #Fill the list of lines to be indexed
                lines2BIndexed.append(line.rstrip().split())

def compareTo(line1, word1, line2, word2):
    '''Compares two words first by lexographical order, then by line number, then by position in a line'''
    firstWord = lines2BIndexed[line1][word1]
    secondWord = lines2BIndexed[line2][word2]
    returnInt = 0
    if firstWord < secondWord:
        returnInt = -1
    elif firstWord > secondWord:
        returnInt = +1
    elif line1 < line2:
        returnInt = -1
    elif line1 > line2:
        returnInt = +1
    elif word1 < word2:
        returnInt = -1
    elif word1 > word2:
        returnInt = +1

    return returnInt



def getLowestNonIndexedWord(lineIndexPrevWord, wordIndexPrevWord):
    '''Return the next non indexed word that isn't excluded'''
    indexLowestword = [lineIndexPrevWord,wordIndexPrevWord]
    for lineIndex, line in enumerate(lines2BIndexed):
        for wordIndex, word in enumerate(line):
            if word not in excludedWords :
                if lines2BIndexed == -1:
                    #The first element is being read in
                    indexLowestword = [lineIndex,wordIndex]
                elif ( compareTo(lineIndex, wordIndex, lineIndexPrevWord, wordIndexPrevWord) < 0):
                    indexLowestword = [lineIndex, wordIndex]
    return  indexLowestword




def main():
    readInFile()
#     Steps to do
#DONE       read the lines of text into some arrays
#DONE       tokenise the stings
#       find the lowest non indexed word
#       save that line with the word capitalized
#       format the line properly
#       print the final output


if __name__ == '__main__':
    main()