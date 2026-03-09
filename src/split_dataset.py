import os, random, shutil
images_dir = "D:\\final_year_project\\Smart_Ambulance\\datasets\\vision\\images\\train"
labels_dir = "D:\\final_year_project\\Smart_Ambulance\\datasets\\vision\\labels\\train"
val_images_dir = "D:\\final_year_project\\Smart_Ambulance\\datasets\\vision\\images\\val"
val_labels_dir = "D:\\final_year_project\\Smart_Ambulance\\datasets\\vision\\labels\\val"


# Make sure validation folders exist
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# List all images
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(image_files)

# Move 20% of images + labels to validation set
val_count = int(0.2 * len(image_files))
for img in image_files[:val_count]:
    lbl = os.path.splitext(img)[0] + '.txt'
    shutil.move(os.path.join(images_dir, img), os.path.join(val_images_dir, img))
    shutil.move(os.path.join(labels_dir, lbl), os.path.join(val_labels_dir, lbl))

print(f"✅ Split complete! {val_count} images moved to validation set.")
