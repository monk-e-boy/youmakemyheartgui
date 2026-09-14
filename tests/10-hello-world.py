# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label


msg = Label("Hello World!")
msg.style <<= "top:50px; left: 50px; width: 300px; min-width: 300px; max-width: 350px"

b1 = Button("Test One 😊")
b1.style <<= "left: 50px; top: 150px;"

b2 = Button("Test Two 🙄")
#b2.style <<= (
#    "left: 50px; top: 230px;"
#    "background-color: #4CAF50;"
#)

b2.style <<= (
    "left: 50px; top: 230px;"
    # CHUNKY FIXES START HERE
    "color: #000000;"
    # A subtle gradient makes the button look convex/curved instead of flat 
    # "background-gradient: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #66bb6a, stop:1 #4CAF50);"
    "border: 2px solid #388E3C;"
    "border-radius: 6px;"
    "border-bottom: 4px solid #2E7D32;" # The "chunky" underside shadow
)

def b1_click():
    msg.text = "Hello world! 😊"
    print("Hello world!!!")

def b2_click():
    msg.text = "Hello world! 🙄"

go()