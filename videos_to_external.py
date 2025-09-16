import os 
import sys
import time 
import shutil 
import datetime 


current_time = datetime.datetime.now()

src_folder_path = "C:/Users/D/Downloads"
dst_folder_path ="E:/movies"

def backup_vidoes():

    src_folder_list = os.listdir(src_folder_path)
    dst_folder_list = os.listdir(dst_folder_path)
    

    for file in src_folder_list:
        if file.endswith(".mkv"):
            if file not in dst_folder_list:
                file_path = f"{src_folder_path}/{file}"
                file_dst_path = f"{dst_folder_path}/{file}"
                shutil.copy(file_path, file_dst_path)
                print(f"\nFile {file} has been copied to {dst_folder_path}")
            else:
                print(f"\tFile {file} already exists in {dst_folder_path}")
        


while True:
    time.sleep(4)
    backup_vidoes()