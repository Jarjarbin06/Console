#############################
###                       ###
###      Console v1.0     ###
###   ----Console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from Color import Color
from Packed import Packed

base_pack = Packed()

class Animation :

    ANIMATION = []
    ANIMATION_STEP = 0
    ANIMATION_MAX_STEP = 0

def cmd(command_line: str) -> None:
    from os import system
    system(command_line)

def log(text: str, *, start: str = "", end: str = "\n", delete=False, sleep: int | float = 0) -> None:
    from time import sleep as slp
    if delete: delete_last_line()
    print(f"{start}{text}", end=end)
    slp(sleep)

def color(text: str, color_code: tuple[str | int, str | int] = base_pack.INFO, title: str = "") -> str:
    try:
        if title == "":
            return f"{color_code[1]}{text}{Color.BASE}"
        else:
            return f"{color_code[0]}{title}{Color.BASE}{color_code[1]} : {text}{Color.BASE}"
    except any:
        if title == "":
            return f"{base_pack.ERROR[0]}ERROR{Color.BASE} : {base_pack.ERROR[1]}color code must be between 0 and 108 (current color_code is {color_code[0]}){Color.BASE}"
        else:
            return f"{base_pack.ERROR[0]}ERROR{Color.BASE} : {base_pack.ERROR[1]}color code must be between 0 and 108 (current color_code is {color_code[0]} and {color_code[1]}){Color.BASE}"

def animate(*, color_val=base_pack.VALID) -> str:
    Animation.ANIMATION_STEP += 1
    if Animation.ANIMATION_STEP > Animation.ANIMATION_MAX_STEP: Animation.ANIMATION_STEP = 0
    return color(Animation.ANIMATION[Animation.ANIMATION_STEP - 1], color_val)

def open_animation(animation: list[str]):
    Animation.ANIMATION = animation
    Animation.ANIMATION_STEP = 0
    Animation.ANIMATION_MAX_STEP = len(animation) - 1

def clear() -> None:
    from os import system
    from sys import platform

    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "win32":
        system("cls")

def delete_last_line() -> None:
    from sys import stdout
    stdout.write('\x1b[1A')
    stdout.write('\x1b[2K')

def test() -> None:
    while True:
        open_animation(base_pack.FILL_R)
        for _ in range(Animation.ANIMATION_MAX_STEP): log(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)
        open_animation(base_pack.EMPTY_R)
        for _ in range(Animation.ANIMATION_MAX_STEP): log(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)
        open_animation(base_pack.FILL_L)
        for _ in range(Animation.ANIMATION_MAX_STEP): log(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)
        open_animation(base_pack.EMPTY_L)
        for _ in range(Animation.ANIMATION_MAX_STEP): log(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)
