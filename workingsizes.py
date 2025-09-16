import os 
import shutil 


src_path = "C:/Users/D/Desktop/src"
dst_path = "C:/Users/D/Desktop/dst"

src_path_list = os.listdir(src_path)
dst_path_folders = os.listdir(dst_path)

print(dst_path_folders)

for f in dst_path_folders:
    print(f"{dst_path}/{f}")
    subdir = f"{dst_path}/{f}"
    subdir_ls = os.listdir(subdir)
    print(subdir_ls)
    for fs in subdir_ls:
        print(f"\n{fs}")
        src = f"{subdir}/{fs}"
        src_status = os.stat(src)
        print(f"{src} {src_status.st_size} bytes")
        print(src)




