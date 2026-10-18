# youmakemy-♡-gui
#
# 21 - THREE SCREENS: login -> address -> your details
#
# Big idea: every screen is just a LIST of widgets.
#   page1 = [...]   page2 = [...]   page3 = [...]
# To change screen we hide() the lists we don't want
# and show() the list we do want.
#
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label, Input, Panel

# ------------------------------------------------------------------
# STYLES (written once, used many times)
# ------------------------------------------------------------------
title_style = "background-color: transparent; color: white; font-size: 24px; font-weight: bold;"
caption_style = "background-color: transparent; color: #1f2a44; font-size: 20px;"
field_style = "width: 270px; font-size: 20px; border: 2px solid #8a94b8;"

green_button = (
    "width: 150px; height: 54px; font-size: 20px; padding: 0px;"
    "color: white; font-weight: bold; border-radius: 10px;"
    "background-color: #54ad58; background: linear-gradient(#66bb6a, #43a047);"
    "border: 3px solid #2e7d32; border-top-color: #a5d6a7; border-bottom-color: #1b5e20;"
)

grey_button = (
    "width: 150px; height: 54px; font-size: 20px; padding: 0px;"
    "color: white; font-weight: bold; border-radius: 10px;"
    "background-color: #6b7280; background: linear-gradient(#9ca3af, #6b7280);"
    "border: 3px solid #4b5563; border-top-color: #d1d5db; border-bottom-color: #374151;"
)

# ------------------------------------------------------------------
# THE CARD - always visible, every page sits on top of it
# ------------------------------------------------------------------
card = Panel()
card.style <<= "left: 150px; top: 100px; width: 500px; height: 420px;"
card.style <<= "background-color: #f5f2ea; border-style: ridge; border-width: 3px;"

title_bar = Panel()
title_bar.style <<= "left: 150px; top: 100px; width: 500px; height: 50px;"
title_bar.style <<= "background: linear-gradient(to right, #1e2a4a, #3b4a7a); border-style: none;"

# ------------------------------------------------------------------
# PAGE 1 - LOGIN
# ------------------------------------------------------------------
login_title = Label("Welcome back")
login_title.style <<= "left: 170px; top: 102px;" + title_style

login_box = Panel()
login_box.style <<= "left: 175px; top: 175px; width: 450px; height: 170px; border-style: groove; background-color: #e8e2d0;"

username_label = Label("Username")
username_label.style <<= "left: 195px; top: 195px;" + caption_style

username = Input("")
username.style <<= "left: 335px; top: 195px;" + field_style

password_label = Label("Password")
password_label.style <<= "left: 195px; top: 265px;" + caption_style

password = Input("")
password.style <<= "left: 335px; top: 265px;" + field_style

error = Label("")
error.style <<= "left: 175px; top: 360px; background-color: transparent; color: #b91c1c; font-size: 18px;"

reset = Button("Reset")
reset.style <<= "left: 175px; top: 420px;" + grey_button

login = Button("Log in")
login.style <<= "left: 475px; top: 420px;" + green_button

# ------------------------------------------------------------------
# PAGE 2 - HOME ADDRESS
# ------------------------------------------------------------------
address_title = Label("Where do you live?")
address_title.style <<= "left: 170px; top: 102px;" + title_style

address_box = Panel()
address_box.style <<= "left: 175px; top: 175px; width: 450px; height: 240px; border-style: groove; background-color: #e8e2d0;"

street_label = Label("Street")
street_label.style <<= "left: 195px; top: 195px;" + caption_style

street = Input("")
street.style <<= "left: 335px; top: 195px;" + field_style

town_label = Label("Town")
town_label.style <<= "left: 195px; top: 265px;" + caption_style

town = Input("")
town.style <<= "left: 335px; top: 265px;" + field_style

postcode_label = Label("Postcode")
postcode_label.style <<= "left: 195px; top: 335px;" + caption_style

postcode = Input("")
postcode.style <<= "left: 335px; top: 335px;" + field_style

back = Button("Back")
back.style <<= "left: 175px; top: 440px;" + grey_button

submit = Button("Submit")
submit.style <<= "left: 475px; top: 440px;" + green_button

# ------------------------------------------------------------------
# PAGE 3 - YOUR DETAILS
# ------------------------------------------------------------------
details_title = Label("Your details")
details_title.style <<= "left: 170px; top: 102px;" + title_style

details_box = Panel()
details_box.style <<= "left: 175px; top: 175px; width: 450px; height: 250px;"
details_box.style <<= "border-style: inset; background-color: white;"

name_out = Label("")
name_out.style <<= "left: 195px; top: 195px;" + caption_style

street_out = Label("")
street_out.style <<= "left: 195px; top: 245px;" + caption_style

town_out = Label("")
town_out.style <<= "left: 195px; top: 295px;" + caption_style

postcode_out = Label("")
postcode_out.style <<= "left: 195px; top: 345px;" + caption_style

restart = Button("Start again")
restart.style <<= "left: 275px; top: 445px;" + green_button
restart.style <<= "width: 250px;"

# ------------------------------------------------------------------
# THE THREE LISTS - one list per screen
# ------------------------------------------------------------------
page1 = [login_title, login_box, username_label, username,
         password_label, password, error, reset, login]

page2 = [address_title, address_box, street_label, street,
         town_label, town, postcode_label, postcode, back, submit]

page3 = [details_title, details_box, name_out, street_out,
         town_out, postcode_out, restart]

# which screen are we on? (1, 2 or 3)
page = 1


# ------------------------------------------------------------------
# SHOW AND HIDE
# ------------------------------------------------------------------
def hide(widgets):
    for w in widgets:
        w.style <<= "display: none;"


def show(widgets):
    for w in widgets:
        w.style <<= "display: block;"


def show_page(number):
    global page
    page = number

    # hide everything...
    hide(page1)
    hide(page2)
    hide(page3)

    # ...then show just the page we want
    if page == 1:
        show(page1)
    elif page == 2:
        show(page2)
    elif page == 3:
        show(page3)


# ------------------------------------------------------------------
# WHAT THE BUTTONS DO
# ------------------------------------------------------------------
def reset_click():
    username.text = ""
    password.text = ""
    error.text = ""


def login_click():
    if username.text == "" or password.text == "":
        error.text = "Please type a username and a password"
    else:
        error.text = ""
        show_page(2)


def back_click():
    show_page(1)


def submit_click():
    name_out.text = "Name:  " + username.text
    street_out.text = "Street:  " + street.text
    town_out.text = "Town:  " + town.text
    postcode_out.text = "Postcode:  " + postcode.text
    show_page(3)


def restart_click():
    username.text = ""
    password.text = ""
    street.text = ""
    town.text = ""
    postcode.text = ""
    show_page(1)


# pressing <return> does the same as clicking the button
def password_return_pressed():
    login_click()


def postcode_return_pressed():
    submit_click()


# ------------------------------------------------------------------
# START: only page 1 is visible
# ------------------------------------------------------------------
hide(page2)
hide(page3)

go()