import os
import shutil
from copy_static import copy_directory

def main():
    clear_directory()
    copy_directory('static', 'public')


def clear_directory():
    current_dir = os.path.dirname(__file__)
    target_dir = os.path.join(current_dir, '..', 'public')

    if not os.path.isdir(target_dir):
        print(f"Directory {target_dir} does not exist")
        return
    
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Removed file {item_path}")
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Removed directory {item_path}")


main()