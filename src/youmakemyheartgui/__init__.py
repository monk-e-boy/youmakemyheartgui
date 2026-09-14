# pip install -e .

from PyQt6.QtWidgets import QApplication
from .MainWindow import MainWindow
from .Widgets import Button, Label, Input, Image
import inspect
import sys

#
# set up some global variables
#
global app, win
app = QApplication([])
win = MainWindow()

from .PrintCapture import *


def go_link_buttons_to_click_handlers(global_vars):
     # 1. Identify Button Instances and their variable names
    buttons_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Button):
            # Store the name on the object itself
            value.instance_name = name
            buttons_to_link[name] = value

    # 2. Link Buttons to Click Handler Functions
    for btn_name, button_obj in buttons_to_link.items():
        # The expected function name is the button's name plus '_click'
        handler_name = f"{btn_name}_click" 
        
        if handler_name in global_vars and callable(global_vars[handler_name]):
            handler_func = global_vars[handler_name]
            button_obj.click_handler = handler_func
            print(f"✅ Linked Button '{btn_name}' (Text: '{button_obj._text}') to handler '{handler_name}'.")
        else:
            button_obj.click_handler = lambda name=btn_name, func_name=handler_name: \
                print(f"❌ Button [{name}] could not find click event:\ndef {func_name}():\n    pass")
            print(f"❌ Button '{btn_name}' does NOT have a click event: '{handler_name}'.")

# Text changed + return pressed
def go_link_inputs_to_handlers(global_vars):
    # 1. Identify Input Instances and their variable names
    inputs_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Input):
            # Store the name on the object itself
            value.instance_name = name
            inputs_to_link[name] = value

    # 2. Link Inputs to text changed and return pressed handlers
    for inp_name, input_obj in inputs_to_link.items():
        # The expected function name is the button's name plus '_text_changed'
        tc = f"{inp_name}_text_changed"
        rp = f"{inp_name}_return_pressed"

        
        if tc in global_vars and callable(global_vars[tc]):
            handler_func = global_vars[tc]
            input_obj.text_changed_handler = handler_func
            print(f"✅ Linked Input '{inp_name}' to handler '{tc}'.")
        else:
            input_obj.text_changed_handler = False


        if rp in global_vars and callable(global_vars[rp]):
            handler_func = global_vars[rp]
            input_obj.return_pressed_handler = handler_func
            print(f"✅ Linked Input '{inp_name}' to handler '{rp}'.")
        else:
            input_obj.return_pressed_handler = False

        #
        # TODO: I'm not sure students will always want to attach code to
        #       text changed or return pressed events. Do we want to warn
        #       them here?
        #
        #if not found:
        #    input_obj.return_pressed_handler = lambda name=inp_name, func_name=f"{tc} or {rp}" : \
        #        print(f"❌ Input [{name}] could not find text changed events:\n{func_name}")
        #    print(f"❌ Input [{name}] could not find text changed events:\n{func_name}")

def go_part_2(global_vars):
    # BUTTONS
    buttons_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Button):
            # Store the name on the object itself
            value.instance_name = name
            buttons_to_link[name] = value

    for key in buttons_to_link:
        value = buttons_to_link[key]
        win.add_button(value)

    # LABELS
    labels_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Label):
            # Store the name on the object itself
            value.instance_name = name
            labels_to_link[name] = value

    for key in labels_to_link:
        value = labels_to_link[key]
        win.add_label(value)

    # IMAGES
    images_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Image):
            # Store the name on the object itself
            value.instance_name = name
            images_to_link[name] = value

    for key in images_to_link:
        value = images_to_link[key]
        win.add_image(value)

    # IMPUTS
    inputs_to_link = {}
    for name, value in global_vars.copy().items():
        if isinstance(value, Input):
            # Store the name on the object itself
            value.instance_name = name
            inputs_to_link[name] = value

    for key in inputs_to_link:
        value = inputs_to_link[key]
        win.add_input(value)


def go():
    print("--- 🚀 Initializing GUI Components ---")

    # If we were NOT inside a module this would work:
    # global_vars = globals()
    # Get the global variables of the calling script
    global_vars = sys._getframe(1).f_globals

    go_link_buttons_to_click_handlers(global_vars)
    go_link_inputs_to_handlers(global_vars)
    go_part_2(global_vars)
    #
    win.show()

    #
    # after the window is shown, now we can set focus
    #
    # TODO select the top one (at the top of the screen I feel is most obvious)
    if len(win.inputs):
        f = next(iter(win.inputs))
        win.inputs[f].setFocus()
    app.exec()