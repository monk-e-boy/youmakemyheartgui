# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button


b1 = Button("Test One 😊")
b1.style <<= "left: 50px; top: 50px;"
#b1.style <<= (
#    "background-color: #4CAF50;"
#    "border: 2px solid #2E7D32;"
#    "border-top: 2px solid #a5d6a7;"
#    "border-bottom: 6px solid #1B5E20;"
#    "border-radius: 8px;"
#    "padding: 10px 18px;"
#    "color: white;"
#    "font-weight: bold;"
#)


b1.style <<= (
    
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



def b1_click():
    print("!")

go()