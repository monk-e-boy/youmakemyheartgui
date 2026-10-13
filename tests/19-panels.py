# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Panel
import random

# a classic raised grey panel (the defaults)
window = Panel()
window.style <<= "left: 40px; top: 40px; width: 420px; height: 300px;"

# a sunken panel inside it (like a text well)
well = Panel()
well.style <<= "left: 60px; top: 70px; width: 380px; height: 80px; border-style: inset; background-color: white;"

# an etched group box
group = Panel()
group.style <<= "left: 60px; top: 170px; width: 380px; height: 150px; border-style: groove;"

# a thick, coloured one
fun = Panel()
fun.style <<= "left: 500px; top: 40px; width: 200px; height: 150px; background-color: #ff82a0; border-width: 4px;"

# a gradient face (title bar!)
title = Panel()
title.style <<= "left: 50px; top: 420px; width: 300px; height: 30px; background: linear-gradient(to right, #000080, #1084d0); border-width: 1px;"

msg = Label("Hello from inside a panel")
msg.style <<= "left: 70px; top: 80px; background-color: transparent;"

b = Button("OK")
b.style <<= (
    "left: 350px; top: 250px; background-color: #D4D0C8;"
    "border: 3px solid #b91c1c;"
    "border-top-color: #ffffff; border-left-color: #ffffff; border-bottom-color: #808080; border-right-color: #808080;"
)

def b_click():
    msg.text += random.choice(["OK",":)","Yes!","kk","ping","pong"]) + " "
go()