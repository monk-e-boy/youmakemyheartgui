from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input

msg = Label("Message:")
msg.style <<= "left: 50px"


i_label = Label("Please enter your name:")
i_label.style <<= "left: 50px; top: 100px"

i = Input("")
i.style <<= "left: 320px; top: 100px; padding: 8px;"

message = Button("Click me!")
message.style <<= "left: 50px; top: 150px; padding: 20px;"

go()