# youmakemy-♡-gui
#
# Tests `display` and `visibility` on every kind of widget.
#
#  - LEFT side:  the widgets being tested (one of each type)
#  - RIGHT side: the controls (these never hide themselves)
#
# What to check:
#   1. No "Unknown property" warnings in the console
#   2. Each widget really disappears and reappears
#   3. It comes back in the SAME place (including the bottom: one)
#   4. display and visibility are independent: if EITHER says hide, it's hidden
#
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Image

#
# THE WIDGETS UNDER TEST
#
target_label = Label("I am a Label")
target_label.style <<= "left: 50px; top: 50px;"

target_button = Button("I am a Button")
target_button.style <<= "left: 50px; top: 130px;"

target_input = Input("")
target_input.style <<= "left: 50px; top: 220px; width: 250px;"

target_image = Image("tests/smile-1.png")
target_image.style <<= "left: 50px; top: 310px;"

# positioned from the bottom: checks size is known before it is placed
target_corner = Label("I am a Label placed with bottom:")
target_corner.style <<= "left: 50px; bottom: 30px;"

targets = [target_label, target_button, target_input, target_image, target_corner]

#
# CONTROLS (right-hand side, never hidden)
#
status = Label("display: block / visibility: visible")
status.style <<= "left: 400px; top: 50px; width: 330px;"

toggle_display = Button("Toggle display: none")
toggle_display.style <<= "left: 400px; top: 130px; background-color: #A736BB;"

toggle_visibility = Button("Toggle visibility: hidden")
toggle_visibility.style <<= "left: 400px; top: 200px; background-color: #36BBA7;"

toggle_label = Button("Toggle just the Label")
toggle_label.style <<= "left: 400px; top: 290px; background-color: #3BB8DB;"

toggle_button = Button("Toggle just the Button")
toggle_button.style <<= "left: 400px; top: 360px; background-color: #3BB8DB;"

toggle_input = Button("Toggle just the Input")
toggle_input.style <<= "left: 400px; top: 430px; background-color: #3BB8DB;"

toggle_image = Button("Toggle just the Image")
toggle_image.style <<= "left: 400px; top: 500px; background-color: #3BB8DB;"

toggle_corner = Button("Toggle just the bottom: Label")
toggle_corner.style <<= "left: 400px; top: 570px; background-color: #3BB8DB;"

#
# STATE
#
display_hidden = False
visibility_hidden = False


def show_status():
    d = "none" if display_hidden else "block"
    v = "hidden" if visibility_hidden else "visible"
    status.text = f"display: {d} / visibility: {v}"


def toggle_display_click():
    global display_hidden
    display_hidden = not display_hidden
    value = "none" if display_hidden else "block"
    for t in targets:
        t.style <<= f"display: {value};"
    show_status()


def toggle_visibility_click():
    global visibility_hidden
    visibility_hidden = not visibility_hidden
    value = "hidden" if visibility_hidden else "visible"
    for t in targets:
        t.style <<= f"visibility: {value};"
    show_status()


# Each widget remembers its own state, so these work on their own.
# (They use `display`, so they share that property with the big
# "Toggle display" button - the last one clicked wins.)
def flip(widget):
    widget.state.off = not getattr(widget.state, "off", False)
    widget.style <<= "display: none;" if widget.state.off else "display: block;"
    print(f"{widget.instance_name} -> {'hidden' if widget.state.off else 'shown'}")


def toggle_label_click():
    flip(target_label)

def toggle_button_click():
    flip(target_button)

def toggle_input_click():
    flip(target_input)

def toggle_image_click():
    flip(target_image)

def toggle_corner_click():
    flip(target_corner)


# the widgets under test don't need handlers, but Button warns if it
# can't find one - so give the target button something harmless
def target_button_click():
    print("target button clicked!")


go()