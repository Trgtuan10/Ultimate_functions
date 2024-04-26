from datasets import load_dataset
from PIL import Image
import os

# Load the dataset from the Hugging Face Hub
dataset = load_dataset("dmarx/corgi-small", split="train")

# Specify the folder where you want to save the images
output_folder = "/path/to/output/folder/"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over the dataset and save the images
for i, example in enumerate(dataset):
    # Assuming the image is stored in the "image" field of the dataset
    image = example["image"]
    
    # Generate a unique filename for each image
    filename = f"image_{i}.jpg"
    
    # Save the image to the output folder
    image.save(os.path.join(output_folder, filename))
    