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
from os import system
from sys import stdout, platform
from time import sleep as slp

base_pack = Packed()


class Animation:
    """
    Animation class contains variable used by animate() and open_animation()
    """

    ANIMATION: list[str] = []
    ANIMATION_STEP: int = 0
    ANIMATION_MAX_STEP: int = 0


def command(
        command_line: str
) -> None:
    """
    execute a command in the shell

    Parameters
        command_line {str} -- command to execute
    """

    system(command_line)


def show(
        text: str,
        *,
        start: str = "",
        end: str = "\n",
        delete: bool = False,
        sleep: int | float = 0
) -> None:
    """
    show a text on the console

    Parameters
        text {str} -- text to show

        (optional)
        start {str} -- start character
        end {str} -- end character
        delete {bool} -- delete last line
        sleep {int} -- sleep time
    """

    if delete: delete_last_line()

    print(f"{start}{text}", end=end)
    slp(sleep)


def color(
        text: str,
        color_code: tuple[str, str] = base_pack.INFO,
        title: str = ""
) -> str:
    """
    put color on a text and return it

    Parameters
        text {str} -- text to show
        color_code {tuple[str, str]} -- color code
        title {str} -- title

    Returns
        str -- color
    """

    if title == "":
        return f"{color_code[1]}{text}{Color.BASE}"
    else:
        return f"{color_code[0]}{title}{Color.BASE}{color_code[1]} : {text}{Color.BASE}"


def open_animation(
        animation: list[str]
):
    """
    open an animation on the console

    Parameters
        animation {list[str]} -- animation list
    """
    
    Animation.ANIMATION = animation
    Animation.ANIMATION_STEP = 0
    Animation.ANIMATION_MAX_STEP = len(animation) - 1


def animate(
        *,
        color_val : tuple[str, str] =base_pack.VALID
) -> str:
    """pass to the next step of the animation and return it
    Parameters
        (optional)
        color_val {tuple[str, str]} -- color value
    """

    Animation.ANIMATION_STEP += 1

    if Animation.ANIMATION_STEP > Animation.ANIMATION_MAX_STEP: Animation.ANIMATION_STEP = 0

    return color(Animation.ANIMATION[Animation.ANIMATION_STEP - 1], color_val)


def clear(
) -> None:
    """
    clear the console
    """

    if platform == "linux" or platform == "linux2": system("clear")

    elif platform == "win32": system("cls")


def delete_last_line(
) -> None:
    """
    delete the last line of the console
    """

    stdout.write('\x1b[1A')
    stdout.write('\x1b[2K')

if __name__ == "__main__":

    while True:

        open_animation(base_pack.FILL_R)
        for _ in range(Animation.ANIMATION_MAX_STEP): show(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)

        open_animation(base_pack.EMPTY_R)
        for _ in range(Animation.ANIMATION_MAX_STEP): show(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)

        open_animation(base_pack.FILL_L)
        for _ in range(Animation.ANIMATION_MAX_STEP): show(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)

        open_animation(base_pack.EMPTY_L)
        for _ in range(Animation.ANIMATION_MAX_STEP): show(
            animate() + " <=> " + color("This is a test", base_pack.VALID, "TEST"),
            delete=True, sleep=0.05)
