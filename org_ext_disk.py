

'''
ORGANISE FILES IN MY EXTERNAL 
HARD DISK
'''


import os
import shutil
import time
import datetime


hdd_path = "D:" #path of the external drive
list_extensions = [".docx", ".pptx", ".pdf","xlsx"]

others_dir = f"{hdd_path}/others"


pdf_dir  = f"{hdd_path}/pdf"

def organize():
    if not os.path.exists(others_dir):
        os.makedirs(others_dir)
    elif not os.path.exists(f"{hdd_path}/pdf"):
        os.makedirs(f"{hdd_path}/pdf")

    ls_dir = os.listdir(hdd_path) #list of directories and files in the external drive
    print(ls_dir)
    for file in ls_dir:
        print(file)
        file_path = f"{hdd_path}/{file}"
        if file.endswith(".docx"):
            shutil.move(file_path, others_dir)
        elif file.endswith(".pdf"):
            shutil.move(file_path, pdf_dir)
            print("file is moved")

if os.path.exists(hdd_path): #checking to see if path actually exist
   organize()
else:
    print('no')