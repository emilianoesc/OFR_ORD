import os
import glob
import math
import shutil


def nname2(directory,rout):

    cwd = os.getcwd()
    all_files=sorted(glob.glob(directory + '/*'))
    #all_files=sorted(glob.glob(directory + '/*'), key=lambda i: int(os.path.splitext(os.path.basename(i))[0]))
    total=int(len(directory))
    fill=math.ceil(math.log(total,10))
    for i,filename in enumerate(all_files, start=1):
        split_tup=os.path.splitext(filename)
        #newname=str(i).zfill(fill)+split_tup[1]
        newname=str(i)+split_tup[1]
        newhead=os.path.join(rout,newname)
        os.rename(filename,newhead)
        #print(newhead)

    #print(len(all_files))
    return len(all_files)
    

def nname3(directory,rout):

    cwd = os.getcwd()
    all_files=sorted(glob.glob(directory + '/*'))
    #all_files=sorted(glob.glob(directory + '/*'), key=lambda i: int(os.path.splitext(os.path.basename(i))[0]))
    total=int(len(directory))
    fill=math.ceil(math.log(total,10))
    for i,filename in enumerate(all_files, start=1):
        split_tup=os.path.splitext(filename)
        splited=split_tup[0].split("\\")
        joined="\\".join(splited[0:6])
        if splited[6].find('(')==-1:
            splited[6]=splited[6]+' (0)'
        newname=joined+'\\'+splited[6].replace('(','0').replace(')','').replace(' ','').zfill(6)+split_tup[1]
        #newname=str(i)+split_tup[1]
        newhead=os.path.join(rout,newname)
        os.rename(filename,newhead)
        print(newname)

    #print(len(all_files))
    return len(all_files)
    