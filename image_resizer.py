import os
from PIL import Image

input_folder = "images"
output_folder = "resized_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

new_size = (800, 800)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        resized_img = img.resize(new_size)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
        resized_img.save(output_path)
        print(f"✅ Resized and saved: {output_path}")

print("🎯 All images have been resized and saved successfully!")
