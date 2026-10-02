# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button


b1 = Button("Test One 😊")
b1.style <<= (
    "left: 50px;"
    "top: 50px;"
    "background-color: #f0003c;"
    "border-bottom: 5px solid #a30036;"
    "border-top:    5px solid #ed487f;"
    "border-left:   5px solid #ed487f;"
    "border-right:  5px solid #a30036;"
    "border-radius: 8px;"
    "padding: 10px 18px;"
    "color: white;"
    "font-weight: bold;"
)

#background-image: linear-gradient(#f7f8fa, #e7e9ec);
#    border-color: #adb1b8 #a2a6ac #8d9096;


b2 = Button("Test Grey 😊")
b2.style <<= (
    "left: 50px;"
    "top: 150px;"
    "background-color: #e7e9ec;"
    "border: 1px solid #8d9096;"
    "border-radius: 3px;"
    "padding: 10px 18px;"
    "color: #555555;"
    "font-weight: bold;"
)

def b2_click():
    print("!")

go()