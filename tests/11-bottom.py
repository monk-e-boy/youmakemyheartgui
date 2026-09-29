# youmakemy-♡-gui
# Using "bottom:" on a Label or Input should place it relative to the
# bottom of the window. Currently it raises NameError: name 'h' is not defined
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Label, Input, Button

msg = Label("I should sit 50px above the bottom edge")
msg.style <<= "left: 50px; bottom: 50px;"

i = Input("")
i.style <<= "left: 50px; bottom: 120px; width: 250px;"

b = Button("Hello")
b.style <<= "left: 50px; bottom: 220px;"

go()