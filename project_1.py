#copy files from one directory to another


import shutil 
import os 
import time 
import datetime 


now = datetime.datetime.now()

start_time = time.sleep(60)

while True:
    print("=====start=====")
    path1 = "C:/Users/D/Desktop/source_folder" # folder filese are been copied from 
    path2 = "C:/Users/D/Desktop/backup_folder" # folder where files are been copied to

    def backup_files(file):
        dir = (f"{path1}/{file}")
        shutil.copy(dir, path2)
        #print(f"File {file} copied to {path2} at {now}")
        #print('Done...\n')
        #p2l = os.listdir(path2)
    

    #def move_to_image_dir():

    
        

                
    def move_files_to_directories():
        text_folder_path = f"{path2}/textfolder"
        py_folder_path = f"{path2}/py_folder"
        image_folder_path =  f"{path2}/image_folder"

      

        if not os.path.exists(text_folder_path):
            os.makedirs(text_folder_path)
        elif not os.path.exists(py_folder_path):
            os.makedirs(py_folder_path)
        elif not os.path.exists(image_folder_path):
            os.makedirs(image_folder_path)
        else:
            pass

        textfolder_list = os.listdir(text_folder_path)
        print(textfolder_list)

        for file in os.listdir(path2):
            if file.endswith(".txt"):   
                src = f"{path2}/{file}"
                dst = (f"{text_folder_path}/{file}")
                if file not in textfolder_list: #checks if file is not a subdir textfolder it should move to texfolder
                    shutil.move(src,dst)
                    print(f"File {file} moved to {text_folder_path} at {now}")
                else:
                    print(f"\t{file} already exist {text_folder_path}. skipping...")
                    

            elif file.endswith(".py"):
                src = f"{path2}/{file}"
                dst = (f"{py_folder_path}/{file}")
                shutil.move(src,dst)
                print(f"File {file} moved to {py_folder_path} at {now}")

            elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".JPG") or file.endswith(".jfif"):
                src = f"{path2}/{file}"
                dst = (f"{image_folder_path}/{file}")
                shutil.move(src,dst)
                print(f"File {file} moved to {image_folder_path} at {now}")


    path1_list = os.listdir(path1)
    path2_list = os.listdir(path2)
    #textfolder_list = os.listdir(text_path)


    for file in path1_list:
        if file not in path2_list:
            time.sleep(60)
            backup_files(file)
            move_files_to_directories() 
       
        else:
            if file.endswith(".txt") and file.endswith(".jpg") and file.endswith(".JPG"):
                file_path = f"{path2}/{file}"
                os.remove(file_path) #delete a file that exist in backup folder after moving to a sub directory
            print(f"File {file} already exists in {path2}. Skipping...")    

