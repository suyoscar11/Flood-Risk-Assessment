
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Titlebar
import pandas as pd


# We have added a Colour Themes to the windows.
sg.theme('DarkTeal9')

#EXCEL_FILE = 'User Data.xlsx'
#PATH ="C:\\Users\Suyog Gaire\Desktop\User Details\User Data.xlsx"
df=pd.read_excel("User Data.xlsx")

sg.popup('Please Enter the following details to know about the weather condition of your locality')
layout = [
   [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
   [sg.Text('Country', size=(15,1)), sg.InputText(key='Country')],
   [sg.Text('City', size=(15,1)), sg.InputText(key='City')],
   [sg.Text('Enter your E-mail', size=(15,1)), sg.InputText(key='Enter your E-mail')],
   





   [sg.Submit(), sg.Exit()]
 ]

window = sg.Window('Simple Data Entry Form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
    if event == 'Submit':
        
       df=df.append(values,ignore_index=True)
       df.to_excel('User Data.xlsx',index=False)
       window.close()
       
    
       sg.popup_yes_no('Are you aware of any flooding events in your area?')
       



       sg.popup('Is there any emergency plan prepared?', button_type= 1)


       
    

       sg.popup_timed("Thanks. Your Data has been saved. The information will be provided in your Email if there is any Flood Alert.",auto_close_duration=10
       , )
    
       
       


       