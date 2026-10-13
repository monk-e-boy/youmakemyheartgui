# <a href="https://www.vecteezy.com/free-vector/backdrop">Backdrop Vectors by Vecteezy</a>
# https://www.vecteezy.com/vector-art/6133451-tropical-plants-background-rectangle-floral-frame-with-space-for-text-in-concept-bamboo-vector
# https://www.vecteezy.com/vector-art/220833-vector-text-frame

# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Image, Timer


msg = Label("The poets have been ominously silent")
msg.style <<= "top:250px; left: 50px; width: 300px; min-width: 300px; max-width: 350px"


w = 4800 * 0.1
h = 3600 * 0.1

bg = Image("tests/08-bg1.jpg")
bg.style <<= f"width: {w}px; height: {h}px;"


w = 4800 * 0.05
h = 3600 * 0.05

bg2 = Image("tests/08-bg1.jpg")
bg2.style <<= f"top: 400px; width: {w}px; height: {h}px;"

smile = Image("tests/smile-2.png")
smile.style <<= f"top: 400px; left: 300px;"
smile.stash.angle = 0

spin = Button("🔄  Spin")
spin.style <<= "left: 590px; top: 550px; font-size: 28px; padding: 10px;"
spin.style <<= "background-color: #c62828; background: linear-gradient(#ff5252, #8b0000);"
spin.style <<= "color: #ffeb3b; font-weight: bold; border: 3px solid #ffeb3b; border-radius: 10px;"

spinner = Timer(40)

def spinner_tick():
    smile.stash.angle = (smile.stash.angle + 2) % 360
    smile.style <<= f"transform: rotate({smile.stash.angle}deg);"

def spin_click():
    spinner.toggle()


go()