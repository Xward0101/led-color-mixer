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
| 0:00-2:00 | **Hook and topic.** Show the finished app. Click Warm White, then Movie Night. | "Every smart-light app stores color as three numbers. Today you'll build the part you touch." Name the chapter: Ch. 18, pp. 511-533. |
| 2:00-3:00 | **Clone and setup check.** Everyone runs `git clone`, opens the folder, then `python -m tkinter` (Mac: `python3`). | "If a little window popped up, you're ready." |
| 3:00-4:30 | **TODO 1.** Everyone runs the starter. Nothing happens. | Ask: "Why did it just quit?" Then key idea 1: a GUI waits. Add `mainloop()`. |
| 4:30-6:30 | **TODO 2.** Add Green and Blue rows. | Point out column and row. "Grid is a spreadsheet for widgets." |
| 6:30-9:30 | **TODO 3.** Write `mix()`, connect `command=mix`. | Key idea 2: callbacks. Key idea 3: `.get()` reads, `.set()` writes. Then: "Type abc. What broke?" |
| 9:30-11:30 | **TODO 4.** Error boxes. | "Users will type anything. Never trust a box." |
| 11:30-14:00 | **TODO 5.** Everyone adds their own scene. | Walk the room. Look for `command=my_scene()`; if you see it, show it on screen as the common mistake. |
| 14:00-15:00 | **Debrief and hand-off.** Ask a reflection question from the README. | "Right now this is one long script. Page 522 shows how to organize it as a class," then hand off to the professor. |

## If time runs short

- Skip the "try to break it" moment in TODO 3 and go straight to TODO 4.
- Do TODO 5 together on screen instead of individually.
- Anyone behind can compare with `code/led_mixer_finished.py`, or put the finished code on
  screen so they can copy the step the room is on.

## Debrief questions

1. What did `mainloop()` change about how the program runs?
2. Who saw their scene load at startup instead of on click? Why did that happen?
3. Where else have you seen "type, check, update" in apps you use?
