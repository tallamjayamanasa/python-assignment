import time
import os

name = "LILLY GRACE"

# Colors
colors = [
    "\033[91m",  # Red
    "\033[95m",  # Magenta
    "\033[93m",  # Yellow
    "\033[96m",  # Cyan
    "\033[92m"   # Green
]

# Heart pattern
heart = [
    "   ♥♥♥     ♥♥♥   ",
    " ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ ",
    "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥",
    "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥",
    " ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ",
    "  ♥♥♥♥♥♥♥♥♥♥♥♥♥  ",
    "   ♥♥♥♥♥♥♥♥♥♥♥   ",
    "    ♥♥♥♥♥♥♥♥♥    ",
    "     ♥♥♥♥♥♥♥     ",
    "      ♥♥♥♥♥      ",
    "       ♥♥♥       ",
    "        ♥        "
]

# Animation
for i in range(20):
    os.system("cls" if os.name == "nt" else "clear")

    color = colors[i % len(colors)]

    print("\n")

    for line in heart:
        print(" " * 10 + color + line + "\033[0m")

    print("\n" + " " * 13 + color + "♥ " + name + " ♥" + "\033[0m")

    time.sleep(0.2)