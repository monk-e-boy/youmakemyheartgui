# youmakemy-♡-gui
from youmakemyheartgui import go, gravity, gravity_step
from youmakemyheartgui.Widgets import Button, Label, Input

msg = Label("Gravity test")
msg.style <<= "left: 50px; top: 20px;"

a = Button("A")
a.style <<= "left: 100px; top: 100px; width: 80px; background-color: #FB2C36;"

b = Button("B")
b.style <<= "left: 230px; top: 250px; width: 80px; background-color: #34A6F4;"

c = Label("I fall too")
c.style <<= "left: 400px; top: 190px;"

i = Input("")
i.style <<= "left: 50px; top: 170px; width: 250px;"

drop = Button("Drop!")
drop.style <<= "left: 300px; top: 300px;"

step = Button("One step")
step.style <<= "left: 450px; top: 300px;"

pause = Button("Pause")
pause.style <<= "left: 600px; top: 300px;"

circle = Button("＋")
circle.style <<= "left: 254px; top: 50px; width: 50px; height: 50px; font-size: 26px; padding: 0px;"
circle.style <<= "background-color: #3b82f6; background: linear-gradient(#60a5fa, #2563eb);"
circle.style <<= "color: white; border: 2px solid #1d4ed8; border-radius: 25px;"


drop.fixed = True
step.fixed = True
pause.fixed = True


def drop_click():
    gravity(True)

def step_click():
    gravity_step()

def pause_click():
    gravity(False)

def a_click():
    print("A clicked")

def b_click():
    print("B clicked")

def button_click(button):
    print("Something happened")

go()