from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button

b = Button("Right")
b.style <<= "right: 50px; top: 50px;"   # UnboundLocalError on w

go()