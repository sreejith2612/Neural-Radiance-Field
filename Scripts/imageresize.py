import os
from PIL import Image, ImageOps

def resize_images_in_folder(folder_path, resize_factor=0.1):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-image files (optional: adjust the extensions based on your image types)
    image_files = [f for f in files if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

    # Sort image files to ensure consistent naming
    image_files.sort()

    # Process each image file
    for index, image_file in enumerate(image_files):
        # Construct the full file path
        image_path = os.path.join(folder_path, image_file)
        
        # Open the image
        with Image.open(image_path) as img:
            # Apply EXIF transpose to handle orientation metadata
            img = ImageOps.exif_transpose(img)
            
            # Calculate the new size
            new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
            
            # Resize the image
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Construct the new file name
            new_file_name = f"{index + 1:04d}.png"
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Save the resized image
            resized_img.save(new_file_path)

            # Optionally, remove the original image if it's different from the new one
            if image_path != new_file_path:
                os.remove(image_path)

# Specify the folder path containing the images
folder_path = r'C:\Users\sreej\OneDrive\Documents\DatasetCreation\Rubixcube\images'  # Adjust the path as needed

# Call the function to resize images
resize_images_in_folder(folder_path)
