import os
import json
import cv2
import numpy as np

data_dir = r"C:\Users\sreej\OneDrive\Documents\DatasetCreation\data8"
transforms_file = os.path.join(data_dir, "transforms.json")

# List to store file paths
file_paths = []
poses = []

with open(transforms_file, 'r') as f:
    data = json.load(f)
    # Iterate over frames
    for frame in data['frames']:
        # Extract file path
        file_path = os.path.join(data_dir, frame['file_path'][2:])
        print(file_path)  # Remove "./" from file path
        file_paths.append(file_path)
        
        # Extract transform matrix
        transform_matrix = np.array(frame['transform_matrix'])
        poses.append(transform_matrix)



# Function to preprocess image
def preprocess_image(img_path):
    # Read image
    img = cv2.imread(img_path)
    # Resize image to 100x100
    img_resized = cv2.resize(img, (100, 100))
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

focal = np.array(138.88887889922103,dtype=np.float64)
print(focal.shape)

output_file = os.path.join(data_dir, "focal.npy")
np.save(output_file, focal)
np.save('focal.npy', focal)

print("Preprocessed images saved to:", output_file)

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
np.savez('3image.npz', **data_dict)