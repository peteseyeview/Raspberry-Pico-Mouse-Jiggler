# Raspberry-Pico-Mouse-Jiggler
 Raspberry Pi Pico Mouse Jiggler

This code is for a mouse jiggler that can run on a Raspberry Pi Pico using CircuitPython. The code uses the usb_hid and adafruit_hid.mouse libraries.

## Prerequisites

Raspberry Pi Pico
CircuitPython 8.x 
USB cable to connect the Raspberry Pi Pico to your computer
Text editor, such as Mu or VSCode
Installing Required Libraries

To use the usb_hid and adafruit_hid.mouse libraries, you need to install them on your Raspberry Pi Pico. You can do this by connecting the Pico to your computer, navigating to the lib directory and copying the required libraries to it.

## Running the Code

Connect the Raspberry Pi Pico to your computer using the USB cable.
Open your text editor and create a new file named main.py.
Copy the following code into the file and save it.
```
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
  ```
Eject the Raspberry Pi Pico from your computer.
The code will automatically run and the mouse cursor will start to move.
