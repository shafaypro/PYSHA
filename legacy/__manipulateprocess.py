import os
import time
def close_program(input_string):
    if input_string == "window media player":
        try:
            os.system("TASKKILL /F /IM wmplayer.exe")
        except Exception as E:
            print("Exception occured a ",E) # printing the exception

    elif input_string == "note pad" or input_string == "notepad":
        try:
            os.system("TASKKILL /F /IM notepad.exe")
        except Exception as E:
            print("Exception occured a ",E) # printing the exception
    elif input_string =="calculator":
        try:
            os.system("TASKKILL /F /IM calc.exe") # Closing the program forecefully
        except Excpetion as E:
            print(E)
def start_program(input_string):
    if input_string =="notepad" or input_string =="note pad":
        try:
            os.startfile("notepad.exe")
        except Exception as E:
            print("Exception occured a ",E) # printing the exception
    elif input_string == "calculator":
            try:
                os.startfile("calc.exe")
            except Exception as E:
                print("Exception occured a ",E) # printing the exception


#close_program("window media player") # Debugging for the notepad program
start_program("calculator")
time.sleep(10)
close_program("calculator")
