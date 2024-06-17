from fotos_apar import *
from fotos_exc import *
from venta import *


valid_response = False
while not valid_response:
    tipo=str(input("EXCEL(1) O FOTOS(2):")) 
    if tipo == '1' or  tipo == '2':
        valid_response = True
        if tipo=='1':
            colcost=fotos_exce()
            hacerventa(colcost)
        else:
            oferta()
            hacerventa()
            
    else:
        print("Invalid response. Please enter 1 OR 2")
