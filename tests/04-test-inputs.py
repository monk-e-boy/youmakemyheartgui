# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input

msg = Label("The input box:")
msg.style <<= "top:50px; left: 50px; width: 300px; min-width: 300px; max-width: 350px"

i = Input("")
i.style <<= "left: 50px; top: 150px; width: 250px;"

instructions = Label("Type here ⤴️ the press <return> or click ➡️")
instructions.style <<= "left 50px; top: 200px; width: 500px; min-width: 500px; max-width: 500px"

clear = Button("Clear")
clear.style <<= "left: 320px; top: 150px; background-color: #36BBA7; height: 30px"

ping = Button("Append !")
ping.style <<= "left: 420px; top: 150px; background-color: #36BBA7; height: 30px"

hello = Button("Set to hello")
hello.style <<= "left: 550px; top: 150px; background-color: #A736BB; height: 30px"

yay = Button("Yay ➡️")
yay.style <<= "left: 550px; top: 200px;"

def i_text_changed():
    print(f"Text changed to: {i.text}")
    msg.text = "The input box:"+i.text

def i_return_pressed():
    print("Label 'i' -- Return pressed!!")
    i.text = ""

def clear_click():
    i.text = ""

def ping_click():
    i.text += "!"

def hello_click():
    i.text = "hello"

go()