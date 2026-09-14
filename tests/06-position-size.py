# pixel perfect sizing (padding, borders, width, height)

# size = text size
#      + style padding
#      + style borders
#      + OS theme insets
#      + extra focus-frame offsets


# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

#
# without width
#
b1 = Button("😊")
b1.style <<= "left: 50px; top: 50px; margin: 0; padding: 0; width: 50px; border-radius: 20px; background-color: green;"

b2 = Button("Test Two 😊")
b2.style <<= "left: 50px; top: 150px;"

right_arm = Button("😍\n💕\n😊")
right_arm.style <<= (
    "left: 450px; top: 350px;"
    "height: 150px; width: 50px;"
    "background-color: #9ebd90;"
)

left_arm = Button("💕\n😍\n🤩")
left_arm.style <<= (
    "left: 250px; top: 350px;"
    "height: 150px; width: 50px;"
    "background-color: #fac854;"
)

left_leg = Button("🎶\n😎\n✌️")
left_leg.style <<= (
    "left: 320px; top: 500px;"
    "height: 150px; width: 50px;"
    "background-color: #d3e2a1;"
)

right_leg = Button("🎶\nLEG\n✌️\n🎶")
right_leg.style <<= (
    "left: 380px; top: 500px;"
    "height: 150px; width: 50px;"
    "background-color: #84fdee;"
)

#
# With WIDTH set
#

#ba = Button("A")
#ba.style <<= "left: 50px; top: 100px; width: 50px; background-color: #FB2C36;"

msg = Label("I'm made of buttons! Click me!")
msg.style <<= ( 
    "top: 60px; left: 500px;"
    "width: 300px; min-width: 300px; max-width: 350px;"
    "background-color: #ffd1ec; border: 3px solid #a152ba;"
)

msg2 = Label("/")
msg2.style <<= "top: 120px; left: 460px; font-size: 50px; color: #a152ba;"

bb = Button("^ - ^")
bb.style <<= "left: 300px; top: 150px;"
bb.style <<= "width: 150px; height: 150px;"
bb.style <<= "background-color: #a152ba; border-radius: 16px;"

bc = Button("BODY")
bc.style <<= (
    "padding: 0px; margin: 0px;"
    "left: 300px; top: 350px;"
    "width: 150px; height: 150px;"
    "background-color: #ff82a0;"
)
print(bc.style)

b9 = Button("Can rotate?")
b9.style <<= "left: 50px; top: 350px; width: 150px; rotate: 30deg;"


go()