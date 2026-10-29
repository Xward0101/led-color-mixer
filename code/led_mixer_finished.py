import tkinter as tk
from tkinter import ttk, messagebox 

def to_hex(red, green, blue):
    #Turn three numbers from 0 to 255 into a hex color code.
    return f"#{red:02X}{green:02X}{blue:02X}"
def mix():
    red = int(red_text.get())
    green = int(green_text.get())
    blue = int(blue_text.get())
    code = to_hex(red, green, blue)
    swatch.config(bg=code)
    hex_text.set(code)

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
#Green
ttk.Label(frame, text="Green (0-255):").grid(column=0, row=1, sticky=tk.E) 
ttk.Entry(frame, width=10, textvariable=green_text).grid(column=1, row=1, sticky=tk.W)
#Blue
ttk.Label(frame, text="Blue (0-255):").grid(column=0, row=2, sticky=tk.E) 
ttk.Entry(frame, width=10, textvariable=blue_text).grid(column=1, row=2, sticky=tk.W)
#HexCode
ttk.Label(frame, text="Hex code:").grid(column=0, row=4, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=hex_text, state="readonly").grid(column=1, row=4, sticky=tk.W)
#ColorSwatch
swatch = tk.Label(frame, width=20, height=6, bg="#333333", relief="sunken")
swatch.grid(column=2, row=0, rowspan=5)
#MixColorButton
ttk.Button(frame, text="Mix Color", command=mix).grid(column=0, row=3, columnspan=2)



root.mainloop()