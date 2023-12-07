# Name: Group Krumrie (Alexander Fletcher, Andrew Etheridge, Evan Bleh, and Kirubel Teklemariam)
# email: fletchax@mail.uc.edu, etheriaw@mail.uc.edu, blehet@mail.uc.edu, and teklemka@mail.uc.edu
# Assignment Title: Final Project
# Due Date: Dec 7, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: PyDev project to use a json and text file to build a location sentence, then decrypt an encrypted movie title, then load a picture of our group at that location with sign that has a quote from that movie.
# Citations: NA
# Anything else that's relevant: NA

import json

def groupSentence(group, jsonFile, textFile):
    '''
    Read a json file and a text file, and return a sentence based on a list of line numbers that is the value to a specific key value in the json file pulling the words from the text file. 
    :param group: The key whose values to pull that contains the list of line numbers in the json file
    :param jsonFile: The json file that contains the dictionary of the groups and their corresponding list of line numbers to pull from the text file
    :param textFile: The text file that contains all the words that could be used to form the sentence
    :return The sentence OR [] on error
    '''
    #opens a given json file, and pulls a value from the given key (group), returns an empty list on error
    try:
        with open(jsonFile) as j:
            newData = json.load(j)
        groupKey = newData[group]
    except:
        return []
    
    #opens a given text file, or returns an empty list on error
    try:
        wordsFile = open(textFile, 'r')
        buffer = wordsFile.readline()
    except:
        return []
    
    #creates a list, wordsList, from the text file, removing any extra spaces from the words from the text file
    wordsList = []
    for w in wordsFile:
        cleanWords = w.strip()
        wordsList.append(cleanWords)
    
    #creates a sentence list pulling the correct words from the text file based on the values for the given key (group)
    sentence = []
    for numeral in groupKey:
        sentence.append((wordsList[int(numeral)-1]))
    
    #Capitalizes the first letter of the first item in the sentence list
    sentence[0] = sentence[0].capitalize()
    
    #returns the sentence list as an actual sentence
    sentenceString = " "
    return ("Place for our group picture is, \""+sentenceString.join(sentence)+"\".")