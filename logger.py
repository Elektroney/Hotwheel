import settings
import datetime
import sys 
import os

if not os.path.exists('logs'):
    os.makedirs('logs')
log_file = open(".\\logs\\"+ datetime.datetime.now().strftime("%Y.%m.%d-%H-%M-%S")+ ".log","a")

def print(message):
    
    global log_file

    message =  datetime.datetime.now().strftime("\n[%H:%M:%S] ") +message 

    if settings._DEBUG_MODE:
        sys.stdout.write(str(message))
        sys.stdout.flush()
    log_file.write(str(message))