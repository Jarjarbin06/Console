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

    def __init__(self, *, active="#", inactive="-", border="|"):
        self.ERROR = (Color.HIGHLIGHT_DARK_RED, Color.DARK_RED)
        self.WARNING = (Color.HIGHLIGHT_DARK_YELLOW, Color.DARK_YELLOW)
        self.VALID = (Color.HIGHLIGHT_DARK_GREEN, Color.DARK_GREEN)
        self.INFO = (Color.HIGHLIGHT, Color.BASE)

        self.SLIDE_R = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{border}"]
        self.SLIDE_L = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}"]
        self.SLIDER_R = [
            f"{border}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{border}"]
        self.SLIDER_L = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}"]
        self.FILL_R = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}"]
        self.FILL_L = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}"]
        self.EMPTY_R = [
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{active}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}"]
        self.EMPTY_L = [
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{active}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}",
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}"]
        self.EMPTY = [
            f"{border}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{inactive}{border}"]
        self.FULL = [
            f"{border}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{active}{border}"]
