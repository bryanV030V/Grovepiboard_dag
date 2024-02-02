from grove_rgb_lcd import *
import random
import time

try:
    while True:
        setRGB(0, 255, 0)

        setText("Grove - LCD RGB Backlight")
        time.sleep(2)

        setText("Hello World")
        time.sleep(2)

        setText("Random colors")
        for i in range(0, 51):
            setRGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            time.sleep(0.1)
        time.sleep(1)

        # ascii char 255 is the cursor character
        setRGB(255, 255, 255)
        setText(chr(255) * 32)
        time.sleep(2)

        # typewriter
        setRGB(255, 127, 0)
        string_text = "Hello World"
        for i in range(0, 12):
            setText(string_text[:i])
            time.sleep(0.2)
        time.sleep(2)

        setRGB(255, 0, 255)
        setText("1234567890ABCDEF1234567890ABCDEF")
        time.sleep(2)

        # Add more sections of your code as needed

except KeyboardInterrupt:
    setText("KeyboardInterrupt")
    setRGB(255, 0, 0)
except IOError:
    setText("IOError")
    setRGB(255, 0, 0)

time.sleep(1)
setText("All done")
setRGB(0, 255, 0)