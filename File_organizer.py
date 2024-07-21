import os
import shutil

path=input("Enter path of folder:")
folder=os.listdir(path)
for file in folder:
    filename,extenction=os.path.splitext(file)
    extenction=extenction[1:]

    if os.path.exists(path+'/'+extenction):
        shutil.move(path +'/'+file,path +'/'+extenction+'/'+file)
    else:
        os.makedirs(path+'/'+extenction)
        shutil.move(path +'/'+file,path +'/'+extenction+'/'+file)
