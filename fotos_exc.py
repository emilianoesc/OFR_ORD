from downpics import *
import os
from newname import *
from openpyxl import load_workbook
from editexcel import *


def fotos_exce():
    #Extrae las fotos y las mueve a enumerar
    path=r'C:\Users\MELY\Desktop'
    directory_extract  = os.path.join(path, 'HACER OFERTAS')
    directory_enumerar  = os.path.join(path, 'ENUMERAR')
    directory_excel  = os.path.join(path, 'ORDEN')
    directory_formatos  = os.path.join(path, 'CH FORMATOS')
    formato =  os.path.join(path, 'FORMATO SISTEMA XO.xlsx') # temp xlsx


    for file in os.listdir(directory_extract):
        if file[0]!='~':
            finish=10
            while True:
                try:
                    finish=int(input("NECECITAS LAS FOTOS:"))
                except:
                    print("OPCIONES 1 o 0")
                else:
                    if finish ==0 or finish==1:
                        break
                    print("OPCIONES 1 o 0")
            completefile=os.path.join(directory_extract,file)
            if finish==1:
                #EXTRAER FOTOS
                name=extract_images_from_excel(completefile)
                shutil.move(os.path.join(directory_extract,name), directory_enumerar)

                #AQUI SE ARREGLAS FOTOS
                cont=0
                cont = int(input("FOTOS ARREGLADAS:"))
                while cont!=1:
                    cont = int(input("FOTOS ARREGLADAS:"))


                #AQUI SE ENUMERA
                d=0
                for subdir, dirs, files in os.walk(directory_enumerar):
                    if d == 0:
                        d+=1
                    else:
                        rows=nname2(subdir,subdir) 
                        shutil.move(subdir, path)
            else:
                rows=int(get_maximum_rows(completefile))-1
                completefile2 = pathlib.Path(completefile)
                name=completefile2.name.replace(''.join(completefile2.suffixes), '')
            #AQUI SE HACE EL EXCEL
            filename=name+'.xlsx'
            temp = os.path.join(path, name+'.xlsx')
            shutil.copyfile(formato, temp)
            infoexcel=os.path.join(path,name+' COSTO.xlsx')
            shutil.move(completefile, infoexcel )

            valid_response = False
            while not valid_response:
                tipo=str(input("XO O SO:")) 
                if tipo.upper() == 'XO' or  tipo.upper() == 'SO':
                    valid_response = True
                else:
                    print("Invalid response. Please enter XO OR SO")

            colcost=0
            while not(str(colcost).isalpha()):
                colcost = input("COLUMNA COSTO:").upper()
            colname='D'
            if tipo=='XO':
                while not(str(colname).isalpha()):
                    colname = input("COLUMNA NOMBRE:").upper()
            colqty=0
            while not(str(colqty).isalpha()):
                colqty = input("COLUMNA QTY:").upper()
            colcolor=0
            while not(str(colcolor).isalpha()):
                colcolor = input("COLUMNA COLOR:").upper()

            color,name,cost,qty=out_info(infoexcel,colname,colcolor,colcost,colqty)
            
            edit_excel(filename,path,rows,cost,name,color,tipo)
            shutil.move(infoexcel,os.path.join(path, os.path.join(path, 'COSTO A VENTA')))
            return colcost


