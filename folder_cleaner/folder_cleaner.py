import os
import shutil

target_folder = 'D:/Downloads'

folders =["Images","Documents","Others"]

for folder in folders:
    folder_path = os.path.join(target_folder, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for file_name in os.listdir(target_folder):
    file_path = os.path.join(target_folder, file_name)
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()
        
        if extension in ['.jpg','.png']:
            dest_folder = "Images"
        elif extension in ['.pdf','.txt','.docx','.pptx']:
            dest_folder = "Documents"
        else:
            dest_folder = "Others"
        dest_path = os.path.join(target_folder, dest_folder, file_name)
        
        shutil.move(file_path, dest_path)
        print(f"Moved: {file_name} --> {dest_folder}")