import os

def find(path, dire):
    for folder in os.listdir(path):
        try:
            if folder == dire:
                os.chdir(path + '\\' + dire)
                print('+-> ' + os.getcwd())
            elif '.' not in folder:
                find(path + '\\' + folder,dire)
            elif '.' in folder:
                continue
            else:
                break
        except:
            print('+-> ' + folder + ' does not allow to be searched')
            continue
    return

find(r'C:\Users\mrm\Documents', 'python')
