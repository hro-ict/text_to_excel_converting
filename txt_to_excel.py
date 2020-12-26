import easygui
import pandas as pd
import os


msg = "1.Type delimiter\n2.Choose name of excel file" # message 
title = "TXT TO EXCEL CONVERTER" # title window
fieldNames = ["Delimiter","Excel File"]
fieldValues = [] 
fieldValues = easygui.multenterbox(msg,title, fieldNames)

easygui.msgbox(msg="",image="images/txt_file.gif")
source= easygui.fileopenbox(msg="Choose Text File", title="title", default=".txt", filetypes="*.txt", multiple=False)
easygui.msgbox(msg="",image="images/excel_file.gif")
#target= easygui.diropenbox(msg="Choose Target", title=None, default=None)
target=easygui.filesavebox(msg=None, title=None, default=fieldValues[1]+".xlsx", filetypes="*.xlsx")
txt_reading= pd.read_table(source, sep=fieldValues[0])


txt_reading.to_excel(target, index=False)
choose=easygui.ccbox(msg='THE TEXT FILE SUCCESSFULLY CONVERTED TO EXCEL\n'
                  'CLICK ON "OPEN" TO OPEN THE EXCEL FILE'
                  '\nCLICK ON " EXIT" TO EXIT ', title=' ', choices=('OPEN', 'EXIT'),
              image="images/success.gif", default_choice='OPEN',
              cancel_choice='EXIT')
if choose==1:
    os.startfile(target)
else:
    quit() 
