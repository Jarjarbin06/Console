#############################
###                       ###
###      Console v1.0     ###
###   ----Packed.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from Color import Color

class Packed:

    def __init__(self, *, on="#", off="-", border="|"):

        self.ERROR = (Color.HIGHLIGHT_DARK_RED, Color.DARK_RED)
        self.WARNING = (Color.HIGHLIGHT_DARK_YELLOW, Color.DARK_YELLOW)
        self.VALID = (Color.HIGHLIGHT_DARK_GREEN, Color.DARK_GREEN)
        self.INFO = (Color.HIGHLIGHT, Color.BASE)

        self.SLIDE_R = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{border}"]

        self.SLIDE_L = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}"]

        self.SLIDER_R = [
            f"{border}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{border}"]

        self.SLIDER_L = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}"]

        self.FILL_R = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}"]

        self.FILL_L = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}"]

        self.EMPTY_R = [
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}"]

        self.EMPTY_L = [
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}",
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}"]

        self.EMPTY = [
            f"{border}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{border}"]

        self.FULL = [
            f"{border}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{border}"]
