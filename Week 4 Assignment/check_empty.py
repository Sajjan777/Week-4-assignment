import os
def check_file_empty(file_path):
    return os.path.getsize(file_path) == 0  

file_path = "example.txt" 
if check_file_empty(file_path):
    print("The file is empty.")
else:
    print("The file is not empty.")
