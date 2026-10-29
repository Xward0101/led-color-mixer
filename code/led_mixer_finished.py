import tkinter as tk
from tkinter import ttk, messagebox 


root = tk.Tk()
root.title("LED Color Mixer")

frame = ttk.Frame(root, padding = "10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

red_text = tk.StringVar()
green_text = tk.StringVar()
blue_text = tk.StringVar()
hex_text = tk.StringVar()
#Red
ttk.Label(frame, text="Red (0-255):").grid(column=0, row=0, sticky=tk.E) 
ttk.Entry(frame, width=10, textvariable=red_text).grid(column=1, row=0, sticky=tk.W)
#Green
ttk.Label(frame, text="Green (0-255):").grid(column=0, row=1, sticky=tk.E) 
ttk.Entry(frame, width=10, textvariable=green_text).grid(column=1, row=1, sticky=tk.W)
#Blue
ttk.Label(frame, text="Blue (0-255):").grid(column=0, row=2, sticky=tk.E) 
ttk.Entry(frame, width=10, textvariable=blue_text).grid(column=1, row=2, sticky=tk.W)


root.mainloop()