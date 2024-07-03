
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

#get user input
def userInput():
    #get user input for file path information
    initialName = input("What is the name of the image you want to fuck up? (Case-Sensitive)\n")
    fileType = input("What is the file type of the image you want to fuck up? If you already input a file type, just hit enter.\n")
    finalName = input("What do you want to call the fucked up image?\n")


    #determine what file will be sorted, and what it should be called.  Uses .env to get paths.
    input_path = os.getenv("input_path") + initialName + fileType
    output_path = os.getenv("output_path") + finalName + ".png"

    return input_path, output_path

def determineIntervalFunction():
    Function = input('''What interval function do you want to use?\n
                      0 - Threshold(default)\n
                      1 - Random\n
                      2 - Edges\n
                      3 - Waves\n
                      4 - None\n'''
                      )
    print(Function)

def determineParameter():
    
    Parameters = input('''Please set the customization parameters for your sort.
                       To set input parameters, choose the parameters you wish to change.  All other parameters will be set to default.\n
                        0 - Interval Function(Threshold by default)\n
                        1 - Randomness(0 by default)\n
                        2 - Upper Threshold(0.25 by default)\n
                        3 - Lower Threshold(0.8 by default)\n
                        4 - Character Length(only used in Random and Waves modes)\n
                        5 - Angle(0 by default)\n
                        6 - HELP'''
                        )
    if Parameters != "6":
        print(Parameters)
    else:
        print("OK put in the # of a parameter and ill explain that shit to you\n")
        helpParameters = input('''
                        0 - Interval Function\n
                        1 - Randomness\n
                        2 - Upper Threshold\n
                        3 - Lower Threshold\n
                        4 - Character Length\n
                        5 - Angle\n

def determineSortingFunction():
    Functions = input('''What quality do you want to sort the pixels by?\n
                      0 - lightness\n
                      1 - hue\n
                      2 - saturation\n
                      3 - intensity\n
                      4 - minimum\n'''
                      )
