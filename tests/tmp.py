from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

msg = Label("I'm made of buttons! Click me!")
msg.style <<= ( 
    "top: 60px; left: 500px;"
    "width: 300px; min-width: 300px; max-width: 350px;"
    "background-color: #ffd1ec; border: 3px solid #a152ba;"
)

go()