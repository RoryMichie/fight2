#imports: this section is where the necessary libraries are imported
import wgsdk
#macros: This section is for functions which make coding things easier. Note: this is not fast! But this game doesn't need performance. So, we do it anyway. Because I don't want to type a lot of code.
def menu(menulist):#this macro calls the wgsdk.menu function, but automatically includes our click.ogg and move.ogg sounds
    return int(wgsdk.menu(menulist,"fight2/sounds/click.ogg","fight2/sounds/enter.ogg"))
#menus: this section is for all the menus of the game
def mainmenu():#that's the main menu. we can save some valuable milliseconds by checking if the music is already playing, but the backend handles it for us automatically, so why bother?
    print("music fight2/sounds/menumus")
    m=menu(["set","play","extras","exit"])
    if m==3: exitmenu()
    
def exitmenu():#This asks if we want to exit or not
    wgsdk.speak("Are you sure you want to exit?")
    if menu(["yes","no"])==1: mainmenu()
mainmenu()