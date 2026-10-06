# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image

SHIP_OVERVIEW = 1
CROWS_NEST_1 = 2

def update_screen():
    if ship.stash.location == CROWS_NEST_1:
        ship.src(f"tests/pirate-crows-nest-1.png")
        title.text = "You see: The crows nest. There is something on the horizon!"
        option_1.text = "Crows Nest"
        option_2.style <<= "visibility: visible;"
        
    if ship.stash.location == SHIP_OVERVIEW:
        # CROWS NEST 1
        ship.src(f"tests/pirate-ship-2.png")
        title.text = "You see: Your pirate ship"
        option_1.text = "Ship Overview"
        option_2.style <<= "visibility: hidden;"


def option_1_click():

    if ship.stash.location == SHIP_OVERVIEW:
        ship.stash.location = CROWS_NEST_1
    
    elif ship.stash.location == CROWS_NEST_1:
        ship.stash.location = SHIP_OVERVIEW
    
    update_screen()


ship = Image("tests/pirate-ship-2.png")
ship.style <<= "left: 62px; top: 5px;"
ship.stash.location = SHIP_OVERVIEW

title = Label("You see: Your pirate ship")
title.style <<= "left: 62px; top: 630px; font-size: 22px; background-color: gold; padding: 5px 20px;"

option_1 = Button("Crows Nest")
option_1.style <<= "top: 670px; left: 62px;"

option_2 = Button("Option 2")
option_2.style <<= "top: 670px; left: 220px; visible: none;"



go()