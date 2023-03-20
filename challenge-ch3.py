import os
from os import path

def main():
    # create a new directory
    new_folder = os.mkdir("folder01")

    # create a new text file within the directory
    save_path = 'folder01'
    file_name = "dir_listing.txt"
    completeName = os.path.join(save_path, file_name)
    file1 = open(completeName, "a")
    
    # write into the file a listing of all files in the current directory, and the total byte count of all the files. Only count files, not directories.
    filesList = os.listdir()
    totalBytes = 0    
    for x in filesList:
        if os.path.isfile(x):
            file1.write(x + "\n")
            totalBytes += os.path.getsize(x)
        
    file1.write("The total number of bytes is " + str(totalBytes))
    file1.close()
      
if __name__ == "__main__":
    main()