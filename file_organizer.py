import os
import shutil

# Folder path to organize
path = input("Enter Folder Path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"],
    "Archives": [".zip", ".rar"]
}

# Check if folder exists
if not os.path.exists(path):
    print("Folder does not exist!")
    exit()

# Read all files
files = os.listdir(path)

for file in files:

    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    moved = False

    # Match extension with category
    for folder_name, extensions in file_types.items():

        if extension in extensions:

            folder_path = os.path.join(path, folder_name)

            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, file))

            print(f"Moved: {file} → {folder_name}")

            moved = True
            break

    # For unknown file types
    if not moved:

        others_folder = os.path.join(path, "Others")

        if not os.path.exists(others_folder):
            os.makedirs(others_folder)

        shutil.move(file_path, os.path.join(others_folder, file))

        print(f"Moved: {file} → Others")

print("\nFiles Organized Successfully!")