from pixelsort import pixelsort
from PIL import Image
from dotenv import load_dotenv
import os


load_dotenv()


print("Hello and welcome to the Thrush Band Incorporated Image Pulverizer.  Please insert tip.\n\n")


initialName = input("What is the name of the image you want to fuck up? (Case-Sensitive)\n")
fileType = input("What is the file type of the image you want to fuck up? If you already input a file type, just hit enter.\n")
finalName = input("What do you want to call the fucked up image?\n")


#determine what file will be sorted, and what it should be called.  Uses .env to get paths.
input_path = os.getenv("input_path") + initialName + fileType
output_path = os.getenv("output_path") + finalName + ".png"


#Pixelsorting
print(f"Attempting to open: {input_path}")

try:

    theImage = Image.open(input_path) #insert the image you want here.

    sortedImage = pixelsort(theImage)

    sortedImage.save(output_path)
    print("image has been saved to " + output_path)

except OSError:
    print("OSError, File not found")

except:
    print("Something went wrong")