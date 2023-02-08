import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

while True:
    # Move the mouse cursor to the right
    mouse.move(5, 0)
    time.sleep(0.5)
    mouse.move(0, 5)
    time.sleep(0.5)
    mouse.move(-5, 0)
    time.sleep(0.5)
    mouse.move(0, -5)
    time.sleep(0.5)
