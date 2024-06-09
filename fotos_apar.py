import os
import shutil
from macros import macros
from editexcel import removerows
from newname import *
from editexcel import *


def oferta():
    path=r'C:\Users\MELY\Desktop'
    formatos=os.path.join(path, 'CH FORMATOS')
    dictformatos={}

    for file in os.listdir(formatos):
        number=file[-7:-5].strip()
        if number.isnumeric():
            dictformatos[int(number)]=os.path.join(formatos, file)
    
    directory  = os.path.join(path, 'HACER OFERTAS')
    chdirectory = os.path.join(path, 'CH')
    formato =  os.path.join(path, 'FORMATO SISTEMA XO.xlsx') # temp xlsx
    for dirs in os.listdir(directory):
        print(dirs)
        cells = int(input("CELLS:"))

        valid_response = False
        while not valid_response:
            precios=str(input("YA TIENES LOS PRECIOS:")) 
            if precios == '1' or  precios == '0':
                valid_response = True
            else:
                print("Invalid response. Please enter 1 OR 0")

        insidedir=os.path.join(directory, dirs)
        excel=os.path.join(path, dirs +' COSTO.xlsx')
        
        form1=dictformatos[cells]
        shutil.copy(form1,excel)

        for file in os.listdir(insidedir):
            fileroot=os.path.join(insidedir, file)
            shutil.copy2(fileroot,chdirectory )     

        macros(excel,cells)

        #ENUMERACION
        i=0
        for subdir, dirs2, files in os.walk(directory):
            if i == 0:
                i=i+1
            else:
                rows=nname2(subdir,subdir) 
    
        i=0
        for file in os.listdir(chdirectory):
            os.remove(os.path.join(chdirectory, file))
            i+=1
        
        shutil.move(insidedir, path)

        removerows(excel,(cells*i)+2,(301*cells)-i)

        print ((cells*i)+2) 

        os.startfile(excel)
        if precios=='1':


            #put prices and products
            finish=10
            while True:
                try:
                    finish=int(input("FINISH:"))
                except:
                    print("OPCIONES 1 o 0")
                else:
                    if finish ==0 or finish==1:

                        break
                    print("OPCIONES 1 o 0")
                    
                        
            if finish==1:
                excelsist=os.path.join(path, dirs +'.xlsx')
                shutil.copyfile(formato, excelsist)
                
                
                color,name,cost,qty=out_info(excel,'C','D','F','D')
                edit_excel( dirs +'.xlsx',path,rows,cost,name,color)

