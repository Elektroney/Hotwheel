




from pystray import MenuItem as item
from PyQt5.QtWidgets import QApplication
from pynput.mouse import Listener

import sys
import time
import ctypes
import pystray
import PIL.Image
import threading
import subprocess
import traceback

# Local Modules
import settings
import plugin
import UI
import logger

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
    global running 
    icon.stop()
    running = False
def on_reload(icon, item):
    global running 
    running = False
    icon.stop()
    subprocess.call("start.bat" )

def tray_icon_thread():
    image = PIL.Image.open("wheel.ico")
    systemTrayIcon = pystray.Icon("Hotring", image)

    # Create a context menu options
    menu = (item('Reload', on_reload),item('Exit', on_exit),)
    systemTrayIcon.menu = pystray.Menu(*menu)

    systemTrayIcon.run()

if __name__ == '__main__':
    try:
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
                time.sleep(0.05)
        logger.print("Exited!")
    except Exception:
        logger.print(traceback.format_exc())