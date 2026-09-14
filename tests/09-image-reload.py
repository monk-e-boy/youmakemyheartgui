# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image


smile = Image("tests/smile-1.png")
smile.style <<= "top: 40px"
smile.stash.count = 1

change = Button("Next!")
change.style <<= "top: 350px; left: 100px;"

def change_click():
    smile.stash.count += 1
    if smile.stash.count > 9:
        smile.stash.count = 1
    smile.src(f"tests/smile-{smile.stash.count}.png")
    print("Hello!!")

go()