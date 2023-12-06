# Name: Group Krumrie (Alexander Fletcher, Andrew Etheridge, Evan Bleh, and Kirubel Teklemariam)
# email: fletchax@mail.uc.edu, etheriaw@mail.uc.edu, blehet@mail.uc.edu, and teklemka@mail.uc.edu
# Assignment Title: Final Project
# Due Date: Dec 7, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: PyDev project to use a json and text file to build a location sentence, then decrypt an encrypted movie title, then load a picture of our group at that location with sign that has a quote from that movie.
# Citations: NA
# Anything else that's relevant: NA

from PIL import Image
#updates code from PIL's ImageFile, to allow the image to load
#Got this from stackoverflow (url: https://stackoverflow.com/questions/12984426/pil-ioerror-image-file-truncated-with-big-images)
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def loadImage(fileName):
    '''
    Load and show an image file.
    :param fileName: The image file to load
    :return The image object being loaded OR loads nothing on error
    '''
    #opens and loads the given image file (fileName), returns None on error
    try:
        myImage = Image.open(fileName)
        myImage.load()
    except:
        myImage = None
    return myImage