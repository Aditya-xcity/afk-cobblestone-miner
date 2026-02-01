from pynput.keyboard import Controller as KeyboardController, KeyCode
from pynput.mouse import Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()

A_KEY = KeyCode.from_char('a')

print("Starting in 3 seconds... switch to Minecraft")
time.sleep(3)

print("AFK mining started (A + scroll)")

try:
    while True:
        # keep A pressed
        keyboard.press(A_KEY)

        # scroll once
        mouse.scroll(0, -1)
        print("Scrolled once")

        time.sleep(5)

except KeyboardInterrupt:
    keyboard.release(A_KEY)
    print("\nStopped. A key released.")
