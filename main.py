import sys
import datetime
import os

if not os.path.exists('logs'):
    os.makedirs('logs')
log_file = open(".\\logs\\"+ datetime.datetime.now().strftime("%Y.%m.%d-%H-%M-%S")+ ".log","a")
sys.stdout = log_file
sys.stderr = log_file


from pystray import MenuItem as item
from PyQt5.QtWidgets import QApplication
from pynput.mouse import Listener

import ctypes
import pystray
import PIL.Image
import threading
import subprocess


# Local Modules
import settings
import plugin
import UI

mouseButtonIsHeld = False
running = True


def on_click(x, y, button, pressed):
    global mouseButtonIsHeld
    if str(button) != settings._ACTIVATION_MOUSE_BUTTON:
        return
    mouseButtonIsHeld = pressed

def check_activation_key():
    return ctypes.windll.user32.GetKeyState(settings._ACTIVATION_KEY) & 0x8000 != 0

def on_exit(icon, item):
    icon.stop()
    os._exit(1)
def on_reload(icon, item):
    global running 
    running = False
    icon.stop()
    subprocess.call("python main.py" )

def tray_icon_thread():
    image = PIL.Image.open("wheel.ico")
    systemTrayIcon = pystray.Icon("Hotring", image)

    # Create a context menu options
    menu = (item('Reload', on_reload),item('Exit', on_exit),)
    systemTrayIcon.menu = pystray.Menu(*menu)

    systemTrayIcon.run()

if __name__ == '__main__':
    plugin.LoadPlugins()
    app = QApplication(sys.argv)
    window = UI.UI()


    tray_thread = threading.Thread(target=tray_icon_thread, daemon=True)
    tray_thread.start()

    with Listener(on_click=on_click) as listener:
        while running:
            if check_activation_key() or mouseButtonIsHeld:
                window.show()
            else:
                window.hide()

            app.processEvents()

