from PIL import Image
import os

# Define the path to the directory containing the PNG files
folder_path = 'train/image/'  # Example path, needs to be adjusted to the actual path

# Define the target size
target_size = (224, 224)

# List all the PNG files in the directory
png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg')]

# Loop through all PNG files and resize them
for file_name in png_files:
    # Open an image file
    with Image.open(os.path.join(folder_path, file_name)) as img:
        # Resize the image
        img_resized = img.resize(target_size, Image.ANTIALIAS)
        
        # Save the resized image back to the filesystem
        resized_path = os.path.join(folder_path, f"{file_name}")
        img_resized.save(resized_path)

# Return the list of resized file paths
resized_files = [os.path.join(folder_path, f"{file_name}") for file_name in png_files]
resized_files
