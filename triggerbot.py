import time
import keyboard
import ctypes

delay = float(input("Please enter the trigger delay: "))

# Get screen size
user32 = ctypes.windll.user32
x, y = user32.GetSystemMetrics(0) // 2, user32.GetSystemMetrics(1) // 2


def mousedown():
    ctypes.windll.user32.mouse_event(0x0002, x, y, 0, 0)
def mouseup():
    ctypes.windll.user32.mouse_event(0x0004, x, y, 0, 0)

firing = False

while not keyboard.is_pressed("`"):
    if ctypes.windll.gdi32.GetPixel(ctypes.windll.user32.GetDC(0), x, y) == 0xFF:
        if not firing:
            mousedown()
            firing = True
    else:
        if firing:
            mouseup()
            firing = False

    time.sleep(0.01)