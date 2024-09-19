from PIL import Image

# Load the image uploaded by the user
file_path = '/content/sample_data/chapter1.jpg'
loaded_image = Image.open(file_path)

# Show basic image information
image_details = loaded_image.size, loaded_image.mode
image_details

# Generating random value

import time

# With the current timestamp as a guide, generate the number.
current_timestamp = int(time.time())
generated_random_value = (current_timestamp % 100) + 50

# Add 10 more if the generated number is even.
if generated_random_value % 2 == 0:
    generated_random_value += 10

generated_random_value

# Total red pixel value

import numpy as np
from PIL import Image

# Convert image to a numpy array for pixel manipulation
image_array = np.array(loaded_image)

# Create a new array for the modified image
updated_image_array = image_array.copy()

# Add the generated random value to each (R, G, B) value, ensuring values don't exceed 255
updated_image_array = np.clip(updated_image_array + generated_random_value, 0, 255)

# Calculate the sum of all the red (R) pixel values in the modified image
total_red_pixel_value = np.sum(updated_image_array[:, :, 0])

# Create a new image from the modified array
output_image = Image.fromarray(updated_image_array.astype('uint8'))

# Save the modified image
output_file_path = '/content/sample_data/chapter1.jpg'
output_image.save(output_file_path)

total_red_pixel_value, output_file_path