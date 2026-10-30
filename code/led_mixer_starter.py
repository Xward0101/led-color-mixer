"""
LED Color Mixer (STARTER)

Book topic: Murach's Python Programming, 2nd ed., Chapter 18,
"How to build a GUI program," pages 511-533.

Run this file from the led-color-mixer folder:
    Windows:  python code/led_mixer_starter.py
    Mac:      python3 code/led_mixer_starter.py

Complete TODOs 1 to 3 in order and run the file after each one.
Stuck? Compare with code/led_mixer_finished.py after you have tried the step.
"""

import tkinter as tk
from tkinter import ttk, messagebox

def to_hex(red, green, blue):
    #Turn three numbers from 0 to 255 into a hex color code.
    return f"#{red:02X}{green:02X}{blue:02X}"
def mix():
    # TODO 3a: Write the callback for the Mix Color button.
    #   1. Read each box with .get() and turn it into a number with int()
    #   2. Build the hex code with to_hex() and store it in code
    #   3. Color the swatch with swatch.config(bg=code)
    #   4. Write code into the Hex code box with hex_text.set()
    pass

root = tk.Tk()
root.title("LED Color Mixer")

frame = ttk.Frame(root, padding = "10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

red_text = tk.StringVar()
green_text = tk.StringVar()
blue_text = tk.StringVar()
hex_text = tk.StringVar()

#Layout
#Red
ttk.Label(frame, text="Red (0-255):").grid(column=0, row=0, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=red_text).grid(column=1, row=0, sticky=tk.W)
# TODO 2: Add the Green row (row 1) and the Blue row (row 2).
#         Copy the two Red lines and change the label text,
#         the StringVar, and the row number.
#HexCode
ttk.Label(frame, text="Hex code:").grid(column=1, row=5, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=hex_text, state="readonly").grid(column=2, row=5, sticky=tk.W)
#ColorSwatch
swatch = tk.Label(frame, width=20, height=6, bg="#333333", relief="sunken")
swatch.grid(column=2, row=0, rowspan=5)
#MixColorButton
# TODO 3b: Add a ttk.Button that says "Mix Color" and runs mix when clicked.
#          Place it at column 0, row 3, spanning 2 columns.

# TODO 1: Start the event loop so the window appears and waits for clicks.
#         It must be the LAST line of the file.
