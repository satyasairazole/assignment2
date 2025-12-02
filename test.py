import os
import shutil

source_folder = r"D:\aass\uploads"

avatar_folder = os.path.join(source_folder, "avatar")
selfie_folder = os.path.join(source_folder, "selfie")

os.makedirs(avatar_folder, exist_ok=True)
os.makedirs(selfie_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isdir(file_path):
        continue

    lower_name = file_name.lower()

    if "avatar" in lower_name:
        shutil.move(file_path, os.path.join(avatar_folder, file_name))
        print(f"Moved to avatar: {file_name}")

    elif "selfie" in lower_name:
        shutil.move(file_path, os.path.join(selfie_folder, file_name))
        print(f"Moved to selfie: {file_name}")
