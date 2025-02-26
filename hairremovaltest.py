import functions as fun 
import cv2

#get paths and save in some list
imagePaths = fun.ImageDataLoader("data")._get_image_paths()
#print(imagePaths)

#loop through original images, remove hair and save in different directory
for i in range(len(imagePaths)):
    rgb, grey = fun.readImageFile(imagePaths[i])
    _, _, img = fun.removeHair(rgb, grey)
    fun.saveImageFile(img, f"hairRemoval/removed_{917+i}.png")



