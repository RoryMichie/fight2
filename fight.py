#imports
import wgsdk
#menus
def mainmenu():
    print("music fight2/sounds/menumus")
    wgsdk.menu(["set","play","extras","exit"],"fight2/sounds/move.ogg","fight2/sounds/enter.ogg")