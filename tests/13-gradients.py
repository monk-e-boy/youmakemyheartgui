# youmakemy-♡-gui
#
# 12 - GRADIENTS + BUTTON STYLE GALLERY
#
# Two jobs:
#   1. tests every kind of linear-gradient the style parser understands
#   2. a "steal this" catalogue of nice buttons - copy the style you like
#
# TIPS
#   * write normal CSS:  background: linear-gradient(#a, #b);
#   * put a plain  background-color  BEFORE the gradient. It is the colour
#     the button uses for hover / pressed, so pick something in the middle
#     of your two gradient colours.
#   * keep border WIDTH the same on all sides. If you want a 3D look, change
#     the border COLOUR of the top / bottom instead (see "chunky" below).
#
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

# ------------------------------------------------------------------
# Titles and captions
# ------------------------------------------------------------------
caption = "font-size: 14px; color: #555555; background-color: transparent;"

title = Label("Gradient + button gallery")
title.style <<= "left: 20px; top: 8px; font-size: 26px; background-color: transparent;"

cap1 = Label("Directions:  default, to top, to right, to left, and the four corners")
cap1.style <<= "left: 20px; top: 52px;" + caption

cap2 = Label("Angles, stops, percentages, hard bands, rgb() colours, rainbow")
cap2.style <<= "left: 20px; top: 130px;" + caption

cap3 = Label("Border widths: 1px 2px 3px 4px 6px 8px")
cap3.style <<= "left: 20px; top: 210px;" + caption

#cap4 = Label("Ghost, pill, circle and chunky (uniform border width, different colours)")
#cap4.style <<= "left: 20px; top: 222px;" + caption

#cap5 = Label("Ready-made buttons")
#cap5.style <<= "left: 20px; top: 300px;" + caption

#cap6 = Label("Fun ones")
#cap6.style <<= "left: 20px; top: 428px;" + caption

status = Label("Click something...")
status.style <<= "left: 20px; top: 680px; width: 500px; min-width: 500px; font-size: 18px;"

# ------------------------------------------------------------------
# ROW 1 - directions
# ------------------------------------------------------------------
small = "width: 84px; height: 40px; font-size: 20px; padding: 0px; border-radius: 8px; color: white;"

d1 = Button("↓")
d1.style <<= "left: 20px; top: 85px;" + small
d1.style <<= "background-color: #5b6ee1; background: linear-gradient(#7f8ff4, #3f4fb8);"

d2 = Button("↑")
d2.style <<= "left: 112px; top: 85px;" + small
d2.style <<= "background-color: #5b6ee1; background: linear-gradient(to top, #7f8ff4, #3f4fb8);"

d3 = Button("→")
d3.style <<= "left: 204px; top: 85px;" + small
d3.style <<= "background-color: #ff7b64; background: linear-gradient(to right, #ff9966, #ff5e62);"

d4 = Button("←")
d4.style <<= "left: 296px; top: 85px;" + small
d4.style <<= "background-color: #ff7b64; background: linear-gradient(to left, #ff9966, #ff5e62);"

d5 = Button("↘")
d5.style <<= "left: 388px; top: 85px;" + small
d5.style <<= "background-color: #1fb17f; background: linear-gradient(to bottom right, #34d399, #059669);"

d6 = Button("↙")
d6.style <<= "left: 480px; top: 85px;" + small
d6.style <<= "background-color: #1fb17f; background: linear-gradient(to bottom left, #34d399, #059669);"

d7 = Button("↗")
d7.style <<= "left: 572px; top: 85px;" + small
d7.style <<= "background-color: #7c3aed; background: linear-gradient(to top right, #a855f7, #5b21b6);"

d8 = Button("↖")
d8.style <<= "left: 664px; top: 85px;" + small
d8.style <<= "background-color: #7c3aed; background: linear-gradient(to top left, #a855f7, #5b21b6);"

# ------------------------------------------------------------------
# ROW 2 - angles, stops, percentages, bands, rgb, rainbow
# ------------------------------------------------------------------
small2 = "width: 84px; height: 40px; font-size: 16px; padding: 0px; border-radius: 8px;"

a1 = Button("45°")
a1.style <<= "left: 20px; top: 160px; color: #5a3a1a;" + small2
a1.style <<= "background-color: #fabb75; background: linear-gradient(45deg, #f6d365, #fda085);"

a2 = Button("90°")
a2.style <<= "left: 112px; top: 160px; color: #1f4e4a;" + small2
a2.style <<= "background-color: #88e6c2; background: linear-gradient(90deg, #84fab0, #8fd3f4);"

a3 = Button("135°")
a3.style <<= "left: 204px; top: 160px; color: white;" + small2
a3.style <<= "background-color: #6f65c6; background: linear-gradient(135deg, #667eea, #764ba2);"

a4 = Button("3 stops")
a4.style <<= "left: 296px; top: 160px; color: #4a3200;" + small2
a4.style <<= "background-color: #f2c14e; background: linear-gradient(#fff1a8, #f2c14e, #b8860b);"

a5 = Button("30%")
a5.style <<= "left: 388px; top: 160px; color: #37474f; border: 1px solid #b0bec5;" + small2
a5.style <<= "background-color: #e3e8ea; background: linear-gradient(#ffffff 30%, #cfd8dc);"

# a hard edge (two stops at 50%) gives a glossy "shine" on the top half
a6 = Button("gloss")
a6.style <<= "left: 480px; top: 160px; color: white;" + small2
a6.style <<= "background-color: #283350; background: linear-gradient(#2e3a59 50%, #1f2740 50%);"

a7 = Button("rgb()")
a7.style <<= "left: 572px; top: 160px; color: white;" + small2
a7.style <<= "background-color: #ff7b64; background: linear-gradient(rgb(255, 94, 98), rgb(255, 153, 102));"

a8 = Button("rainbow")
a8.style <<= "left: 664px; top: 160px; color: #1b1b2f; font-weight: bold;" + small2
a8.style <<= "background-color: #48dbfb; background: linear-gradient(to right, #ff6b6b, #feca57, #48dbfb, #1dd1a1, #a55eea);"

# ------------------------------------------------------------------
# ROW 3 - border widths (navy + gold)
# ------------------------------------------------------------------
navy = "height: 44px; width: 100px; font-size: 16px; padding: 0px; color: white; border-radius: 10px;"
navy += "background-color: #2c3a63; background: linear-gradient(#3b4a7a, #1b2440);"

bw1 = Button("1px")
bw1.style <<= "left: 20px; top: 245px; border: 1px solid #d4a017;" + navy

bw2 = Button("2px")
bw2.style <<= "left: 128px; top: 245px; border: 2px solid #d4a017;" + navy

bw3 = Button("3px")
bw3.style <<= "left: 236px; top: 245px; border: 3px solid #d4a017;" + navy

bw4 = Button("4px")
bw4.style <<= "left: 344px; top: 245px; border: 4px solid #d4a017;" + navy

bw6 = Button("6px")
bw6.style <<= "left: 452px; top: 245px; border: 6px solid #d4a017;" + navy

bw8 = Button("8px")
bw8.style <<= "left: 560px; top: 245px; border: 8px solid #d4a017;" + navy

# ------------------------------------------------------------------
# ROW 4 - ghost, pill, circle, chunky
# ------------------------------------------------------------------
ghost = Button("Ghost")
ghost.style <<= "left: 20px; top: 310px; width: 90px; height: 44px; font-size: 16px; padding: 0px;"
ghost.style <<= "background-color: #ffffff; color: #2c3a63; border: 2px solid #2c3a63; border-radius: 10px;"

pill = Button("Pill")
pill.style <<= "left: 122px; top: 310px; width: 120px; height: 44px; font-size: 16px; padding: 0px;"
pill.style <<= "background-color: #e2a596; background: linear-gradient(#f9d4c8, #d99c8c);"
pill.style <<= "color: #5a2e26; border: 1px solid #b5786a; border-radius: 22px;"

circle = Button("＋")
circle.style <<= "left: 254px; top: 310px; width: 50px; height: 50px; font-size: 26px; padding: 0px;"
circle.style <<= "background-color: #3b82f6; background: linear-gradient(#60a5fa, #2563eb);"
circle.style <<= "color: white; border: 2px solid #1d4ed8; border-radius: 25px;"

chunky = "width: 110px; height: 44px; font-size: 16px; padding: 0px; color: white; border-radius: 10px;"

chunky_green = Button("Chunky")
chunky_green.style <<= "left: 318px; top: 310px;" + chunky
chunky_green.style <<= "background-color: #54ad58; background: linear-gradient(#66bb6a, #43a047);"
chunky_green.style <<= "border: 3px solid #2e7d32; border-top-color: #a5d6a7; border-bottom-color: #1b5e20;"

chunky_blue = Button("Chunky")
chunky_blue.style <<= "left: 440px; top: 310px;" + chunky
chunky_blue.style <<= "background-color: #3b82f6; background: linear-gradient(#60a5fa, #2563eb);"
chunky_blue.style <<= "border: 3px solid #1d4ed8; border-top-color: #bfdbfe; border-bottom-color: #1e3a8a;"

chunky_red = Button("Chunky")
chunky_red.style <<= "left: 562px; top: 310px;" + chunky
chunky_red.style <<= "background-color: #ef4444; background: linear-gradient(#f87171, #dc2626);"
chunky_red.style <<= "border: 3px solid #b91c1c; border-top-color: #fecaca; border-bottom-color: #7f1d1d;"

# ------------------------------------------------------------------
# READY-MADE BUTTONS
# ------------------------------------------------------------------
wide = "width: 180px; height: 44px; font-size: 18px; padding: 0px; border-radius: 10px;"

save = Button("💾  Save")
save.style <<= "left: 20px; top: 400px; color: white;" + wide
save.style <<= "background-color: #22c55e; background: linear-gradient(#4ade80, #16a34a);"
save.style <<= "border: 2px solid #15803d;"

delete = Button("🗑  Delete")
delete.style <<= "left: 210px; top: 400px; color: white;" + wide
delete.style <<= "background-color: #dc2626; background: linear-gradient(#f87171, #b91c1c);"
delete.style <<= "border: 2px solid #991b1b;"

cancel = Button("Cancel")
cancel.style <<= "left: 400px; top: 400px; color: #3c4048;" + wide
cancel.style <<= "background-color: #eff0f3; background: linear-gradient(#f7f8fa, #e7e9ec);"
cancel.style <<= "border: 1px solid #c5c9d0;"

warning = Button("⚠  Careful!")
warning.style <<= "left: 590px; top: 400px; color: #4a3200; font-weight: bold;" + wide
warning.style <<= "background-color: #facc15; background: linear-gradient(#fde047, #f59e0b);"
warning.style <<= "border: 2px solid #b45309;"

info = Button("ℹ  Info")
info.style <<= "left: 20px; top: 450px; color: white;" + wide
info.style <<= "background-color: #3b82f6; background: linear-gradient(#60a5fa, #2563eb);"
info.style <<= "border: 2px solid #1d4ed8;"

done = Button("✔  Done")
done.style <<= "left: 210px; top: 450px; color: white;" + wide
done.style <<= "background-color: #14b8a6; background: linear-gradient(#2dd4bf, #0d9488);"
done.style <<= "border: 2px solid #0f766e;"

download = Button("⬇  Download")
download.style <<= "left: 400px; top: 450px; color: #e2e8f0;" + wide
download.style <<= "background-color: #334155; background: linear-gradient(#475569, #1e293b);"
download.style <<= "border: 2px solid #0f172a;"

play = Button("▶  Play")
play.style <<= "left: 590px; top: 450px; color: white;" + wide
play.style <<= "background-color: #8b5cf6; background: linear-gradient(#a78bfa, #6d28d9);"
play.style <<= "border: 2px solid #5b21b6;"

# ------------------------------------------------------------------
# FUN ONES
# ------------------------------------------------------------------
eject = Button("⏏  Eject!")
eject.style <<= "left: 20px; top: 500px; width: 160px; height: 44px; font-size: 18px; padding: 0px;"
eject.style <<= "background-color: #ff9a20; background: linear-gradient(#ffb347, #ff7b00);"
eject.style <<= "color: #3b1a00; font-weight: bold; border: 3px solid #b34d00; border-radius: 10px;"

dive = Button("🌊  Dive dive dive!")
dive.style <<= "left: 192px; top: 500px; width: 230px; height: 44px; font-size: 18px; padding: 0px;"
dive.style <<= "background-color: #0f3a5f; background: linear-gradient(#1e5f8a, #04162b);"
dive.style <<= "color: #bfefff; border: 2px solid #5ec8e8; border-radius: 10px;"

launch = Button("🚀  Launch")
launch.style <<= "left: 434px; top: 500px; width: 170px; height: 44px; font-size: 18px; padding: 0px;"
launch.style <<= "background-color: #302b63; background: linear-gradient(to right, #0f0c29, #302b63, #6b3fa0);"
launch.style <<= "color: #ffd166; border: 2px solid #ffd166; border-radius: 10px;"

party = Button("🎉  Party")
party.style <<= "left: 616px; top: 500px; width: 170px; height: 44px; font-size: 18px; padding: 0px;"
party.style <<= "background-color: #ffa0a0; background: linear-gradient(135deg, #ff6bcb, #ffb86b, #fff275);"
party.style <<= "color: #4a1030; font-weight: bold; border: 3px solid #ff3fa4; border-radius: 10px;"

coffee = Button("☕  Coffee")
coffee.style <<= "left: 20px; top: 550px;" + wide
coffee.style <<= "background-color: #6d4c41; background: linear-gradient(#8d6e63, #4e342e);"
coffee.style <<= "color: #ffe0b2; border: 2px solid #3e2723;"

snooze = Button("💤  Snooze")
snooze.style <<= "left: 210px; top: 550px;" + wide
snooze.style <<= "background-color: #303a63; background: linear-gradient(#232946, #3d4a78);"
snooze.style <<= "color: #b8c1ec; border: 1px solid #5a67a8;"

level_up = Button("⭐  Level up!")
level_up.style <<= "left: 400px; top: 550px;" + wide
level_up.style <<= "background-color: #fbc02d; background: linear-gradient(#fff59d, #fbc02d, #f57f17);"
level_up.style <<= "color: #4a2c00; font-weight: bold; border: 3px solid #b26a00;"

self_destruct = Button("💥  Self-destruct")
self_destruct.style <<= "left: 590px; top: 550px; width: 200px; height: 44px; font-size: 18px; padding: 0px;"
self_destruct.style <<= "background-color: #c62828; background: linear-gradient(#ff5252, #8b0000);"
self_destruct.style <<= "color: #ffeb3b; font-weight: bold; border: 3px solid #ffeb3b; border-radius: 10px;"

do_not_press = Button("Do not press")
do_not_press.style <<= "left: 20px; top: 600px; color: white;" + wide
do_not_press.style <<= "background-color: #d32f2f; background: linear-gradient(#e53935 50%, #b71c1c 50%);"
do_not_press.style <<= "border: 2px solid #7f0000;"

boop = Button("Boop")
boop.style <<= "left: 210px; top: 600px; color: #5a2e26; border-radius: 22px;"
boop.style <<= "width: 180px; height: 44px; font-size: 18px; padding: 0px;"
boop.style <<= "background-color: #e2a596; background: linear-gradient(#f9d4c8, #d99c8c);"
boop.style <<= "border: 1px solid #b5786a;"

matrix = Button("🕶  Matrix")
matrix.style <<= "left: 400px; top: 600px;" + wide
matrix.style <<= "background-color: #052a05; background: linear-gradient(#0a0a0a, #003b00);"
matrix.style <<= "color: #00ff41; font-family: Consolas, monospace; border: 2px solid #00ff41;"

ice = Button("🧊  Ice")
ice.style <<= "left: 590px; top: 600px;" + wide
ice.style <<= "background-color: #b2ebf2; background: linear-gradient(to bottom right, #e0f7fa, #80deea);"
ice.style <<= "color: #005662; border: 2px solid #4dd0e1;"


# ------------------------------------------------------------------
# Click handlers - a few special ones, everything else is filled in below
# ------------------------------------------------------------------
def save_click():
    status.text = "Saved! 💾"

def delete_click():
    status.text = "Deleted. (Just kidding, nothing was harmed.)"

def eject_click():
    status.text = "3... 2... 1... 🪂"

def dive_click():
    status.text = "AOOGAH! AOOGAH! Diving to 300 metres 🌊"

def self_destruct_click():
    status.text = "Self-destruct in 5... just kidding 💥"

def do_not_press_click():
    status.text = "I said DO NOT press. 😠"


# Give every other button a default handler that reports its own name, so the
# test never prints "could not find click event". (Students: you won't need this,
# just write  def my_button_click():  for each button you care about.)
def _make_default_handler(button_name):
    def handler():
        status.text = f"You clicked: {button_name}"
    return handler

for _name, _value in list(globals().items()):
    if isinstance(_value, Button) and f"{_name}_click" not in globals():
        globals()[f"{_name}_click"] = _make_default_handler(_name)

go()