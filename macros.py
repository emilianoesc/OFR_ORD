import win32com.client
from pathlib import Path

def macros(save_path,cells):

    # Sets up Excel to run Macro
    try:
        xl = win32com.client.Dispatch('Excel.Application')
        xl.visible = False
        personal_wb = xl.workbooks.Open(
            Filename=r"C:\Users\MELY\AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB")
        wb = xl.workbooks.Open(Filename=save_path)
        xl.Run("'PERSONAL.XLSB'!ImageMacroAuto5",cells)
        wb.Close(SaveChanges=1)
        xl.Quit()
        print("Macro ran successfully")
    except:
        print("Error found while running the excel macro")
        xl.Quit()