# youmakemy-♡-gui
#
# 13 - LABELS: WIDTHS AND WRAPPING
#
# RULES BEING TESTED
#   * no width   -> the label NEVER wraps. One line, as wide as the text.
#   * width set  -> the label wraps at that width and grows taller to fit.
#   * height set -> the label is exactly that tall (text can be clipped).
#   * padding and border must be included in the wrapped height, so the
#     last line of text is never cut off.
#
# WHAT TO LOOK FOR
#   A  every label is a single line (except the one with \n in it)
#   B  same text, three widths: more lines as the width gets smaller
#   C  the LAST line of text is fully visible inside the box, even with
#      lots of padding and a thick border
#   D  first box is clipped on purpose, the long word can't wrap (Qt
#      can't break a word with no spaces), right: / bottom: land where
#      they should
#   E  click the buttons: the labels re-measure themselves as the text grows
#
# NOTE: the window is 1200px wide but the black terminal covers the right
#       third, so  right: 440px  puts a label at the right of the grid area.
#
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label

lorem = "The quick brown fox jumps over the lazy dog and keeps on running through the field."


def box(bg, border):
    """A tinted box with a border so you can see exactly how big each label is."""
    return (
        f"background-color: {bg}; border: 1px solid {border}; border-radius: 6px;"
        "padding: 6px; font-size: 14px; color: #1f2937;"
    )


indigo = box("#eef2ff", "#6366f1")
green = box("#ecfdf5", "#10b981")
orange = box("#fff7ed", "#f97316")
red = box("#fef2f2", "#ef4444")
violet = box("#f5f3ff", "#8b5cf6")

caption = "font-size: 12px; color: #6b7280; background-color: transparent; padding: 0px;"

title = Label("Labels: widths and wrapping")
title.style <<= "left: 20px; top: 6px; font-size: 22px; background-color: transparent;"

# ------------------------------------------------------------------
# A - no width: must never wrap
# ------------------------------------------------------------------
capA = Label("A. No width set: always one line")
capA.style <<= "left: 20px; top: 40px;" + caption

a1 = Label("Short label")
a1.style <<= "left: 20px; top: 60px;" + indigo

a2 = Label("No width set, so this label stays on ONE line however long the text gets")
a2.style <<= "left: 20px; top: 90px;" + indigo

a3 = Label("Emoji 😊🎉 and symbols ⚠ ✔ ♡ don't confuse the sizing")
a3.style <<= "left: 20px; top: 120px;" + indigo

# explicit newlines are fine without wrapping
a4 = Label("Line one\nLine two\nLine three")
a4.style <<= "left: 20px; top: 150px;" + indigo

# min-width with no width: grows to the text but never smaller than 250px
a5 = Label("min-width: 250px, right aligned")
a5.style <<= "left: 200px; top: 150px; min-width: 250px; qproperty-alignment: 'AlignRight';" + indigo

# ------------------------------------------------------------------
# B - same text, three widths
# ------------------------------------------------------------------
capB = Label("B. Width set: wraps at 200px, 300px and 220px")
capB.style <<= "left: 20px; top: 232px;" + caption

b1 = Label(lorem)
b1.style <<= "left: 20px; top: 252px; width: 200px;" + green

b2 = Label(lorem)
b2.style <<= "left: 240px; top: 252px; width: 300px;" + green

b3 = Label(lorem)
b3.style <<= "left: 560px; top: 252px; width: 220px;" + green

# ------------------------------------------------------------------
# C - padding and borders in wrapped labels
# ------------------------------------------------------------------
capC = Label("C. Padding / border: the last line must not be cut off")
capC.style <<= "left: 20px; top: 352px;" + caption

c1 = Label(lorem)
c1.style <<= "left: 20px; top: 372px; width: 220px;" + orange
c1.style <<= "padding: 0px; border: 0px solid #f97316;"

c2 = Label(lorem)
c2.style <<= "left: 260px; top: 372px; width: 220px;" + orange

c3 = Label(lorem)
c3.style <<= "left: 500px; top: 372px; width: 220px;" + orange
c3.style <<= "padding: 20px; border: 4px solid #f97316; border-radius: 16px;"

# ------------------------------------------------------------------
# D - height, long words, right: and bottom:
# ------------------------------------------------------------------
capD = Label("D. height: 40px (clipped on purpose) | unbroken word | right: | bottom:")
capD.style <<= "left: 20px; top: 508px;" + caption

d1 = Label(lorem)
d1.style <<= "left: 20px; top: 528px; width: 200px; height: 40px;" + red

d2 = Label("ThisIsOneVeryLongWordWithNoSpacesAtAll")
d2.style <<= "left: 240px; top: 528px; width: 200px;" + red

d3 = Label("right: 440px, width: 200px")
d3.style <<= "right: 440px; top: 528px; width: 200px;" + red

d4 = Label("bottom: 20px, width: 200px")
d4.style <<= "left: 580px; bottom: 20px; width: 200px;" + red

# ------------------------------------------------------------------
# E - text changes after the window is up
# ------------------------------------------------------------------
capE = Label("E. Change the text while running")
capE.style <<= "left: 20px; top: 596px;" + caption

grow = Button("Grow text")
grow.style <<= "left: 20px; top: 614px; font-size: 14px; padding: 4px 10px;"
grow.style <<= "color: white; background-color: #8b5cf6; border-radius: 6px;"

reset = Button("Reset")
reset.style <<= "left: 130px; top: 614px; font-size: 14px; padding: 4px 10px;"
reset.style <<= "color: white; background-color: #6b7280; border-radius: 6px;"

dyn_wrapped = Label("Wrapped (width 300px). Press Grow text.")
dyn_wrapped.style <<= "left: 20px; top: 654px; width: 300px;" + violet

dyn_single = Label("Single line. Press Grow text.")
dyn_single.style <<= "left: 340px; top: 654px;" + violet


def grow_click():
    dyn_wrapped.text += " More words arrive."
    dyn_single.text += " More."


def reset_click():
    dyn_wrapped.text = "Wrapped (width 300px). Press Grow text."
    dyn_single.text = "Single line. Press Grow text."


go()