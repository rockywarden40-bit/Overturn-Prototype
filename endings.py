# This file is responsible for saving the endings the player has achieved in a text file.

import os
import sys


def save_ending(ending_name):
    # Get correct path (same folder as this file)
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(__file__)

    file_path = os.path.join(base_path, "endings.txt")

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except:
        lines = []

    found = False
    new_lines = []

    for line in lines:
        if ending_name in line:
            count = int(line.split("(")[1].split("x")[0])
            count += 1
            new_lines.append(f"{ending_name} ({count}x)\n")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{ending_name} (1x)\n")

    with open(file_path, "w") as f:
        f.writelines(new_lines)
