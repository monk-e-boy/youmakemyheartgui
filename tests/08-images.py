# <a href="https://www.vecteezy.com/free-vector/backdrop">Backdrop Vectors by Vecteezy</a>
# https://www.vecteezy.com/vector-art/6133451-tropical-plants-background-rectangle-floral-frame-with-space-for-text-in-concept-bamboo-vector
# https://www.vecteezy.com/vector-art/220833-vector-text-frame

# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image

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
bg2.style <<= f"top: 400px;"

go()