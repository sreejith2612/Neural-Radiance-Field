import os
import io
from rembg import remove
from PIL import Image

def remove_background(image_path, output_folder):
    # Load image
    with open(image_path, "rb") as f:
        image = f.read()
    
    # Remove background using rembg
    bg_removed_image = remove(image)
    
    # Convert image data to PIL Image object
    img = Image.open(io.BytesIO(bg_removed_image))
    
    # Convert image to RGBA (if not already)
    img = img.convert("RGBA")
    
    # Save the processed image with transparent background as PNG
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
    img.save(output_path)

    print(f"{filename} converted to png")

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add more extensions if necessary
            image_path = os.path.join(input_folder, filename)
            remove_background(image_path, output_folder)


if __name__ == "__main__":
    input_folder = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\Data4\images"
    output_folder = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\Data4\images"
    process_images(input_folder, output_folder)
