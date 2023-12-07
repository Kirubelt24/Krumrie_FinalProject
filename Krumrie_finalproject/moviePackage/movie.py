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
from cryptography.fernet import Fernet

def Movie(group, jsonFile, decryptKey):
    '''
    Read a json file and return an encrypted movie title based on the group's name, and then decrypts that tile based on a given decryption key. 
    :param group: The dictionary key whose value to pull that contains the encrypted movie title in the json file
    :param jsonFile: The json file that contains the dictionary of the groups and their corresponding encrypted movie title
    :param decryptKey: The decryption key needed to decrypt the given movie title
    :return The movie title OR [] on error
    '''
    #opens a given json file, and pulls a value from the given key (group), returns an empty list on error
    try:
        with open(jsonFile) as j:
            newData = json.load(j)
        encryptedMovie = newData[group]
    except:
        return []
    
    #slices the value and converts it to a string
    strEncryptedMovie = (encryptedMovie[0])
    
    #uses a given decryption key to decrypt the value pulled from the above json file, returns an empty list on error
    try:
        key = (decryptKey.encode('utf-8'))
        f = Fernet(key)
        quote = f.decrypt(strEncryptedMovie.encode('utf-8'))
    except:
        return []
    #returns the movie title, converting it from byte to string, and adding it to a full sentence
    return ("Movie title is "+quote.decode("utf-8")+".")