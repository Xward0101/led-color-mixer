# Facilitator Notes (15 minutes)

These are presenter notes for leading the LED Color Mixer activity. Classmates follow the README;
this page is the run-of-show.

## Before class

- [ ] Run `code/led_mixer_finished.py` on the presentation computer.
- [ ] Have the README open in a browser tab and the starter open in VS Code.
- [ ] Confirm the repo is public and the clone command in the README works from a fresh folder.
- [ ] Keep `docs/images/` handy as a backup if the live demo fails.

## Run of show

| Time | What happens | Say or ask |
|---|---|---|
| 0:00-2:00 | **Hook and topic.** Show the finished app. Type `255, 169, 87` (warm white) and click Mix Color, then `60, 40, 140` (movie night). | "Every smart-light app stores color as three numbers. Today you'll build the part you touch." Name the chapter: Ch. 18, pp. 511-533. |
| 2:00-4:00 | **Clone and setup check.** Everyone runs `git clone`, opens the folder, then `python -m tkinter` (Mac: `python3`). | "If a little window popped up, you're ready." |
| 4:00-5:30 | **TODO 1.** Everyone runs the starter. Nothing happens. | Ask: "Why did it just quit?" Then key idea 1: a GUI waits. Add `mainloop()`. |
| 5:30-8:00 | **TODO 2.** Add Green and Blue rows. | Point out column and row. "Grid is a spreadsheet for widgets." |
| 8:00-12:30 | **TODO 3.** Write `mix()` (3a), then the Mix Color button (3b). Test `0, 200, 255`. | Key idea 2: callbacks. Key idea 3: `.get()` reads, `.set()` writes. Point out `command=mix` has no parentheses; if anyone's app crashes on launch, that's why. |
| 12:30-13:30 | **Break it.** Everyone types `abc` and clicks Mix Color. | "What broke? Users will type anything. That's what the bonus TODO 4 fixes." |
| 13:30-15:00 | **Debrief and hand-off.** Ask a reflection question from the README and point to the bonus TODOs. | "Right now this is one long script. Page 522 shows how to organize it as a class," then hand off to the professor. |

## If time runs short

- Do TODO 2 together on screen instead of individually.
- Shorten the "break it" moment to a live demo on your screen.
- Anyone behind can compare with `code/led_mixer_finished.py`, or put the finished code on
  screen so they can copy the step the room is on.

## Debrief questions

1. What did `mainloop()` change about how the program runs?
2. Who saw their scene load at startup instead of on click? Why did that happen?
3. Where else have you seen "type, check, update" in apps you use?
