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
import importlib
import os
import keyboard
from evdev import InputDevice, categorize, ecodes
# Local Modules
import settings
import plugin
import UI
import logger

mouseButtonIsHeld = False
running = True
linuxEventPath = '/dev/input/event8'

def on_click(x, y, button, pressed):
    global mouseButtonIsHeld
    if str(button) != settings._ACTIVATION_MOUSE_BUTTON:
        return
    mouseButtonIsHeld = pressed

def check_activation_key():
    if os.name == "win":
        return ctypes.windll.user32.GetKeyState(settings._ACTIVATION_KEY_WIN) & 0x8000 != 0
    elif os.name == "posix":
        return keyboard.is_pressed(settings._ACTIVATION_KEY_LINUX)
    return False

def on_exit(icon, item):
    global running 
    icon.stop()
    running = False

def on_reload(icon, item):
    global running 
    running = False
    icon.stop()
    subprocess.call("start.bat")

def tray_icon_thread():
    image = PIL.Image.open("wheel.ico")
    systemTrayIcon = pystray.Icon("Hotring", image)
    # Create context menu options
    menu = (item('Reload', on_reload), item('Exit', on_exit),)
    systemTrayIcon.menu = pystray.Menu(*menu)
    systemTrayIcon.run()

if __name__ == '__main__':
    try:
        plugin.LoadPlugins()
        app = QApplication(sys.argv)
        window = UI.UI()
        
        tray_thread = threading.Thread(target=tray_icon_thread, daemon=True)
        tray_thread.start()
        
        if os.name == "win":
            with Listener(on_click=on_click) as listener:
                while running:
                    if plugin.needReinit():
                        importlib.reload(UI)
                        window = UI.UI()
                        stageReinitalization = False
                        logger.print("Reinitialized UI!")
                    if check_activation_key() or mouseButtonIsHeld:
                        window.show()
                    else:
                        window.hide()
                    app.processEvents()
                    time.sleep(0.05)
                    
        elif os.name == "posix":
            try:
                device = InputDevice(linuxEventPath)
                # Removed the device.grab() line to allow normal mouse operation
                
                while running:
                    try:
                        for event in device.read():
                            if event.type == ecodes.EV_KEY:
                                key_event = categorize(event)
                                # Check if it's the mouse button we're interested in
                                # You'll need to adjust the key_event.keycode check based on your mouse button

                                if str( key_event.keycode) == settings._ACTIVATION_MOUSE_EVENT_LINUX:
                                    mouseButtonIsHeld = key_event.keystate == key_event.key_down
                    except BlockingIOError:
                        pass
                    
                    if mouseButtonIsHeld or check_activation_key():
                        window.show()
                    else:
                        window.hide()
                        
                    if plugin.needReinit():
                        importlib.reload(UI)
                        window = UI.UI()
                        stageReinitalization = False
                        logger.print("Reinitialized UI!")
                    
                    app.processEvents()
                    time.sleep(0.05)
                    
            except PermissionError:
                logger.print("Permission denied accessing input device. Try running with sudo.")
            except OSError as e:
                logger.print(f"Error accessing input device: {e}")
            finally:
                if 'device' in locals():
                    device.close()
                    
        logger.print("Exited!")
    except Exception:
        logger.print(traceback.format_exc())
