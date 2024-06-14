from pixelsort import pixelsort
from PIL import Image
from dotenv import load_dotenv
import os


load_dotenv()


print("Hello and welcome to the Thrush Band Incorporated Image Pulverizer.  Please insert tip.\n\n")


initialName = input("What is the name of the image you want to fuck up?\n")
fileType = input("What is the file type of the image you want to fuck up? If you already input a file type, don't input anything.\n")
finalName = input("What do you want to call the fucked up image?\n")


#determine what file will be sorted, and what it should be called
input_path = os.getenv("input_path") + initialName
output_path = os.getenv("output_path") + finalName + ".png"


#Pixelsorting
path = r"C:\Users\usuario\Desktop\thrushArt\images\Unsorted\download.png"
theImage = Image.open(path) #insert the image you want here.


sortedImage = pixelsort(theImage)


sortedImage.save(output_path)
print("image has been saved to " + output_path)
