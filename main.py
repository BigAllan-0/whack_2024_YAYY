from detecting_people import get_people
from image_captioning import get_engagement
import os
import shutil


def delete_folder_contents(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print("The folder does not exist.")
        return

    # Iterate over the files and directories inside the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # If it's a file, delete it
        if os.path.isfile(item_path):
            os.remove(item_path)

        # If it's a directory, remove the directory and its contents
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted directory and its contents: {item_path}")
