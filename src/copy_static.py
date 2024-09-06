import os
import shutil

def copy_directory(from_copy, to_copy):
    current_dir = os.path.dirname(__file__)
    copy_from = os.path.join(current_dir, '..', from_copy)
    copy_to = os.path.join(current_dir, '..', to_copy)

    if not os.path.isdir(copy_to):
        print(f"Directory {copy_to} does not exist")
        return
    if not os.path.isdir(copy_from):
        print(f"Directory {copy_from} does not exist")
        return
    
    for item in os.listdir(copy_from):
        item_path = os.path.join(copy_from, item)

        if os.path.isfile(item_path):
            shutil.copy(item_path, copy_to)
            print(f"File {item_path} copied successfully")
        elif os.path.isdir(item_path):
            isolate_text = item_path.rfind('/')
            item_name = item_path[isolate_text + 1:]
            new_location = copy_to + f"/{item_name}"
            os.mkdir(new_location)
            copy_directory(item_path, new_location)