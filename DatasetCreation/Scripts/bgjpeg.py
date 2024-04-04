import os
from rembg import remove
from PIL import Image
from io import BytesIO

# Directory containing the images from which you want to remove the background
input_dir = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\Data4\images"

# Directory where you want to save the images with the backgrounds removed
output_dir = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\Data4\images"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')  # Change '.jpeg' to '.jpg'

        # Open the image
        with open(input_path, 'rb') as input_file:
            input_image = input_file.read()

            # Remove the background
            output_image = remove(input_image)

            # Save the output image in JPEG format
            image = Image.open(BytesIO(output_image))
            image = image.convert("RGB")  # Convert to RGB to ensure compatibility with JPEG
            image.save(output_path, 'JPEG')  # Change 'JPEG' to 'JPG'

print("Background removal complete.")
