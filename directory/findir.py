import os

def find(path, dire):
    for folder in os.listdir(path):
        if folder == dire:
            os.chdir(dire)
            print('+' + os.getcwd(dire))
        elif '.' not in folder:
            find(folder,dire)
        else:
            print("That's All")
            break
    return

print(os.listdir(r"C:\Users\ssv\OneDrive - Polytama Propindo\Documents\Flakes"))
