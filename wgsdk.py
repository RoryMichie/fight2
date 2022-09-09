# WolfGames development kit
# This is version 0.8.0.1 of the kit
# Note: Although our games are open-source, the WolfGames engine is not, for security reasons. Keep this in mind!
# We do not provide hosting for 3rd-party WolfGames projects under any circumstances as of July 2022.
# This engine, and any games using it, is licensed under the gnu general public license (gpl) version 3
def reset_edit_box():
    print("clearedit")
def reset_menu():
    print("mc")
def speak(text):
    print("speak "+text)
def menu(menulist, movesound, entersound):
    print("showmenu")
    for x in menulist:
        print("mad "+x)
    while True:
        m = input()
        m2 = m.split("|")
        if m2[0] == "menuchange":
            print("sound ./"+movesound+" 50 0")
        if m2[0] == "menu":
            print("sound ./"+entersound+" 50 0")
            print("mc")
            return m2[1]
def edit_box(typesound, entersound):
    while True:
        s = input().split("|")
        if s[0] == "editchange":
            print("sound "+typesound+" 50 0")
        if s[0] == "edit":
            print("sound "+entersound+" 50 0")
            return s[1]
def sound(name, volume=50, pan=0):
    print("sound "+name+" "+volume+" "+pan)
def wait(ticks):
    while True:
        a=input()
        if a=="timer 99":
            ticks-=1
            if ticks==0: return