import functions as fun
import cv2
from PIL import Image
import os

# Get paths and save in some list
imagePaths = fun.ImageDataLoader("../../data")._get_image_paths()

# Create output directory if it doesn't exist
output_dir = "mergedImages"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through original images, remove hair, save, and merge with processed images
for i in range(len(imagePaths)):
    # Read and process the original image
    rgb, grey = fun.readImageFile(imagePaths[i])
    _, _, img = fun.removeHair(rgb, grey)
    fun.saveImageFile(img, f"hairRemoval/removed_{917 + i}.png")

    # Paths to the original and processed images
    original_img_path = imagePaths[i]
    processed_img_path = f"hairRemoval/removed_{917 + i}.png"

    # Open the original and processed images using Pillow
    original_img = Image.open(original_img_path)
    processed_img = Image.open(processed_img_path)

    # Get the dimensions of each image (assuming they have the same height)
    width1, height1 = original_img.size
    width2, height2 = processed_img.size

    # Create a new image with the combined width and maximum height
    combined_image = Image.new('RGB', (width1 + width2, max(height1, height2)))

    # Paste the images side by side
    combined_image.paste(original_img, (0, 0))
    combined_image.paste(processed_img, (width1, 0))

    # Save the combined image
    combined_image.save(f"{output_dir}/merged_{917 + i}.png")

