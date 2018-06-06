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

# Returns -1 if word one is earlier in alphabet or line than word2
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
    # Return None if there is no next word
    indexLowestword = [None,None]

    for lineIndex, line in enumerate(lines2BIndexed):
        for wordIndex, word in enumerate(line):
            if word not in excludedWords :
                # If we are reading this in the first time
                if (indexLowestword[0] == None or (compareTo(lineIndex, wordIndex, indexLowestword[0], indexLowestword[1]) < 0)):
                    # If there is no previous word
                    if (lineIndexPrevWord == None ) or (compareTo(lineIndex, wordIndex, lineIndexPrevWord, wordIndexPrevWord) > 0):
                        indexLowestword = [lineIndex, wordIndex]

    return indexLowestword

def splitLineIntoTriple(indexOfLine, indexOfWord):
    '''Given a word this fills a tuple with prefix, and postfix'''
    returnTriple = [ (' '.join([x for x in lines2BIndexed[indexOfLine][:indexOfWord]  ])),
                     lines2BIndexed[indexOfLine][indexOfWord],
                      (' '.join([x for x in lines2BIndexed[indexOfLine][(indexOfWord+1):] ]))
                      ]
    # Cut off the prefix word that overflows
    if ( len(returnTriple[0])>19 and returnTriple[0][-19] != " " and returnTriple[0][-20] != " " ):
        while len(returnTriple[0])>19:
            returnTriple[0] = returnTriple[0].split(' ',1)[1]

    # Cut off the postfix word that overflows
    lenWord = len(returnTriple[1])
    if ( (len(returnTriple[2])+ lenWord > 31) and returnTriple[2][30-lenWord] != ' '
         and returnTriple[2][31-lenWord] != ' '   ):
        while len(returnTriple[2])+lenWord > 29 :
            returnTriple[2] = returnTriple[2].rsplit(' ',1)[0]

    return returnTriple

def printFormattedTriple(triple):
    '''This will print the tripple in the correct format.'''
    lengthLeft = len(triple[0])
    lengthIndexWord = len(triple[1])
    lengthRight=len(triple[2])
    # Create a string of 9 white spaces
    returnString = " "*9
    if (lengthLeft <= 19) :
        returnString = ''.join([returnString," "*(19-lengthLeft),triple[0], " ", triple[1].upper()])
    else:
        returnString = ''.join([returnString, triple[0][-19:]," ", triple[1].upper()])

    #the last collum cannot go past 60
    if (lengthRight <= (29 - lengthIndexWord)) and (lengthRight>0) :
        returnString = " ".join([returnString, triple[2]])
    else:
        returnString = " ".join([returnString, triple[2][:(29-lengthIndexWord)]])
    # print("\nThe string is:",returnString)
    return returnString.rstrip()





def main():
    readInFile()
    nextWordToBeIndexed = getLowestNonIndexedWord(None,None)
    while nextWordToBeIndexed[0] != None :
        print(printFormattedTriple(splitLineIntoTriple(nextWordToBeIndexed[0],nextWordToBeIndexed[1])))
        # print(printFormattedLine(nextWordToBeIndexed[0],nextWordToBeIndexed[1]))

        nextWordToBeIndexed = getLowestNonIndexedWord(nextWordToBeIndexed[0],nextWordToBeIndexed[1])


#     Steps to do
#DONE       read the lines of text into some arrays
#DONE       tokenise the stings
#DONR       find the lowest non indexed word
#       save that line with the word capitalized
#       format the line properly
#       print the final output


if __name__ == '__main__':
    main()