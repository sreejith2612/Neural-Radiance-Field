import os
import json
import cv2
import numpy as np
import os
from rembg import remove
from PIL import Image
from io import BytesIO


data_dir = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\data8"
transforms_file = os.path.join(data_dir, "transforms.json")
input_dir = os.path.join(data_dir,"images")
output_dir = input_dir

if True:
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


file_paths = []
poses = []

with open(transforms_file, 'r') as f:
    data = json.load(f)
    # Iterate over frames
    for frame in data['frames']:
        # Extract file path
        file_path = os.path.join(data_dir, frame['file_path'][2:])  # Remove "./" from file path
        file_paths.append(file_path)
        
        # Extract transform matrix
        transform_matrix = np.array(frame['transform_matrix'])
        poses.append(transform_matrix)



# Function to preprocess image
def preprocess_image(img_path):
    # Read image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Resize image to 100x100
    width, height, _ = img.shape
    img_resized = cv2.resize(img, (100, int(100*width/height)))
    # Convert image to float32 and scale to range [0, 1]
    img_rescaled = img_resized.astype(np.float32) / 255.0
    return img_rescaled

# List to store preprocessed images
preprocessed_images = []

# Iterate over file paths
for img_path in file_paths:
    # Preprocess image
    preprocessed_img = preprocess_image(img_path)
    # Append preprocessed image to list
    preprocessed_images.append(preprocessed_img)
    print(img_path)

# Convert list to numpy array
preprocessed_images = np.array(preprocessed_images)
print(preprocessed_images.shape)

output_file = os.path.join(data_dir, "images.npy")
np.save(output_file, preprocessed_images)
np.save("images.npy", preprocessed_images)

poses = np.array(poses,dtype=np.float32)
print(poses.shape)

output_file = os.path.join(data_dir, "poses.npy")
np.save(output_file, poses)
np.save('poses.npy', poses)

focal = np.array(140,dtype=np.float64)
print(focal.shape)

output_file = os.path.join(data_dir, "focal.npy")
np.save(output_file, focal)
np.save('focal.npy', focal)

print("Preprocessed the data")

npy_files = ['images.npy', 'poses.npy', 'focal.npy']

# Initialize an empty dictionary to store the data
data_dict = {}

# Load each .npy file and store its contents in the dictionary
for npy_file in npy_files:
    # Extract the name of the variable from the file name (excluding the extension)
    variable_name = npy_file.split('.')[0]
    
    # Load the data from the .npy file
    data = np.load(npy_file)
    
    # Store the data in the dictionary with the variable name as the key
    data_dict[variable_name] = data

# Save the data dictionary as a .npz file
np.savez('new_data.npz', **data_dict)

print("Data saved as .npz file")