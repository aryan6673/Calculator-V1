
#import


import picture #import picture.py

import math
import winsound
import ctypes
from colorama import *
import os
import time
from threading import Timer





#setting

#color fix windows
init()

#coppyright

print(Fore.LIGHTCYAN_EX +'''
Welcome to calculater !

Create by aliakbartnt !

Its simple calculate !

''')

#fake proccese


time.sleep(1)
print(Fore.YELLOW +"App launching processing . . .")
print(picture.calculator_ascii)
time.sleep(3)
print(Fore.RED +"App runing")
time.sleep(1)

#Code cleaning

def cleaner_consol():
    print("\n"*5)
    
cleaner_consol()    

#app source

#Variable


dot = (Fore.LIGHTGREEN_EX +": ")
color_reset = (Fore.RESET +"")

#main source
    
def cal():
    cleaner_consol()
    #Variable
    
    awnser_1 = str((Fore.LIGHTGREEN_EX +"\n" "Awnser : ")) #It is used to beautify the code

    
    
    #1anti-bug
    try:
            #input
            a = float(input(color_reset+F"Enter num 1 "+dot+color_reset ))
             #input mathematical operations
            c = input(Fore.RESET +"What mathematical operations should be performed? (sqrt,+,-,/,*,**,//) "+dot+color_reset)
            if c in ["sqrt"]:#if user type sqrt dont get b value and do it operation
                a = float(a)
                awnser = math.sqrt(a)
                print(f'{awnser_1}{awnser}')

            else: #if not match sqrt get b input form user
                b = float(input(F"Enter num 2 "+dot+color_reset ))
                b = str(b) #change type
           
           #change type
            a = str(a)
            
          
            

     #1anti-bug
            
    except:
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        print(Fore.RED +"Please enter number"+color_reset)
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number", "Not Correct", 0 | 0x30)
        cal()
    
    #2anti-bug
    try:
        #check for c value true
        if c in ['+', '-', '*', '**', '/', '//']:
            awnser = eval(a + c + b) #eval mathematical operations 
            print(f'{awnser_1}{awnser}')

        elif c in ["sqrt"]: #its for dont bug else system
            again()  

           
            #anti-bug
        else :
            print(Fore.RED +"Undefined mathematical operations")   

    #2anti-bug        
    except: 
        print(Fore.RED +"Please enter number"+color_reset)#invalid number
        winsound.MessageBeep(winsound.MB_ICONHAND)#sound
        #message-box
        ctypes.windll.user32.MessageBoxW(0, "Please enter number", "Not Correct", 0 | 0x30)
        cal()#aggain run main code
    
        
    #if main code end ask user relaunch
    again()   



#relaunch code


def again():
    rep = str(input(Fore.LIGHTRED_EX +"\n""Relaunch calculater ? y or n "+dot+color_reset))#user awnser input
    print(Fore.RESET +"") #for color reset with awnser user
    if rep == "y" :   #check user awnser
        cal()#relaunch main code
        
        
    elif rep == "n" :   #check user awnser
        print("5 s to close")    
        def end():#start fake end time
#fake-end-time           
            print("Close now")
            time.sleep(1)
        t = Timer(5.0, exit)#after 5 s end app
        t.start() #start timer  
        
#anti-bug     
    else :
        print(Fore.LIGHTRED_EX +"incorrect value"+color_reset)
        again()
        
#call main code . at the first lunch app this code work   
cal()    
    
    
