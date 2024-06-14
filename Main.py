from pixelsort import pixelsort
from PIL import Image



print("Hello and welcome to the Thrush Band Incorporated Image Pulverizer.  Please insert tip.")

#Pixelsorting
path = input("What is the path to the image you want to fuck up?")
theImage = Image.open(path) #insert the image you want here.
theImage
sortedImage = pixelsort(theImage)
sortedImage