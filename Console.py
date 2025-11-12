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

BASE_PACK = Packed()


class Animation:
    """
        Animation class.

        Attributes:
            ANIMATION (list[str]): list of all steps of the animation.
            ANIMATION_STEP (int): current step of the animation.
            ANIMATION_LENGTH (int): last step of the animation.
    """


    def __init__(
            self,
            animation: list[str]
        ) -> None:
        """
            Open an animation.

            Args:
                animation (list[str]): list of all steps of the animation.
        """

        self.ANIMATION : list[str] = animation
        self.ANIMATION_STEP : int = 0
        self.ANIMATION_LENGTH : int = len(animation) - 1


    def animate(
            self,
            color_val: tuple[str, str] = BASE_PACK.VALID
        ) -> str:
        """
            Go to the next step of the animation and return it.

            Args:
                color_val (tuple[str, str])(optional): color value.
        """

        self.ANIMATION_STEP += 1

        if self.ANIMATION_STEP > self.ANIMATION_LENGTH: self.ANIMATION_STEP = 0

        return color(self.ANIMATION[self.ANIMATION_STEP - 1], color_code = color_val)


    def reset(
            self
        ) -> None:
        """
            Reset the animation back to first step.
        """

        self.ANIMATION_STEP = 0


class Action:
    """
        Action class.
    """

    @staticmethod
    def command(
            command_line: str
        ) -> None:
        """
            Execute a command in the shell.

            Args:
                command_line (str): command to execute.
        """

        system(command_line)


    @staticmethod
    def clear(
        ) -> None:
        """
            clear the console
        """

        if platform == "linux" or platform == "linux2":
            system("clear")

        elif platform == "win32":
            system("cls")


    @staticmethod
    def delete_last_line(
        ) -> None:
        """
            delete the last line of the console
        """

        stdout.write('\x1b[1A')
        stdout.write('\x1b[2K')


    @staticmethod
    def line_up(
        ):
        """
            bring next print to the previous line
        """

        stdout.write('\033[1A')


def show(
        text: str,
        *,
        start: str = "",
        end: str = "\n",
        delete: bool = False,
        sleep: int | float = 0
    ) -> None:
    """
        Show a text on the console.

        Args:
            text (str): text to show.

            start (str)(optional): starting character
            end (str)(optional): ending character
            delete (bool)(optional): delete last line
            sleep (int)(optional): sleep time
    """

    if delete: Action.delete_last_line()

    print(f"{start}{text}", end=end)
    slp(sleep)


def color(
        text: str,

        *,
        color_code: tuple[str, str] = BASE_PACK.INFO,
        title: str = ""
    ) -> str:
    """
        Put color on a text and return it.

        Args:
            text (str): text to show.

            color_code (tuple[str, str])(optional): color code.
            title (str)(optional): title of the text.

        Returns:
            str: colored text.
    """

    if title == "":
        return f"{color_code[1]}{text}{Color.BASE}"
    else:
        return f"{color_code[0]}{title}{Color.BASE}{color_code[1]} : {text}{Color.BASE}"


if __name__ == "__main__":

    #########################################
    ## initialize the different animations ##
    #########################################
    anim1 : Animation = Animation(BASE_PACK.FILL_R) #fill from left to right
    anim2 : Animation = Animation(BASE_PACK.EMPTY_R) #empty from left to right
    anim3 : Animation = Animation(BASE_PACK.FILL_L) #fill from right to left
    anim4 : Animation = Animation(BASE_PACK.EMPTY_L) #empty from right to left

    ########################
    ## animation the loop ##
    ########################
    while True: # animation loop

        #####################
        ## first animation ##
        #####################
        for _ in range(anim1.ANIMATION_LENGTH):
            show(
                anim1.animate() + " <=> " + color(
                    "This is a test",
                    color_code=BASE_PACK.VALID,
                    title="TEST"),
                delete = True,
                sleep = 0.05
            )
        anim1.reset() #reset the animation's step back to zero

        ######################
        ## second animation ##
        ######################
        for _ in range(anim2.ANIMATION_LENGTH):
            show(
                anim2.animate() + " <=> " + color(
                    "This is a test",
                    color_code=BASE_PACK.VALID,
                    title="TEST"),
                delete = True,
                sleep = 0.05
            )
        anim2.reset() #reset the animation's step back to zero

        #####################
        ## third animation ##
        #####################
        for _ in range(anim3.ANIMATION_LENGTH):
            show(
                anim3.animate() + " <=> " + color(
                    "This is a test",
                    color_code=BASE_PACK.VALID,
                    title="TEST"),
                delete = True,
                sleep = 0.05
            )
        anim3.reset() #reset the animation's step back to zero

        ######################
        ## fourth animation ##
        ######################
        for _ in range(anim4.ANIMATION_LENGTH):
            show(
                anim4.animate() + " <=> " + color(
                    "This is a test",
                    color_code=BASE_PACK.VALID,
                    title="TEST"),
                delete = True,
                sleep = 0.05
            )
        anim4.reset() #reset the animation's step back to zero
