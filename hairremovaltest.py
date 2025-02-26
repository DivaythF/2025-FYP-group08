import functions as fun 
import cv2 


rgb, grey = fun.readImageFile("data/img_0918.png")

blackhat, thresh, img_out = fun.removeHair( rgb, grey, kernel_size=25, threshold=10, radius=3)
fun.saveImageFile(img_out, "test_removal/someImage.png")

