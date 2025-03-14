import os
import shutil
import time

now = time.time()
one_month = now-30*24*60*60
path = r"C:\ar_dicom"

def check_file(path):
    if os.path.exists(path):
        for file in os.listdir(path):
            file_create = os.path.getctime(os.path.join(path, file))
            if file_create < one_month:
                if os.path.isdir(os.path.join(path, file)):
                    in_folder = os.path.join(path, file)
                    try:
                        shutil.rmtree(in_folder)
                        print(f"file delete {in_folder}")
                    except Exception as e:
                        print(e)
        else:
            print("Path not found!")

if __name__ == "__main__":
    check_file(path)