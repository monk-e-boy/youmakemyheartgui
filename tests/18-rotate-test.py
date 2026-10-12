# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image

msg = Label("Click the tilted buttons, including near their corners")
msg.style <<= "top: 20px; left: 50px;"

b = Button("Spin me")
b.stash.angle = 45
b.style <<= "left: 200px; top: 200px; width: 160px; transform: rotate(45deg);"


b2 = Button("Spin me")
b2.stash.angle = 45
b2.style <<= "left: 200px; top: 270px; width: 160px; transform: rotate(45deg); border-radius: 15px;"


c = Button("Upside down")
c.stash.angle = 180
c.style <<= "left: 200px; top: 400px; transform: rotate(180deg);"
c.style <<= "font-size: 18px; padding: 10px 20px;"
c.style <<= "background-color: #c62828; background: linear-gradient(#ff5252, #8b0000);"
c.style <<= "color: #ffeb3b; font-weight: bold; border: 3px solid #ffeb3b; border-radius: 10px;"

d = Button("Quarter turn")
d.style <<= "right: 50px; bottom: 50px; rotate: 0.25turn;"

i = Input("")
i.style <<= "left: 50px; top: 100px; width: 200px; transform: rotate(-10deg);"

pic = Image("tests/smile-1.png")
pic.style <<= "left: 450px; top: 300px; transform: rotate(20deg);"

def b_click():
    print("b clicked")
    b.stash.angle -= 7
    b.style <<= f"transform: rotate({b.stash.angle}deg);"
    b.text = "Ouch!"

def c_click():
    print("c clicked")
    c.stash.angle += 5
    c.style <<= f"transform: rotate({c.stash.angle}deg);"

def d_click():
    print("d clicked")

go()