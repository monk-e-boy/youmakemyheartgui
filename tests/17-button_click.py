# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

ba = Button("🎵")
ba.stash.value = 1
ba.style <<= "left: 50px; top: 350px; width: 50px; background-color: #FF692A;"

bb = Button("🎵")
bb.stash.value = 2
bb.style <<= "left: 100px; top: 350px; width: 50px; background-color: #FF692A;"

bc = Button("🎵")
bc.stash.value = 3
bc.style <<= "left: 150px; top: 350px; width: 50px; background-color: #FE9A37;"

bd = Button("🎵")
bd.stash.value = 4
bd.style <<= "left: 200px; top: 350px; width: 50px; background-color: #F0B13B;"

be = Button("🎵")
be.stash.value = 5
be.style <<= "left: 250px; top: 350px; width: 50px; background-color: #7CCF35;"

bf = Button("🎵")
bf.stash.value = 6
bf.style <<= "left: 300px; top: 350px; width: 50px; background-color: #31C950;"

bg = Button("🎵")
bg.stash.value = 7
bg.style <<= "left: 350px; top: 350px; width: 50px; background-color: #37BC7D;"

bh = Button("🎵")
bh.stash.value = 8
bh.style <<= "left: 400px; top: 350px; width: 50px; background-color: #36BBA7;"

bi = Button("🎵")
bi.stash.value = 9
bi.style <<= "left: 450px; top: 350px; width: 50px; background-color: #3BB8DB;"

bj = Button("🎵")
bj.stash.value = 10
bj.style <<= "left: 500px; top: 350px; width: 50px; background-color: #34A6F4;"

bk = Button("🎵")
bk.stash.value = 11
bk.style <<= "left: 550px; top: 350px; width: 50px; background-color: #2B7FFF;"

bl = Button("🎵")
bl.stash.value = 12
bl.style <<= "left: 600px; top: 350px; width: 50px; background-color: #615FFF;"

def button_click(button):
    print(f"Clicked a button: {button.stash.value}")

go()