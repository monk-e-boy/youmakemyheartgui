# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

style = "" # "height: 40px; font-size: 22px; width: 50px;"

b1 = Button("Test One 😊")
b1.style <<= "left: 50px; top: 50px;"

b2 = Button("2")
b2.style <<= (
    "left: 50px; top: 130px; width: 50px;"
    "background-color: #4CAF50;"
)

b3 = Button("3")
#
# THE USER HAS MISTAKENLY USE A TUPLE:
#
#b3.style <<= (
#    "left: 50px;", # <-- LOOK there is a comma
#    "top: 180px;", # <-- LOOK there is a comma
#    "background-color: #4CAF50;"
#)

#
# ROW 1
#

# https://htmlcolorcodes.com/color-chart/
ba = Button("A")
ba.style <<= "left: 50px; top: 350px; width: 50px; background-color: #FB2C36;"

bb = Button("B")
bb.style <<= "left: 100px; top: 350px; width: 50px; background-color: #FF692A;"

bc = Button("C")
bc.style <<= "left: 150px; top: 350px; width: 50px; background-color: #FE9A37;"

bd = Button("D")
bd.style <<= "left: 200px; top: 350px; width: 50px; background-color: #F0B13B;"

be = Button("E")
be.style <<= "left: 250px; top: 350px; width: 50px; background-color: #7CCF35;"

bf = Button("F")
bf.style <<= "left: 300px; top: 350px; width: 50px; background-color: #31C950;"

bg = Button("G")
bg.style <<= "left: 350px; top: 350px; width: 50px; background-color: #37BC7D;"

bh = Button("H")
bh.style <<= "left: 400px; top: 350px; width: 50px; background-color: #36BBA7;"

bi = Button("I")
bi.style <<= "left: 450px; top: 350px; width: 50px; background-color: #3BB8DB;"

bj = Button("J")
bj.style <<= "left: 500px; top: 350px; width: 50px; background-color: #34A6F4;"

bk = Button("K")
bk.style <<= "left: 550px; top: 350px; width: 50px; background-color: #2B7FFF;"

bl = Button("L")
bl.style <<= "left: 600px; top: 350px; width: 50px; background-color: #615FFF;"


#
# ROW 2
#

ba2 = Button("A")
ba2.style <<= "left: 50px; top: 430px; width: 50px; background-color: #FB2C36; color: #ffffff"
ba2.hover_style = "background-color: #F0B13B;"

bb2 = Button("B")
bb2.style <<= "left: 100px; top: 430px; width: 50px; background-color: #FF692A; color: #ffffff"
bb2.hover_style = "background-color: #ff07a9;"

bc2 = Button("C")
bc2.style <<= "left: 150px; top: 430px; width: 50px; background-color: #FE9A37; color: #ffffff"
bc2.hover_style = "background-color: #ff07a9;"

bd2 = Button("D")
bd2.style <<= "left: 200px; top: 430px; width: 50px; background-color: #F0B13B; color: #ffffff"
bd2.hover_style = "background-color: #ff07a9;"

be2 = Button("E")
be2.style <<= "left: 250px; top: 430px; width: 50px; background-color: #7CCF35; color: #ffffff"
be2.hover_style = "background-color: #ff07a9;"

bf2 = Button("F")
bf2.style <<= "left: 300px; top: 430px; width: 50px; background-color: #31C950; color: #ffffff"
bf2.hover_style = "background-color: #ff07a9;"

bg2 = Button("G")
bg2.style <<= "left: 350px; top: 430px; width: 50px; background-color: #37BC7D; color: #ffffff"
bg2.hover_style = "background-color: #ff07a9;"

bh2 = Button("H")
bh2.style <<= "left: 400px; top: 430px; width: 50px; background-color: #36BBA7; color: #ffffff"
bh2.hover_style = "background-color: #ff07a9;"

bi2 = Button("I")
bi2.style <<= "left: 450px; top: 430px; width: 50px; background-color: #3BB8DB; color: #ffffff"
bi2.hover_style = "background-color: #ff07a9;"

bj2 = Button("J")
bj2.style <<= "left: 500px; top: 430px; width: 50px; background-color: #34A6F4; color: #ffffff"
bj2.hover_style = "background-color: #ff07a9;"

bk2 = Button("K")
bk2.style <<= "left: 550px; top: 430px; width: 50px; background-color: #2B7FFF; color: #ffffff"
bk2.hover_style = "background-color: #ff07a9;"

bl2 = Button("L")
bl2.style <<= "left: 600px; top: 430px; width: 50px; background-color: #615FFF; color: #ffffff"
bl2.hover_style = "background-color: #ff07a9;"

go()