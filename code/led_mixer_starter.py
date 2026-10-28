"""
LED Color Mixer (STARTER)

Book topic: Murach's Python Programming, 2nd ed., Chapter 18,
"How to build a GUI program," pages 511-533.

Run this file from the led-color-mixer folder:
    Windows:  python code/led_mixer_starter.py
    Mac:      python3 code/led_mixer_starter.py

Complete the TODOs in order (1 through 5) and run the file after each one.
Stuck? Compare with code/led_mixer_finished.py after you have tried the step.
"""

import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------------------------------------------------
# Helper (already done for you)
# ----------------------------------------------------------------------

def to_hex(red, green, blue):
    """Turn three numbers from 0 to 255 into a hex color code.

    Example: to_hex(255, 169, 87) returns "#FFA957".
    The 02X format means "two characters, uppercase hexadecimal,"
    so 255 becomes FF and 0 becomes 00.
    """
    return f"#{red:02X}{green:02X}{blue:02X}"


def get_channel(text, name):
    """Convert one box's text into a whole number from 0 to 255.

    Returns the number if it is valid. Returns None if it is not.
    This follows the get_int() method in figure 18-8 (page 529).
    """
    try:
        value = int(text)
    except ValueError:
        # TODO 4a: Show an error box, for example:
        #   messagebox.showerror("Invalid value", f"{name} must be a whole number.")
        return None

    if value < 0 or value > 255:
        # TODO 4b: Show an error box that says the value must be 0 to 255.
        return None

    return value


# ----------------------------------------------------------------------
# Callbacks: functions the window runs when a button is clicked
# ----------------------------------------------------------------------

def mix():
    """Callback for the Mix Color button."""
    # TODO 3: Make the Mix Color button work.
    #   1. Read each box with .get() and convert it with int().
    #        red = int(red_text.get())
    #   2. Build the code:            code = to_hex(red, green, blue)
    #   3. Color the swatch:          swatch.config(bg=code)
    #   4. Show the code in the box:  hex_text.set(code)
    # Then scroll down and connect the button with command=mix
    pass


def load_scene(red, green, blue):
    """Put a scene's numbers into the three boxes, then mix them."""
    red_text.set(str(red))      # .set() writes INTO a box
    green_text.set(str(green))
    blue_text.set(str(blue))
    mix()


def warm_white():
    load_scene(255, 169, 87)


def movie_night():
    load_scene(60, 40, 140)


# TODO 5a: Add your own scene function here. Copy the pattern above:
#   def your_scene_name():
#       load_scene(R, G, B)


# ----------------------------------------------------------------------
# Build the window (this runs once, from top to bottom)
# ----------------------------------------------------------------------

root = tk.Tk()
root.title("LED Color Mixer")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# StringVar objects connect each entry box to our code (figure 18-4)
red_text = tk.StringVar()
green_text = tk.StringVar()
blue_text = tk.StringVar()
hex_text = tk.StringVar()

# Row 0: Red
ttk.Label(frame, text="Red (0-255):").grid(column=0, row=0, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=red_text).grid(
    column=1, row=0, sticky=tk.W)

# TODO 2: Add the Green row (row 1) and the Blue row (row 2).
#         Copy the Red row above and change three things:
#         the label text, the StringVar, and the row number.

# Row 3: the Mix Color button
# TODO 3 (continued): connect the button by adding command=mix
#         Careful: mix with NO parentheses.
ttk.Button(frame, text="Mix Color").grid(column=0, row=3, columnspan=2)

# Row 4: read-only box that shows the hex code
ttk.Label(frame, text="Hex code:").grid(column=0, row=4, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=hex_text, state="readonly").grid(
    column=1, row=4, sticky=tk.W)

# The color swatch. This is tk.Label, NOT ttk.Label, because ttk widgets
# ignore background colors on Mac.
swatch = tk.Label(frame, width=20, height=6, bg="#333333", relief="sunken")
swatch.grid(column=2, row=0, rowspan=5)

# Row 5: scene buttons, grouped in their own frame (like figure 18-8)
scene_frame = ttk.Frame(frame)
scene_frame.grid(column=0, row=5, columnspan=3)

ttk.Button(scene_frame, text="Warm White", command=warm_white).grid(
    column=0, row=0)
ttk.Button(scene_frame, text="Movie Night", command=movie_night).grid(
    column=1, row=0)

# TODO 5b: Add a button for your scene in column 2 of scene_frame.

# Add the same padding around every component in the frame (figure 18-5)
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=4)

# TODO 1: Start the event loop so the window appears and waits for clicks.
#         It must be the LAST line. Code after it will not run until
#         the window closes.
