# Name: Group Krumrie (Alexander Fletcher, Andrew Etheridge, Evan Bleh, and Kirubel Teklemariam)
# email: fletchax@mail.uc.edu, etheriaw@mail.uc.edu, blehet@mail.uc.edu, and teklemka@mail.uc.edu
# Assignment Title: Final Project
# Due Date: Dec 7, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: PyDev project to use a json and text file to build a location sentence, then decrypt an encrypted movie title, then load a picture of our group at that location with sign that has a quote from that movie.
# Citations: NA
# Anything else that's relevant: NA

#imports functions from the place, picture, and movie modules in the placePackage, picturePackage, and moviePackage respectively
from placePackage.place import *
from picturePackage.picture import *
from moviePackage.movie import *

#makes sure to only run the below if this is the main page (entry point)
if __name__ == "__main__":
    #prints the groupSentence function pulled from place module in the placePackage, using the given group, jsonFile, and textFile
    print(groupSentence("Krumrie","EncryptedGroupHints Fall 2023 Section 001.json","english-2.txt"))
    
    #prints the Movie function pulled from movie module in the moviePackage, using the given group, jsonFile, and decryptKey
    print(Movie("Krumrie","TeamsAndEncryptedMessagesForDistribution.json","5cO4IoIiCYWy9oCnI8e2bKQYCGRCnp1TOw_4oApG9RE="))
    
    #pulls the loadImage function from the picture module in the picturePackage, using the given image file (fileName)
    ourImage = loadImage("GroupPic.jpg")
    #displays the loaded image
    ourImage.show(ourImage)