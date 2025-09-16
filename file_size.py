import os 
import shutil  
file1 = "C:/Users/D/Desktop/backup_folder/textfolder/bulls.txt"
file2 = "C:/Users/D/Desktop/backup_folder/textfolder/chicago.txt"

file1_stats = os.stat(file1)
file2_stats = os.stat(file2)

#print(f"{file1_stats} ")

print(f"file 1 size: {file1_stats.st_size} bytes")
print(f"file 2 size: {file2_stats.st_size} bytes")

if file1_stats.st_size == file2_stats.st_size:
    print(f"\thas the same ")
else:
    print("\tdifferent sizes.")
    print(os.replace(file1,file2))
    print(file1)

backup = "C:/Users/D/Desktop/backup_folder/textfolder"
d = os.listdir(backup)
for file in os.listdir(backup):
    src = f"{backup}/{file}"
    src_status = os.stat(src)
    src_size = src_status.st_size
    print(f"{file} size: {src_size} bytes")

