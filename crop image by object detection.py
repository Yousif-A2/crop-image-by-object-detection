import pandas as pd
from PIL import Image
import os


name = 'valid'
# Function to crop and save the image based on coordinates
def crop_and_save_image(input_image_path, output_image_path, xmin, ymin, xmax, ymax):
    image = Image.open(name + "/"+input_image_path)
    cropped_image = image.crop((xmin, ymin, xmax, ymax))
    cropped_image.save(output_image_path)

# Read the Excel file containing the data (columns: filename, xmin, ymin, xmax, ymax, class)
excel_file_path = name+'\_annotations.csv'
data = pd.read_csv(excel_file_path)

# Create a new folder for each class and move the cropped images
for index, row in data.iterrows():
    class_name = row['class']
    class_folder = os.path.join(name+"Crop", class_name)
    os.makedirs(class_folder, exist_ok=True)
    
    filename = row['filename']
    xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
    input_image_path = os.path.join(filename)  # Assuming input images are in the 'input_images' folder
    output_image_path = os.path.join(class_folder, filename)
    
    crop_and_save_image(input_image_path, output_image_path, xmin, ymin, xmax, ymax)

print("Cropping and sorting completed.")