
import os
import shutil 
import time 
import datetime 
from rich.console import Console 



def main():
    BOLD = "\033[1m"
    RESET = "\033[0m"
    console = Console() 
    console.print("[bold]hello world[/bold]")

    src_path = "C:/Users/D/Desktop/src"
    list_of_images_ext = (
            '.png', '.jpg', '.JPG', '.svg','.gif'
        )

    print(f'\n{BOLD}Second bold method test{RESET}\n')
    for file in os.listdir(src_path):
        print("file: ",file)
        file_path = f"{src_path}/{file}"
        root,extension = os.path.splitext(file_path)
        print(f'\nfile path: {file_path}')
        console.print(f'\nfile root: {root} and file extension: {extension}')

        # if file.endswith(extension) and extension in list_of_images_ext:
        #     print("image files: ", file)
        # else:
        #     print("\nother: ", file)

    # root, extension = os.path.splitext(src_path)
    # print(f"root of path: {root}")
    # print(f"extension of file: {extension}")
    # if 

if __name__ == '__main__':
    main()