from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

score = Label("Score: 0")
hit = Button("Click me!")
hit.style <<= "left: 50px; top: 150px; padding: 20px;"

points = 0

go()