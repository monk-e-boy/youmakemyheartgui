# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image

SHIP_OVERVIEW = 1
CROWS_NEST = 2
CROWS_NEST_LEFT =3
CROWS_NEST_RIGHT = 4
ST_MICHAELS = 5
ST_MICHAELS_2 = 6

def update_screen():
    if ship.stash.location == ST_MICHAELS_2:
        ship.src(f"tests/pirate-tender-towards.png")
        title.text = "DEATH - YOU ARE EATEN by a 🦈"
        options.text = "Exits: heaven, hell"

    if ship.stash.location == ST_MICHAELS:
        ship.src(f"tests/pirate-island-st-michael-anchor.png")
        title.text = "You see: An island. There is a whisp of smoke."
        options.text = "Exits: set sail, row to island"

    if ship.stash.location == CROWS_NEST:
        ship.src(f"tests/pirate-crows-nest-1.png")
        title.text = "You see: The crows nest. There is something on the horizon!"
        options.text = "Exits: down, left, right"
        # tell the ship the user has seen the enemy!!
        ship.stash.seen_island = True

    if ship.stash.location == CROWS_NEST_LEFT:
        ship.src(f"tests/pirate-crows-nest-3.png")
        title.text = "You see: The crows nest port side. You see nothing."
        options.text = "Exits: right"

    if ship.stash.location == CROWS_NEST_RIGHT:
        ship.src(f"tests/pirate-crows-nest-2.png")
        title.text = "You see: The crows nest startboard side. There is something on the horizon!"
        options.text = "Exits: left"
        # tell the ship the user has seen the enemy!!
        ship.stash.seen_enemy = True

    if ship.stash.location == SHIP_OVERVIEW:
        # CROWS NEST 1
        ship.src(f"tests/pirate-ship-2.png")
        title.text = "You see: Your pirate ship"
        options.text = "Exits: crows nest"

        if ship.stash.seen_enemy:
            options.text += ", right"

        if ship.stash.seen_island:
            options.text += ", north"
        
    


def command_return_pressed():
    print("Command:", command.text)
    

    # parse the command
    action, param = command.text.split(" ", 1)

    if action=="go":
        if ship.stash.location == SHIP_OVERVIEW:
            if param=="crows nest":
                ship.stash.location = CROWS_NEST
            if param=="north" and ship.stash.seen_island:
                ship.stash.location = ST_MICHAELS

        elif ship.stash.location == CROWS_NEST:
            if param=="down":
                ship.stash.location = SHIP_OVERVIEW
            elif param=="left":
                ship.stash.location = CROWS_NEST_LEFT
            elif param=="right":
                ship.stash.location = CROWS_NEST_RIGHT

        elif ship.stash.location == CROWS_NEST_LEFT:
            if param=="right":
                ship.stash.location = CROWS_NEST

        elif ship.stash.location == CROWS_NEST_RIGHT:
            if param=="left":
                ship.stash.location = CROWS_NEST

        elif ship.stash.location == ST_MICHAELS:
            if param=="set sail":
                ship.stash.location = SHIP_OVERVIEW
            elif param=="row to island":
                ship.stash.location = ST_MICHAELS_2
        

    command.text = ""
    update_screen()



ship = Image("tests/pirate-ship-3.png")
ship.style <<= "left: 62px; top: 5px;"
ship.stash.location = SHIP_OVERVIEW
ship.stash.seen_enemy = False
ship.stash.seen_island = False

title = Label("You see: Your pirate ship")
title.style <<= "left: 62px; top: 550px; font-size: 22px; background-color: gold; padding: 5px 20px;"

options = Label("Exits: Crows Nest")
options.style <<= "left: 62px; top: 600px; font-size: 18px; background-color: #98FB98; padding: 5px 20px;"

command = Input("")
command.style <<= "width: 400px; left: 62px; top: 650px; "


go()