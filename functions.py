import random
import os
import cv2

class ImageDataLoader:
    def __init__(self, directory, image_size=(224, 224)):
        self.directory = directory
        self.image_size = image_size
        self.image_paths = self._get_image_paths()
        
    def _get_image_paths(self):
        
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        image_paths = []

        for filename in os.listdir(self.directory):
            full_path = os.path.join(self.directory, filename)
        
           

        # Check if the file is an image
            if any(filename.lower().endswith(ext) for ext in valid_extensions):
                image_paths.append(full_path)
                

        return image_paths
        
def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False

def removeHair(img_org, img_gray, kernel_size=25, threshold=10, radius=3):
    # kernel for the morphological filtering
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    # perform the blackHat filtering on the grayscale image to find the hair countours
    blackhat = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)

    # intensify the hair countours in preparation for the inpainting algorithm
    _, thresh = cv2.threshold(blackhat, threshold, 255, cv2.THRESH_BINARY)

    # inpaint the original image depending on the mask
    img_out = cv2.inpaint(img_org, thresh, radius, cv2.INPAINT_TELEA)

    return blackhat, thresh, img_out

rgb, grey = readImageFile("data/img_0918.png")

blackhat, thresh, img_out = removeHair( rgb, grey, kernel_size=25, threshold=10, radius=3)
saveImageFile(img_out, "test_removal/someImage.png")