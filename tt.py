import os 
import shutil 
import time 
import datetime 
from rich.console import Console



def backup_files():
    console = Console()
    BOLD = "\033[1m]"
    ENDBOLD = "\033[0m]"

    src_path = "C:/Users/D/Desktop/src" # source directory
    dst_path = "C:/Users/D/Desktop/dst" # backup directory

    src_path_list = os.listdir(src_path) # list files in src directory for easy iteration
    dst_path_list = os.listdir(dst_path)

    

    for file in src_path_list:
        textfolder_path = f"{dst_path}/textfolder"
        imagefolder_path = f"{dst_path}/image" #image directory
        pdffolder_path = f"{dst_path}/pdf_files"
        audiofolder_path = f"{dst_path}/audio"
        videosfolder_path = f"{dst_path}/videos"

       
        textfolder_path_list = os.listdir(textfolder_path)
        #print(audiofolder_path)
        #aud_p = os.listdir(audiofolder_path)
        #print(f"audio list= {aud_p}")

        root,extension = os.path.splitext(file)

        list_of_images_ext = (
            '.png', '.jpeg', '.JPG', '.svg','.gif','.jpg','.jpe'
        )
        
    
        for textfile in textfolder_path_list:
            textfile_path = f"{textfolder_path}/{textfile}"
            texfile_size = os.path.getsize(textfile_path)
            continue
        
        

        src = f"{src_path}/{file}" #path of a file 
        # src_status = os.stat(src)
       # print(src_status.st_size)

        root,extension = os.path.splitext(src) # returns a file's root and extension

       
            
        # text files
        if file.endswith(".txt"):
            fil_path = f"{src_path}/{file}"
            if not os.path.exists(textfolder_path): #if the folder does not exist
                os.makedirs(textfolder_path)    #create the folder 
                #textfolder_path_list = os.listdir(textfolder_path) #list containing files in the folder created

                shutil.copy(fil_path,textfolder_path) #copy the file to the folder created
                print(f"{BOLD}[+]{ENDBOLD} {file} moved to {textfolder_path}")
            else:
                if file not in textfolder_path_list: #when file is not  the folder created
                    shutil.copy(fil_path,textfolder_path)       #copy file to the folder created. 
                    print(f"{BOLD}[+]{ENDBOLD} {file} copied to {textfolder_path} @ {now}") #print out the file name and the timestamp
                else:
                    #os.replace(fil_path,textfile_path)
                    print(f"\t{BOLD}[-]{ENDBOLD} {file} exist already skip...")

        elif file.endswith(extension) and extension in list_of_images_ext:  #checks if the file is an image file
            
            if not os.path.exists(imagefolder_path):
                os.makedirs(imagefolder_path)
                #imagefolder_path_list = os.listdir(imagefolder_path)
                shutil.copy(src,imagefolder_path)
                print(f"{BOLD}[+]{ENDBOLD} {file} copied to {imagefolder_path} @ {now}")
            else:
                if file not in os.listdir(imagefolder_path):
                    shutil.copy(src,imagefolder_path)
                    print(f"{BOLD}[+]{ENDBOLD} {file} copied to {imagefolder_path} @ {now}")
            #shutil.copy(src,textfolder_path) # moves file without the extension .txt to the dst folder not the textfolder

        #checking if file is pdf
        elif file.endswith(".pdf"):     #checking if file is a pdf file
            if not os.path.exists(pdffolder_path):
                os.makedirs(pdffolder_path)
                shutil.copy(src,pdffolder_path)
                print(f"{BOLD}[+]{ENDBOLD} {file} copied to {pdffolder_path} @ {now}")
            else:
                if file not in os.listdir(pdffolder_path):
                    shutil.copy(src,pdffolder_path)
                    print(f"{BOLD}[+]{ENDBOLD} {file} copied to {pdffolder_path} @ {now}")
                else:
                    print(f"\t{BOLD}[-]{ENDBOLD} {file} exist already skip...")
        
        #CHECKING FOR AUDIO FILES
        elif file.endswith(".mp4") or file.endswith(".mp3"):
            if not os.path.exists(audiofolder_path):
                os.makedirs(audiofolder_path)
                shutil.copy(src,audiofolder_path)
                print(f"{BOLD}[+]{ENDBOLD} {file} copied to {audiofolder_path} @ {now}")
            else:
                if file not in os.listdir(audiofolder_path):
                    shutil.copy(src,audiofolder_path)
                    print(f"{BOLD}[+]{ENDBOLD} {file} copied to {audiofolder_path} @ {now}")
                else:
                    print(f"\t{BOLD}[-]{ENDBOLD} {file} exist already skip...")

        #CHECKING VIDEO FILES
        elif file.endswith(".mkv") or file.endswith(".mp4"):
            if not os.path.exists(videosfolder_path):
                os.makedirs(videosfolder_path)
                shutil.copy(src,audiofolder_path)
                print(f"{BOLD}[+]{ENDBOLD} {file} copied to {audiofolder_path} @ {now}")
            else:
                if file not in os.listdir(videosfolder_path):
                    shutil.move(src,videosfolder_path)
                    print(f"{BOLD}[+]{ENDBOLD} {file} copied to {audiofolder_path} @ {now}")
                else:
                    print(f"\t{BOLD}[-]{ENDBOLD} {file} exist already skip... ")


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        print("\n\t=====Start Backup @ {} ===== \n".format(now))   
        time.sleep(4)     
        
        backup_files() #function for backing up files from src folder to dst foldeer