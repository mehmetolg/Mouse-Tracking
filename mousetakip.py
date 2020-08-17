import win32api
import time
import os 
from tkinter import *
from tkinter import messagebox as mb
from threading import Thread
from threading import *
import winsound
import winreg as reg 

oldx=-1
oldy=-1
root = Tk()
root.withdraw()
gorunurluk=False
def main():    
    while True:
        kontrolet()
        time.sleep(900)
def kontrolet():
    global oldx,oldy,gorunurluk,th1
    x, y = win32api.GetCursorPos()
    if(oldx==-1 and oldy==-1):
        print(str(x)+","+str(y))
    elif(x==oldx and y==oldy):
        root.deiconify()
        gorunurluk=True
        th1 = Thread(target = tired)
        th1.start()
        soru = mb.askyesno('Hareketsiz Kaldı', 'Kapatıyım mı?')     
        if soru:
            root.withdraw()
            gorunurluk=False
        else:
            root.withdraw()
            gorunurluk=False
       
    oldx=x
    oldy=y
def tired():
    global gorunurluk,th1
    frequency = 2500 
    duration = 1000
    winsound.Beep(frequency, duration)
    time.sleep(15) 
    while True:
        if(gorunurluk==False):
            print('kapatmadım')
            break
        else:            
            os.system("shutdown /s /t 1")
            break
def AddToRegistry():  
    pth = os.path.dirname(os.path.realpath(__file__)) 
    s_name="mousetakip.exe"  
    address=os.path.join(pth,s_name)  
    if(os.path.exists(address)):  
        key = reg.HKEY_CURRENT_USER 
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"    
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
        reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)
        reg.CloseKey(open) 
  

if __name__ == "__main__":
    AddToRegistry()  
    main()