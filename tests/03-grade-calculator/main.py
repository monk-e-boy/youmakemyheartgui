from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input


i_label = Label("Please enter the mark as a %:")
i_label.style <<= "left: 50px; top: 100px"

i = Input("")
i.style <<= "left: 375px; top: 100px; padding: 8px;"

# abacus emoji!!
calculate = Button("🧮   Get grade")
calculate.style <<= "left: 600px; top: 100px;"
calculate.style <<= "font-size: 20px; padding: 5px 10px; color: white; border-radius: 10px;"
calculate.style <<= "background-color: #14b8a6; background: linear-gradient(#2dd4bf, #0d9488);"
calculate.style <<= "border: 2px solid #0f766e;"

msg = Label("Grade:")
msg.style <<= "left: 375px; top: 170px"


go()