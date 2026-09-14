
#import youmakemyheartgui as ♡
# youmakemy-♡-gui
from youmakemyheartgui import go
from youmakemyheartgui.Widgets import Button, Label


msg = Label("Hello world!!")
msg2 = Label("bottom long text here bottom long text herebottom long text herebottom long text herebottom long text herebottom long text herebottom long text here")
msg2.style <<= "top: 480px;"

b = Button("Hello world!!")
b.style = "{background-color: #332233;}"
#b.style <<= "right: 100px;"
#b.style <<= "{ width: 150px; }"
b.style <<= "{background-color: RED;}"

b.style <<= """
    left: 100px;
    top: 100px;
    h-eight: 50px;
    background-color: #4CAF50;
    color: white;
    border-radius: 5px;
    padding: 15px;
    font-size: 17px;
"""
b.state.lives = 0

c = Button("Boo!! 😊")
c.style = """
{
    left: 120px;
    top: 170px;
    width: 150px;
    h-eight: 50px;
    background-color: #4CAF50;
    color: white;
    border-radius: 5px;
    padding: 15px;
}
"""

calc_display = Label("")
calc_display.style <<= "left: 60px; top: 230px; font-size: 22px; min-width: 150px; qproperty-alignment: 'AlignRight';"

calc_style = "height: 40px; font-size: 22px; width: 50px;"
b1 = Button("1")
b1.style = calc_style
b1.style <<= "left: 60px; top: 280px;"

b2 = Button("2")
b2.style = calc_style
b2.style <<= "left: 115px; top: 280px;"

b3 = Button("3")
b3.style = calc_style
b3.style <<= "left: 170px; top: 280px;"

b4 = Button("4")
b4.style = calc_style
b4.style <<= "left: 60px; top: 330px;"

b5 = Button("5")
b5.style = calc_style
b5.style <<= "left: 115px; top: 330px;"

b6 = Button("6")
b6.style = calc_style
b6.style <<= "left: 170px; top: 330px;"

b7 = Button("7")
b7.style = calc_style
b7.style <<= "left: 60px; top: 380px;"

b8 = Button("8")
b8.style = calc_style
b8.style <<= "left: 115px; top: 380px;"

b9 = Button("9")
b9.style = calc_style
b9.style <<= "left: 170px; top: 380px;"

b0 = Button("0")
b0.style = calc_style
b0.style <<= "left: 115px; top: 430px;"

add = Button("+")
add.style = calc_style
add.style <<= "left: 220px; top: 380px; background-color: pink"

eq = Button("=")
eq.style = calc_style
eq.style <<= "left: 220px; top: 430px; background-color: #CBC3E3"


total = 0
nums = []

def add_click():
    if len(calc_display.text) > 0:
        nums.append(int(calc_display.text))
        print(f"Nums is {nums}")
        
    calc_display.text = ""

def eq_click():
    # the user may have typed some new numbers
    # after they clicked "+"
    add_click()

    calc_display.text = str(sum(nums))


def b1_click():
    calc_append(1)
    
def b2_click():
    calc_append(2)

def b3_click():
    calc_append(3)

def b4_click():
    calc_append(4)

def b5_click():
    calc_append(5)

def b6_click():
    calc_append(6)

def b7_click():
    calc_append(7)

def b8_click():
    calc_append(8)

def b9_click():
    calc_append(9)

def b0_click():
    calc_append(0)

def calc_append(value):
    calc_display.text += str(value)

def b_click():
    print("clicked!")
    msg.text = "You look very nice today!!"

def c_click():
    if not hasattr(c_click, 'count'):
        c_click.count = 0

    c_click.count += 1
    print(f"c clicked {c_click.count} times! 😊")

    print("B is", b)

    b.state.lives += 1
    if c_click.count % 2:
        b.style <<= "{background-color: RED;}"
        b.style <<= "left: 30px;"
        b.text = f"Lives: {b.state.lives}"
    else:
        b.style <<= "{background-color: GREEN;}"
        b.style <<= "left: 70px;"
        b.text = f"Lives: {b.state.lives} very very very long text"

    msg.text = "c clicked!!"



go()
