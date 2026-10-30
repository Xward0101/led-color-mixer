# LED Color Mixer

Build a small desktop app that mixes red, green, and blue light into a color and shows its hex
code. Along the way you will learn how a Python GUI waits for you, listens for clicks, and talks
to the boxes on screen.

![The LED Color Mixer after TODO 3](docs/images/step3_mix.png)

## At a glance

| | |
|---|---|
| **Schedule topic** | Week 9: Murach's Python Programming, Section 4, Part B. GUI programming |
| **Textbook** | *Murach's Python Programming*, 2nd ed., Chapter 18, "How to build a GUI program," pages 511-533 |
| **Time** | About 15 minutes for TODOs 1 to 3, plus optional bonus challenges |
| **You will practice** | Root windows and the event loop, labels and entry boxes, `StringVar`, grid layout, button callbacks, and read-only fields. Bonus: message boxes |
| **Python** | 3.10 or newer. No packages to install (`tkinter` comes with Python) |

## Why this is worth learning

So far our programs run in the terminal: they ask a question, wait for typing, and print an
answer. Most software people actually use has a window instead. A GUI lets someone use your
program without knowing anything about the terminal.

This app also mirrors real tools:

- **Smart lighting apps** like Philips Hue and Govee store colors as three numbers from 0 to 255,
  one each for red, green, and blue. On a microcontroller such as an Arduino, those same three
  numbers set how bright each color of an LED strip glows.
- **Dashboards and design tools** like Power BI, Tableau, matplotlib, Canva, and CSS use **hex
  codes** (`#FFA957`) for exact colors. Companies define their brand colors this way.
- **The pattern carries over:** type values, check them, and update the screen. That same loop
  runs every form, settings panel, and dashboard filter you have ever used.

## Three key ideas

**1. A GUI program waits instead of finishing.** A console program runs from the top to the
bottom and stops. A GUI program sets up its window once, then calls `root.mainloop()`, which
shows the window and waits for things to happen, like a click. Your code only runs again when
the window "calls you back." (Figure 18-1, pages 512-513.)

**2. Callbacks connect a button to your code.** When you create a button, `command=mix` tells
it which function to run *later*, when someone clicks it. That function is called a **callback**
or **event handler**. (Figure 18-3, pages 516-517.)

**3. `StringVar` is the bridge between a box and your code.** Each entry box is bound to a
`StringVar`. Your code uses `.get()` to read what the user typed and `.set()` to write into a
box. `mix()` reads the three color boxes and writes the result into the Hex code box. (Figure 18-4, pages 518-519.)

## Before you start

1. **Python 3.10 or newer**, and **VS Code** (or any editor plus a terminal).
2. **Check that tkinter works.** In a terminal, run:

   | Windows | Mac |
   |---|---|
   | `python -m tkinter` | `python3 -m tkinter` |

   A small test window should pop up. Close it and continue. If you get an error, see
   [Troubleshooting](#troubleshooting).

## Setup

1. **Clone the repository.** Open a terminal in the folder where you keep class work, then run:

   ```text
   git clone https://github.com/Xward0101/led-color-mixer.git
   ```

   This creates a `led-color-mixer` folder with everything inside. No Git? On the repository page,
   click **Code > Download ZIP** and unzip it instead.
2. In VS Code, choose **File > Open Folder** and open the `led-color-mixer` folder.
3. Open a terminal with **Terminal > New Terminal**. It should already be in `led-color-mixer`.
4. Open `code/led_mixer_starter.py`. This is the only file you will edit.

**Run command** (use it after every TODO):

| Windows | Mac |
|---|---|
| `python code/led_mixer_starter.py` | `python3 code/led_mixer_starter.py` |

**Stuck?** The finished app is in `code/led_mixer_finished.py`. It is the starter with TODOs 1 to
3 filled in, line for line. Try each step yourself first, then use it to compare.

## The activity

**TODOs 1 to 3 are the activity.** TODOs 4 and 5 are bonus challenges for anyone who finishes
early or wants to keep going after class. Each TODO ends with a **Checkpoint** that tells you what
you should see.

### TODO 1: Make the window appear (pages 512-513)

Run the starter **before changing anything**. What happens?

Nothing. The program starts, builds the window in memory, and then exits right away. This is
the most common GUI mistake, and the book calls it out on page 512: without `mainloop()`, the
program never starts waiting for events.

Scroll to the bottom of the file and add this as the **very last line**:

```python
root.mainloop()
```

> **Checkpoint 1:** A window titled "LED Color Mixer" appears with a Red box, a dark swatch, and a
> Hex code box under the swatch. Nothing works yet.

![Checkpoint 1](docs/images/step1_window.png)

### TODO 2: Add the Green and Blue rows (pages 518-521)

Find the Red row. It is a `Label` in column 0 and an `Entry` in column 1, both in row 0:

```python
ttk.Label(frame, text="Red (0-255):").grid(column=0, row=0, sticky=tk.E)
ttk.Entry(frame, width=10, textvariable=red_text).grid(column=1, row=0, sticky=tk.W)
```

Copy it twice, right below, for **Green in row 1** and **Blue in row 2**. Change three things each
time: the label text, the `StringVar` (`green_text`, `blue_text`), and the row number.

> **Checkpoint 2:** Three labeled boxes, lined up in a column beside the swatch.

![Checkpoint 2](docs/images/step2_layout.png)

### TODO 3: Make Mix Color work (pages 516-519)

This TODO has two parts: the function that does the work, and the button that runs it.

**TODO 3a: write `mix()`.** Find `mix()` near the top and replace `pass` with code that does four
things:

1. Read each box with `.get()` and turn the text into a number with `int()`
2. Build the hex code with `to_hex()`
3. Color the swatch
4. Write the hex code into the Hex code box

```python
red = int(red_text.get())
green = int(green_text.get())
blue = int(blue_text.get())
code = to_hex(red, green, blue)
swatch.config(bg=code)
hex_text.set(code)
```

**TODO 3b: add the button.** Find TODO 3b and add a Mix Color button that runs `mix` when clicked:

```python
ttk.Button(frame, text="Mix Color", command=mix).grid(column=0, row=3, columnspan=2)
```

Three things are new here:

- `command=mix` connects the button to your callback. **No parentheses** (see
  [Common mistake](#common-mistake-parentheses-after-a-callback)).
- `swatch.config(bg=code)` changes a widget **after** it was created. The book does not cover
  `config()`, but it works on almost every widget.
- The swatch is a `tk.Label`, not a `ttk.Label`. On Mac, `ttk` widgets ignore background colors,
  so the plain `tk` version is used for anything that needs to change color.

> **Checkpoint 3:** Type `0`, `200`, `255` and click Mix Color. The swatch turns sky blue and the
> Hex code box shows `#00C8FF`. Try a few colors of your own.

![Checkpoint 3](docs/images/step3_mix.png)

**Now try to break it.** Type `abc` in the Red box and click Mix Color. A red error appears in
the terminal (`ValueError`), and the color does not change. Users will type anything, so we need
to catch that. That is where the bonus challenges pick up.

## Bonus challenges (on your own)

Finished early, or want to keep going after class? These have no starter code. Write them in your
own copy of the file.

### TODO 4 (bonus): Catch bad input with message boxes (pages 524-529)

Write a function named `get_channel(text, name)` above `mix()` that:

1. **Tries** to turn `text` into an `int`
2. If that raises a `ValueError`, shows an error box and returns `None`
3. If the number is below 0 or above 255, shows an error box and returns `None`
4. Otherwise returns the number

Then change `mix()` to call `get_channel()` instead of `int()`, and stop early with `return` if
any value came back as `None`.

**Hints:** the book's `get_int()` method on page 529 uses the same try/except pattern. The error
box is `messagebox.showerror(title, message)` on page 525. An f-string lets the message name the
box: `f"{name} must be a whole number."`

> **Checkpoint 4:** Type `300` in Red and click Mix Color. A pop-up says
> "Red must be from 0 to 255." Click OK. The color has not changed, and your typing is still
> there so you can fix it. Also try `abc`, `-1`, `12.5`, and an empty box.

![Checkpoint 4: the error box](docs/images/error_box.png)

<details>
<summary>Example answer (try it yourself first)</summary>

```python
def get_channel(text, name):
    try:
        value = int(text)
    except ValueError:
        messagebox.showerror("Invalid value", f"{name} must be a whole number.")
        return None
    if value < 0 or value > 255:
        messagebox.showerror("Out of range", f"{name} must be from 0 to 255.")
        return None
    return value
```

The first three lines of `mix()` become:

```python
red = get_channel(red_text.get(), "Red")
green = get_channel(green_text.get(), "Green")
blue = get_channel(blue_text.get(), "Blue")
if red is None or green is None or blue is None:
    return
```
</details>

### TODO 5 (bonus): Add a preset color button

Smart-light apps let you save a favorite color and load it with one tap. Add one preset of your
own: your room's lighting, a favorite team's color, anything.

You need two things:

1. **A function** that fills the three boxes with `.set()` and then calls `mix()`
2. **A button** whose `command=` names your function. Row 4, columns 0 and 1, is open, right below
   Mix Color

Need ideas? Warm White `(255, 169, 87)`, Movie Night `(60, 40, 140)`, Sunset `(255, 94, 77)`,
Ocean `(0, 180, 200)`.

> **Checkpoint 5:** Your button appears under Mix Color. Clicking it fills the three boxes by
> itself and the swatch changes to your color. Movie Night gives `#3C288C`.

<details>
<summary>Example answer (try it yourself first)</summary>

```python
def movie_night():
    red_text.set("60")
    green_text.set("40")
    blue_text.set("140")
    mix()
```

```python
ttk.Button(frame, text="Movie Night", command=movie_night).grid(column=0, row=4, columnspan=2)
```
</details>

## Common mistake: parentheses after a callback

```python
ttk.Button(frame, text="Mix Color", command=mix())   # wrong
ttk.Button(frame, text="Mix Color", command=mix)     # right
```

With parentheses, Python **runs** `mix()` immediately, once, while it builds the window. The boxes
are still empty, so `int("")` crashes and the app never opens. The terminal shows
`ValueError: invalid literal for int() with base 10: ''`. Without parentheses, you hand the button
the **function itself** to run later, when it is clicked.

A related mistake from TODO 1: any code placed **after** `root.mainloop()` will not run until the
window closes. Keep `mainloop()` as the last line.

## Check your understanding

Try to answer before opening each one.

<details>
<summary>1. You ran the starter and nothing appeared. Why, and what fixed it?</summary>

There was no `root.mainloop()`. Without the event loop, the program builds the window and exits.
Adding `mainloop()` as the last line shows the window and keeps it open, waiting for events.
</details>

<details>
<summary>2. What is the difference between <code>red_text.get()</code> and <code>red_text.set("255")</code>?</summary>

`.get()` reads whatever is in the Red box. `.set("255")` writes `255` into the box. `mix()` does
both: it reads the three color boxes and writes into the Hex code box.
</details>

<details>
<summary>3. You added the Mix Color button and now the app crashes before the window opens, with a <code>ValueError</code> about <code>''</code>. What happened?</summary>

The button was created with `command=mix()` instead of `command=mix`. The parentheses ran `mix()`
while the window was being built, when the boxes were still empty, and `int("")` crashed.
</details>

<details>
<summary>4. (Bonus) Why does <code>mix()</code> <code>return</code> early when a value is <code>None</code>?</summary>

`None` means that box failed validation and the user already saw an error box. Returning stops
`to_hex()` from crashing and leaves the old color on screen.
</details>

## Connections

- **Activity 4, Week 9 (Party Roster):** the same pattern, with a database behind it. Read the
  boxes in a callback, validate, then update what the window shows.
- **Homework 18-2 (MPG program):** uses the same tools. Labels and entries in a grid, a Calculate
  callback, a read-only result field, and a `get_float()` method like `get_channel()`.
- **What comes next in the book:** page 522 shows how to organize a GUI as a class that inherits
  `ttk.Frame`. Try turning this app into a `MixerFrame` class.

## Reflection

Take one minute and answer: **What is one thing about how a GUI program runs that is different
from the console programs we wrote earlier in the course?** And: **Where else have you seen this
"type, check, update" pattern in apps you use?**

## Troubleshooting

| What you see | What to try |
|---|---|
| The program ends immediately with no window | Add `root.mainloop()` as the last line (TODO 1). |
| `python` is not recognized (Windows) | Try `py code/led_mixer_starter.py`. |
| `python: command not found` (Mac) | Use `python3` instead of `python`. |
| `No module named '_tkinter'` (Mac, Homebrew Python) | Run `brew install python-tk`, or install Python from python.org, which includes tkinter. Do not run `pip install tkinter`. |
| A button does nothing | Check that its `command=` names the right function with **no parentheses**, and look for a red error in the terminal. |
| The swatch stays gray on Mac | Make sure the swatch is `tk.Label`, not `ttk.Label`. |
| `NameError` mentioning a variable | Check spelling. `green_text` and `greentext` are different names. |
| `IndentationError` | The lines inside a function must be indented the same amount (4 spaces). |

## Project structure

```text
led-color-mixer/
|-- README.md                       this guide
|-- .gitignore
|-- code/
|   |-- led_mixer_starter.py        the file you edit
|   `-- led_mixer_finished.py       finished TODOs 1 to 3, for comparing
`-- docs/
    |-- facilitator_notes.md        presenter run-of-show
    |-- peer_test_log.md            results from peer testing
    `-- images/                     expected-output screenshots
```

## Known limitations

- The app shows colors on screen only. It does not connect to real lights. Controlling an actual
  LED strip would need hardware and a library for Bluetooth or a serial connection.
- The finished file covers TODOs 1 to 3. The bonus TODOs have no answer file; this README shows
  an example answer for each.
- There is no padding between widgets, so labels sit right against their boxes. The padding loop on
  page 521 of the book would add space.
- Presets live in the code, so a new preset means a new function and button. Saving presets to a
  file would be a natural next step.
- Screenshots were taken on Linux. Buttons and boxes look a little different on Windows and Mac,
  but the layout and behavior are the same.

## Sources and AI use

- **Textbook:** Urban, M., & Murach, J. (2021). *Murach's Python Programming* (2nd ed.). Mike
  Murach & Associates. Chapter 18, pages 511-533. The window setup, grid layout, and validation
  pattern follow figures 18-1 through 18-8.
- **Course materials:** activity structure and README style were informed by the course's
  Activity 4 (Party Roster) materials.
- **Color values:** the preset colors are approximations chosen for this activity, not
  manufacturer specifications.
- **AI assistance:** I used Claude (Anthropic) to brainstorm activity ideas, draft the starter
  file and this README, and coach me with hints while I wrote `led_mixer_finished.py` myself.
  I verified the code against Chapter 18 and by running it after every step, and checked that
  each checkpoint produces the result and hex code shown. Peer testing results and the changes I made afterward are in
  [docs/peer_test_log.md](docs/peer_test_log.md).
