import os

def rename_files():
    file_list = os.listdir(r"C:\Users\Clock\Desktop\Python\Secret Message\prank\prank")
    saved_path = os.getcwd()
    pictures = str.maketrans(dict.fromkeys('0123456789'))
    print(file_list)
    os.chdir(r"C:\Users\Clock\Desktop\Python\Secret Message\prank\prank")
    
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(pictures))
        os.rename(file_name, file_name.translate(pictures))
    os.chdir(saved_path)
    
rename_files()
