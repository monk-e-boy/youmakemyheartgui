# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

left = 50
b1 = Button("I go wiizzin' ->>")
b1.style <<= f"left: {left}px; top: 50px;"

b2 = Button("<<- I go wiizzin'")
b2.state.left = 450
b2.style <<= f"left: {b2.state.left}px; top: 120px; background-color: #ff82a0;"

move = Button("Move it!")
move.style <<= "left: 50px; top: 300px;"

def move_click():
    global left
    left += 5
    b1.style <<= f"left: {left}px"

    b2.state.left -= 5
    b2.style <<= f"left: {b2.state.left}px;"

go()