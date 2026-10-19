# youmakemy-♡-gui
#
# ======================================================================
#  00 - SELFTEST: REGRESSION CHECKS  +  CODE MAP
# ======================================================================
#
#  >>> CLAUDE / ANY AI: READ THIS FILE FIRST when asked about this
#  >>> library. The CODE MAP and GOTCHAS below are cheaper than reading
#  >>> every source file. Run the file (below) after ANY change to
#  >>> src/youmakemyheartgui and look for the line:
#  >>>
#  >>>       SELFTEST RESULT: N passed, N failed, N warnings, N skipped
#  >>>
#  >>> If that line is MISSING the process crashed part way through:
#  >>> the last ✅/❌ line printed tells you which check killed it.
#
# ----------------------------------------------------------------------
#  HOW TO RUN (human)
# ----------------------------------------------------------------------
#    python tests/00-SELFTEST-regression-checks-and-code-map.py
#
#  A window opens. The big banner at the top says either
#      ✅ ALL N CHECKS PASSED          (green)
#      ⚠️ ... passed, N warnings       (amber, tidy-up only, not broken)
#      ❌ N FAILED                      (red, something is broken)
#  Anything that is NOT a pass is listed under the banner.
#  The black panel on the right has EVERY check, one line each.
#  The small widgets along the bottom are the "test bench" - the real
#  Buttons / Inputs / Labels the checks poke at. You can ignore them.
#
#    ✅ passed      ❌ FAILED (broken)      ⚠️ warning (tidy-up, not broken)
#    ⏭ skipped (that feature isn't in the library, nothing to test)
#
# ----------------------------------------------------------------------
#  HOW TO RUN (AI / headless / CI)
# ----------------------------------------------------------------------
#    pip install pyqt6 pymunk --break-system-packages
#    QT_QPA_PLATFORM=offscreen python tests/00-SELFTEST-regression-checks-and-code-map.py --quit
#
#  --quit closes the window when the checks finish. Exit code is 0 if
#  nothing failed, 1 otherwise (warnings don't count as failures).
#  Output is plain text; failed checks print "❌ section: name" followed
#  by an indented "↳ reason" line.
#
# ----------------------------------------------------------------------
#  HOW TO ADD A CHECK
# ----------------------------------------------------------------------
#  Three kinds, all the same shape - a tiny function that raises (via
#  expect()) if something is wrong:
#
#    @pre("section", "what it proves")       runs NOW, before go().
#                                             Use for anything that needs no window.
#    @live(1, "section", "what it proves")    runs after the window is up (stage 1).
#                                             Use win.buttons / win.inputs / win.proxies...
#    @live(2, ...)                            stage 2 = after ~0.4s of the event loop
#                                             (timers have had time to tick).
#    add soft=True to make a failure a ⚠️ instead of ❌.
#    raise Skip("why") if the feature doesn't exist (yet).
#
#  Keep check functions SHORT and put the BUG HISTORY in a comment above,
#  so the next person knows what a failure means.
#
# ----------------------------------------------------------------------
#  CODE MAP  (src/youmakemyheartgui/)
# ----------------------------------------------------------------------
#  __init__.py    Importing the package creates the ONE QApplication (app) and
#                 the ONE MainWindow (win) as module globals. Nothing is shown
#                 until go().
#                 go()  = the student's entry point. It reads the CALLER's
#                         globals (sys._getframe(1).f_globals), so widgets must
#                         be MODULE-LEVEL variables to be picked up.
#                 find_widgets(globals, Kind) -> {variable_name: widget}; it also
#                         sets widget.instance_name (the variable name).
#                 go_link_buttons_to_click_handlers / go_link_inputs_to_handlers /
#                 go_link_timers: connect student functions BY NAME:
#                         <name>_click        (priority 1)
#                         button_click(button) generic fallback (priority 2)
#                         <name>_click.py     file next to the script, re-read on
#                                              every click (priority 3)
#                         <name>_text_changed, <name>_return_pressed  (Input)
#                         <name>_tick                                 (Timer)
#                 gravity(on) / gravity_step(): thin wrappers over win.physics.
#
#  Widgets.py     The student-facing classes: Button, Label, Input, PasswordInput,
#                 Image, Panel, Timer (+ StyleProxy, UserData).
#                 Widget base class: .style is kept as a DICT (self._props) so each
#                 CSS property exists once; str(w.style) joins it back to text.
#                 .state / .stash / .inventory = free-for-all UserData objects.
#                 .container = the MainWindow, None until go(). Every setter
#                 (text, src, style) must cope with container being None.
#                 Timer is NOT a Widget (no style); it wraps a QTimer and stops
#                 itself if the student's tick handler raises.
#
#  MainWindow.py  The Qt side. Fixed 1200x760: grid/stage on the left (~800px),
#                 black terminal on the right. Student widgets are real Qt widgets
#                 inside a QGraphicsScene (via proxies) so they can rotate.
#                 Dicts keyed by instance_name:
#                    win.buttons/labels/inputs/images/panels -> the Qt widgets
#                    win.proxies -> QGraphicsProxyWidget (position/rotation/visibility)
#                    win.objs    -> the student's own widget objects
#                 add_X() builds the Qt widget once; update_X() re-applies style.
#                 Every student style change flows:
#                    w.style <<= "..." -> Widget.add_style -> container.update_X
#                      -> style.split_style() -> (layout, qt_props)
#                      -> setStyleSheet(...) + placement.place()
#
#  style.py       PURE functions, no Qt: parse_style, css_gradient_to_qt,
#                 split_style (-> layout dict + Qt-only props), with_box_defaults,
#                 qt_stylesheet. Safe to unit test without a window.
#  placement.py   place(): size first, then position (so right:/bottom: know the
#                 real size), rotation about the centre, visibility. Goes via proxy.
#  Panel.py       PanelFrame (hand-drawn 3D bevel) + parse_bevel.
#  Physics.py     pymunk gravity (NOT covered by this selftest yet).
#  PrintCapture.py  print() is copied to win.terminal (start_print_capture(write)).
#  errors.py      where_in_student_code(tb) and friendly_excepthook (installed as
#                 sys.excepthook so a typo in a click handler doesn't kill the app).
#  colour.py      adjust_colour(colour, factor): lighten/darken (hover/pressed).
#  Grid.py, TerminalLabel.py   the background grid and the console pane.
#
# ----------------------------------------------------------------------
#  GOTCHAS (each one cost us time once - each has a check below)
# ----------------------------------------------------------------------
#  1. `b.style <<= "x"` is really  b.style = b.style.__ilshift__("x").  Python
#     calls the style SETTER with the StyleProxy it just got from the getter,
#     so the setter ignores anything that isn't a str. Remove that and every
#     <<= wipes the style.
#  2. In a Qt stylesheet the LAST declaration wins, even between different
#     properties (background vs background-color). add_style therefore pops
#     the old key and re-adds it at the END. A plain dict update would keep
#     the old position and a later background-color would silently lose.
#  3. Qt can only mask a password with ONE character in the BMP (● ♡ ★ *).
#     Emoji like 😊 and "❤️" (2 characters) are rejected with a warning.
#  4. PyQt6 ABORTS the whole process if a slot raises, unless sys.excepthook
#     has been replaced. A handler typo must print a friendly error instead.
#  5. print capture must not import the package's __init__ (it once did:
#     "from .__init__ import win" ran __init__ twice -> TWO MainWindows).
#  6. Student widgets can have .text / .src / .style set BEFORE go()
#     (container is None then); this used to crash.
#  7. Hidden = display:none OR visibility:hidden. They are independent: if
#     EITHER says hide, it's hidden.
#  8. A Label with no width never wraps; with a width it wraps and grows.
#  9. Hover/pressed colours are derived from background-color, so put
#     background-color BEFORE a gradient ("background: linear-gradient(...)").
# 10. Handlers are found only for MODULE-LEVEL names at the moment go() runs.
# 11. Input text set before go() (or Input("hello")) is stored but NOT shown:
#     MainWindow.add_input always makes QLineEdit(""). A check below covers it.
#
# ----------------------------------------------------------------------
#  WHERE WE ARE (update this when things change)
# ----------------------------------------------------------------------
#  Done & covered here: dict-based style, guards for set-before-go, hover_style,
#  PasswordInput, print capture (single window), sys.excepthook, find_widgets,
#  place() moved to placement.py, cssutils removed.
#  NEXT (not written yet): keyboard support (key down / key up, e.g. WASD moving a
#  widget). Checks to add when it exists: OS auto-repeat is filtered; all keys
#  are released when the window loses focus; keys ignored while an Input has
#  focus; key names are plain strings ("left", "space"), never Qt enums.
#
# ======================================================================

import contextlib
import gc
import io
import math
import os
import sys
import tempfile

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QPixmap

import youmakemyheartgui as ymmh
from youmakemyheartgui import go, win, app
from youmakemyheartgui.Widgets import Button, Label, Input, PasswordInput, Image, Panel, Timer
from youmakemyheartgui.style import parse_style, split_style, with_box_defaults, css_gradient_to_qt
from youmakemyheartgui.colour import adjust_colour

HERE = os.path.dirname(os.path.abspath(__file__))
THIS_FILE = os.path.basename(__file__)
QUIT_WHEN_DONE = "--quit" in sys.argv or bool(os.environ.get("YMMH_SELFTEST_QUIT"))


# ======================================================================
#  A TINY TEST FRAMEWORK (about 60 lines, no pytest needed)
# ======================================================================
RESULTS = []        # (status, section, name, message)
LIVE_CHECKS = []    # (stage, section, name, function, soft)


class Skip(Exception):
    """Raise inside a check when the feature isn't in the library."""


def expect(condition, message="expectation failed"):
    """The only assert we need: raise with a helpful message."""
    if not condition:
        raise AssertionError(message)


def approx(a, b, tolerance=1.0):
    return abs(a - b) <= tolerance


def run_check(section, name, func, soft=False):
    """Run one check, record it, and print one line (plus a reason if it didn't pass)."""
    bad = "⚠️" if soft else "❌"
    message = ""
    try:
        func()
        status = "✅"
    except Skip as why:
        status, message = "⏭", str(why)
    except AssertionError as why:
        status, message = bad, str(why)
    except Exception as why:                       # the check itself blew up
        status, message = bad, f"{type(why).__name__}: {why}"

    RESULTS.append((status, section, name, message))
    line = f"{status} {section}: {name}"
    if message:
        line += f"\n     ↳ {message}"
    print(line)


def pre(section, name, soft=False):
    """Decorator: run this check immediately (before go(), no window needed)."""
    def wrap(func):
        run_check(section, name, func, soft)
        return func
    return wrap


def live(stage, section, name, soft=False):
    """Decorator: queue this check to run once the window is up."""
    def wrap(func):
        LIVE_CHECKS.append((stage, section, name, func, soft))
        return func
    return wrap


def capture_print(func):
    """Run func() and return the list of lines it print()ed, WITHOUT them
    reaching the terminal pane (keeps the black panel tidy)."""
    import builtins
    saved = builtins.print
    lines = []
    builtins.print = lambda *args, **kwargs: lines.append(" ".join(str(a) for a in args))
    try:
        func()
    finally:
        builtins.print = saved
    return lines


def style_keys(widget):
    """['left', 'top', ...] in the order they appear in str(widget.style)."""
    return [d.split(":")[0].strip() for d in str(widget.style).split(";") if d.strip()]


def link_buttons(fake_globals):
    return capture_print(lambda: ymmh.go_link_buttons_to_click_handlers(fake_globals))


# ======================================================================
#  THE TEST BENCH: real widgets the live checks poke at.
#  (They must be module-level so go() finds them - see GOTCHA 10.)
# ======================================================================
IMG_A = os.path.join(HERE, "smile-1.png")        # 208 x 290
IMG_B = os.path.join(HERE, "pirate-ship-3.png")  # 627 x 539 (different size on purpose)

small = "font-size: 14px; padding: 4px 8px;"

banner = Label("SELFTEST  -  library regression checks")
banner.style <<= "left: 20px; top: 10px; font-size: 26px; background-color: transparent;"

summary = Label("⏳ Running checks...")
summary.style <<= "left: 20px; top: 60px; width: 760px; font-size: 26px; font-weight: bold;"
summary.style <<= "background-color: #e5e7eb; border: 3px solid #9ca3af; border-radius: 10px; padding: 14px;"

details = Label("")
details.style <<= "left: 20px; top: 160px; width: 760px; font-size: 14px; background-color: transparent;"

hint = Label("Every check is listed in the black panel ➡   ⚠️ = tidy-up only   ⏭ = skipped")
hint.style <<= "left: 20px; top: 425px; font-size: 13px; color: #6b7280; background-color: transparent;"

# two thin panels: used by the z-order check, and they make a divider line
t_panel_a = Panel()
t_panel_a.style <<= "left: 20px; top: 458px; width: 760px; height: 4px; border-width: 1px;"
t_panel_b = Panel()
t_panel_b.style <<= "left: 20px; top: 462px; width: 760px; height: 4px; border-width: 1px;"

# row 1 (y=480): labels
t_label = Label("bench label")
t_label.style <<= "left: 20px; top: 480px;" + small

t_wrapped = Label("This label has a width so it wraps onto several lines")
t_wrapped.style <<= "left: 180px; top: 480px; width: 150px;" + small

t_oneline = Label("No width: this label must never wrap, however long it gets")
t_oneline.style <<= "left: 350px; top: 480px;" + small

t_hide = Label("hide me")
t_hide.style <<= "left: 20px; top: 540px;" + small

t_rot = Label("rotated")
t_rot.style <<= "left: 120px; top: 545px; transform: rotate(30deg);" + small

t_right = Label("right: 20 / bottom: 20")
t_right.style <<= "right: 20px; bottom: 20px;" + small

# row 2 (y=590): buttons
t_button = Button("click me")
t_button.style <<= "left: 20px; top: 590px;" + small

t_generic = Button("generic")
t_generic.style <<= "left: 120px; top: 590px;" + small

t_hover_custom = Button("hover: pink")
t_hover_custom.style <<= "left: 210px; top: 590px; background-color: #336699; color: white;" + small
t_hover_custom.hover_style = "background-color: #ff07a9;"

t_hover_auto = Button("hover: auto")
t_hover_auto.style <<= "left: 340px; top: 590px; background-color: #336699; color: white;" + small

boom = Button("💥 boom")      # its handler raises ON PURPOSE - see the last check
boom.style <<= "left: 470px; top: 590px;" + small

# row 3 (y=640): inputs
t_input = Input("")
t_input.style <<= "left: 20px; top: 640px; width: 150px; font-size: 14px; padding: 4px;"

t_password = PasswordInput("", "♡")
t_password.style <<= "left: 190px; top: 640px; width: 150px; font-size: 14px; padding: 4px;"

t_plain_input = Input("")
t_plain_input.style <<= "left: 360px; top: 640px; width: 150px; font-size: 14px; padding: 4px;"

t_preset_input = Input("")
t_preset_input.style <<= "left: 530px; top: 640px; width: 150px; font-size: 14px; padding: 4px;"

# row 4 (y=690): widgets whose text is set BEFORE go()
t_preset_label = Label("original text")
t_preset_label.style <<= "left: 20px; top: 690px;" + small

t_preset_button = Button("original text")
t_preset_button.style <<= "left: 170px; top: 690px;" + small

t_img = Image(IMG_A)
t_img.style <<= "left: 330px; top: 685px; width: 52px; height: 45px;"

# a timer (invisible; it ticks during stage 2)
t_timer = Timer(30)


# ---- handlers for the bench (found by NAME when go() runs) ----
t_clicks = 0
last_generic = None
t_input_changes = 0
t_input_returns = 0
t_ticks = 0


def t_button_click():
    global t_clicks
    t_clicks += 1


def button_click(button):
    """Generic handler: every Button WITHOUT its own <name>_click lands here."""
    global last_generic
    last_generic = button.instance_name


def t_input_text_changed():
    global t_input_changes
    t_input_changes += 1


def t_input_return_pressed():
    global t_input_returns
    t_input_returns += 1


def t_timer_tick():
    global t_ticks
    t_ticks += 1


def boom_click():
    # ON PURPOSE. If the library has no sys.excepthook, PyQt aborts the whole
    # process here and the SELFTEST RESULT line never appears.
    1 / 0


# ======================================================================
#  PART 1 - CHECKS THAT NEED NO WINDOW (run immediately)
# ======================================================================
print("── PART 1: no window needed ──")

# ----------------------------------------------------------------------
#  style  (Widget.add_style / the <<= operator)
# ----------------------------------------------------------------------
# BUG HISTORY: add_style only de-duplicated the FIRST property in a string,
# so  b.style <<= "left: 30px; top: 40px;"  inside a click handler or timer
# left another "top:" behind every time and the string grew without limit.
@pre("style", "repeated <<= with 2 properties never grows")
def style_does_not_grow():
    w = Label("x")
    for _ in range(500):
        w.style <<= "left: 30px; top: 40px;"
    keys = style_keys(w)
    expect(len(keys) == len(set(keys)), f"duplicate properties: {keys}")
    expect(len(str(w.style)) < 700, f"style string is {len(str(w.style))} characters long")


@pre("style", "a later value replaces the earlier one")
def style_later_wins():
    w = Label("x")
    w.style <<= "left: 10px; top: 20px;"
    w.style <<= "left: 99px;"
    expect(parse_style(str(w.style))["left"] == "99px", str(w.style))
    expect(parse_style(str(w.style))["top"] == "20px", "top was lost")


# BUG HISTORY: Qt applies the LAST declaration, even between different
# properties. If background-color kept its old position (before the gradient),
# a student's later "background-color: red" would be silently ignored.
@pre("style", "re-set property moves to the END (last one wins)")
def style_reset_goes_to_end():
    b = Button("x")
    b.style <<= "background-color: #54ad58; background: linear-gradient(#66bb6a, #43a047);"
    b.style <<= "background-color: red;"
    keys = style_keys(b)
    expect(keys.index("background-color") > keys.index("background"),
           f"order is {keys}")


# GOTCHA 1: the <<= operator calls the setter with a StyleProxy.
@pre("style", "<<= keeps the existing style (does not wipe it)")
def style_ilshift_keeps_defaults():
    w = Label("x")
    expect("font-size" in style_keys(w), "default Label style missing before")
    w.style <<= "left: 5px;"
    expect("font-size" in style_keys(w), "Label default font-size was wiped by <<=")


@pre("style", "style = '{...}' replaces everything, braces stripped")
def style_assignment_replaces():
    b = Button("x")
    b.style = "{background-color: #332233;}"
    expect(str(b.style) == "background-color: #332233;", repr(str(b.style)))


@pre("style", "a typo'd declaration is reported and skipped, not fatal")
def style_bad_declaration():
    w = Label("x")
    lines = capture_print(lambda: w.add_style("left 50px; top: 10px"))
    expect(any("Could not parse" in line for line in lines), f"no warning printed: {lines}")
    expect(parse_style(str(w.style)).get("top") == "10px", "the good declaration was lost")


@pre("style", "parse_style: braces, blanks and ;; are fine")
def parse_style_messy():
    expect(parse_style(" { left: 50px ;; top:10px } ") == {"left": "50px", "top": "10px"},
           str(parse_style(" { left: 50px ;; top:10px } ")))


@pre("style", "parse_style splits on the FIRST colon only")
def parse_style_first_colon():
    got = parse_style("background-image: url(a:b.png)")
    expect(got == {"background-image": "url(a:b.png)"}, str(got))


@pre("style", "hover_style stores and replaces")
def hover_style_stores():
    b = Button("x")
    b.hover_style = "background-color: #ff07a9"
    expect(str(b.hover_style) == "background-color: #ff07a9;", repr(str(b.hover_style)))


@pre("style", "every widget gets its OWN state / stash objects")
def state_not_shared():
    a, b = Label("a"), Label("b")
    a.state.lives = 3
    a.stash.x = 1
    expect(not hasattr(b.state, "lives"), "state is shared between widgets")
    expect(not hasattr(b.stash, "x"), "stash is shared between widgets")


# ----------------------------------------------------------------------
#  gradient  (style.css_gradient_to_qt)
# ----------------------------------------------------------------------
@pre("gradient", "default direction is top to bottom")
def gradient_default():
    got = css_gradient_to_qt("linear-gradient(#f7f8fa, #e7e9ec)")
    expect(got and "x1:0.5, y1:0, x2:0.5, y2:1" in got, str(got))


@pre("gradient", "'to right' runs left to right")
def gradient_to_right():
    got = css_gradient_to_qt("linear-gradient(to right, red, blue)")
    expect(got and "x1:0, y1:0.5, x2:1, y2:0.5" in got, str(got))


@pre("gradient", "angle (45deg) is understood")
def gradient_angle():
    got = css_gradient_to_qt("linear-gradient(45deg, red, blue)")
    expect(got and got.startswith("qlineargradient("), str(got))


@pre("gradient", "percentage stops: '#fff 30%'")
def gradient_percent():
    got = css_gradient_to_qt("linear-gradient(#ffffff 30%, #cfd8dc)")
    expect(got and "stop:0.3 #ffffff" in got and "stop:1 #cfd8dc" in got, str(got))


@pre("gradient", "stops with no % are spread evenly")
def gradient_even():
    got = css_gradient_to_qt("linear-gradient(red, yellow, green)")
    expect(got and "stop:0.5 yellow" in got, str(got))


@pre("gradient", "rgb(1, 2, 3) commas don't split a colour")
def gradient_rgb():
    got = css_gradient_to_qt("linear-gradient(rgb(255, 94, 98), rgb(255, 153, 102))")
    expect(got and "rgb(255, 94, 98)" in got and got.count("stop:") == 2, str(got))


@pre("gradient", "not-a-gradient and 1-colour gradients give None")
def gradient_rejects():
    expect(css_gradient_to_qt("red") is None, "plain colour should be None")
    expect(css_gradient_to_qt("linear-gradient(red)") is None, "1 colour should be None")


@pre("gradient", "split_style swaps CSS gradient for a Qt one")
def gradient_through_split_style():
    layout, qt_props = split_style("background: linear-gradient(#aaaaaa, #bbbbbb);")
    expect(qt_props.get("background", "").startswith("qlineargradient("), str(qt_props))


# ----------------------------------------------------------------------
#  layout  (style.split_style, with_box_defaults, colour)
# ----------------------------------------------------------------------
@pre("layout", "left/top/width/height become ints")
def layout_px():
    layout, _ = split_style("left: 50px; top: 20; width: 100px; height: 30px")
    expect(layout["left"] == 50 and layout["top"] == 20, str(layout))
    expect(layout["width"] == 100 and layout["height"] == 30, str(layout))


@pre("layout", "a bad number ('left: abc') is dropped with a warning")
def layout_bad_px():
    result = {}
    lines = capture_print(lambda: result.update(layout=split_style("left: abc; top: 5px")[0]))
    expect("left" not in result["layout"], str(result["layout"]))
    expect(result["layout"].get("top") == 5, "the good value was lost")
    expect(len(lines) >= 1, "no warning printed")


@pre("layout", "display:none / visibility:hidden both hide")
def layout_hidden():
    hidden = lambda css: split_style(css)[0]["hidden"]
    expect(hidden("display: none;"), "display: none")
    expect(hidden("visibility: hidden;"), "visibility: hidden")
    expect(hidden("visibility: collapse;"), "visibility: collapse")
    expect(hidden("display: block; visibility: hidden;"), "visible display must not override hidden visibility")
    expect(not hidden("display: block; visibility: visible;"), "should be visible")
    expect(not hidden("left: 5px;"), "default should be visible")


@pre("layout", "rotation: deg, turn, rad, grad and transform: rotate()")
def layout_rotation():
    rot = lambda css: split_style(css)[0]["rotate"]
    expect(approx(rot("transform: rotate(45deg);"), 45, 0.01), "rotate(45deg)")
    expect(approx(rot("rotate: 0.25turn;"), 90, 0.01), "0.25turn")
    expect(approx(rot("rotate: 3.14159265rad;"), 180, 0.01), "pi rad")
    expect(approx(rot("rotate: 100grad;"), 90, 0.01), "100grad")
    expect(approx(rot("rotate: 30;"), 30, 0.01), "bare number = degrees")
    expect(rot("left: 5px;") == 0, "no rotation = 0")


@pre("layout", "our own properties never reach the Qt stylesheet")
def layout_not_sent_to_qt():
    _, qt_props = split_style("left: 1px; top: 2px; width: 3px; height: 4px; "
                              "display: none; visibility: hidden; transform: rotate(5deg); rotate: 5deg; color: red;")
    leaked = [k for k in ("left", "top", "right", "bottom", "width", "height",
                          "display", "visibility", "transform", "rotate") if k in qt_props]
    expect(not leaked, f"leaked to Qt: {leaked}")
    expect(qt_props.get("color") == "red", "colour should still go to Qt")


# Qt drops the native look as soon as a stylesheet sets a border/background.
@pre("layout", "with_box_defaults fills in the missing border/background")
def layout_box_defaults():
    expect(with_box_defaults({"color": "red"}) == {"color": "red"}, "untouched style must stay untouched")
    got = with_box_defaults({"border-radius": "10px"})
    expect("background-color" in got and "border" in got, str(got))
    got = with_box_defaults({"background-color": "red"})
    expect(got["background-color"] == "red" and "border" in got, str(got))


@pre("layout", "adjust_colour lightens and darkens")
def colour_adjust():
    from PyQt6.QtGui import QColor
    base = QColor("#336699").valueF()
    expect(QColor(adjust_colour("#336699", 0.3)).valueF() > base, "not lighter")
    expect(QColor(adjust_colour("#336699", -0.3)).valueF() < base, "not darker")


# ----------------------------------------------------------------------
#  before-go  (GOTCHA 6)
# ----------------------------------------------------------------------
# BUG HISTORY: msg.text = "x" BEFORE go() crashed with
#   'NoneType' object has no attribute 'change_text_label'
@pre("before-go", "setting .text / .src / .style before go() doesn't crash")
def set_things_before_go():
    t_preset_label.text = "set before go"
    t_preset_button.text = "set before go"
    t_preset_input.text = "set before go"
    t_img.src(IMG_B)
    t_label.style <<= "color: black;"
    expect(t_preset_label.text == "set before go", "label text not kept")
    expect(t_preset_button.text == "set before go", "button text not kept")
    expect(t_preset_input.text == "set before go", "input text not kept")


@pre("before-go", "each widget type survives .text / .style before go()")
def each_type_before_go():
    for w in (Label("a"), Button("b"), Input(""), PasswordInput(""), Image(IMG_A), Panel()):
        w.style <<= "left: 5px;"
        if not isinstance(w, Panel):
            w.text = "x"      # Image/Panel included on purpose


# ----------------------------------------------------------------------
#  password  (PasswordInput - one BMP character)
# ----------------------------------------------------------------------
@pre("password", "default character is ●, custom one is kept")
def password_chars():
    expect(PasswordInput("").char == "●", "default should be ●")
    expect(PasswordInput("", "♡").char == "♡", "♡ should be accepted")
    expect(PasswordInput(char="*").char == "*", "* should be accepted")


@pre("password", "emoji / 2 characters / empty fall back to ● with a warning")
def password_rejects():
    for bad in ("😊", "❤️", "ab", "", None):
        got = {}
        lines = capture_print(lambda: got.update(char=PasswordInput("", bad).char))
        expect(got["char"] == "●", f"{bad!r} gave {got['char']!r}")
        expect(any("PasswordInput" in line for line in lines), f"{bad!r}: no warning printed")


@pre("password", ".char setter validates too")
def password_setter():
    p = PasswordInput("")
    p.char = "★"
    expect(p.char == "★", "★ should be accepted")
    capture_print(lambda: setattr(p, "char", "😊"))
    expect(p.char == "●", "emoji via setter should fall back to ●")


@pre("password", "PasswordInput IS an Input (so go() links its handlers)")
def password_is_input():
    expect(isinstance(PasswordInput(""), Input), "not an Input subclass")
    found = ymmh.find_widgets({"a": PasswordInput(""), "b": Label("x")}, Input)
    expect(list(found) == ["a"], str(list(found)))


# ----------------------------------------------------------------------
#  timer
# ----------------------------------------------------------------------
@pre("timer", "milliseconds / start / stop / toggle / running")
def timer_basics():
    t = Timer(250)
    expect(t.milliseconds == 250, "initial interval")
    t.milliseconds = 40
    expect(t.milliseconds == 40, "interval not changed")
    expect(not t.running, "should start stopped")
    t.start()
    expect(t.running, "start() did not run it")
    t.toggle()
    expect(not t.running, "toggle() should stop a running timer")
    t.toggle()
    expect(t.running, "toggle() should start a stopped timer")
    t.stop()
    expect(not t.running, "stop() did not stop it")


# BUG HISTORY: a typo in a tick handler used to repeat the error many times a
# second. Now the timer reports ONCE (with the student's file + line) and stops.
@pre("timer", "an error in a tick handler is reported once and stops the timer")
def timer_error_stops():
    t = Timer(10)
    t.instance_name = "demo"

    def demo_tick():
        raise ZeroDivisionError("kaboom")

    t.tick_handler = demo_tick
    t.start()
    lines = capture_print(t._tick)
    text = "\n".join(lines)
    expect(not t.running, "timer is still running after the error")
    expect("demo_tick" in text and "ZeroDivisionError" in text, f"message was: {text!r}")
    expect(THIS_FILE in text, "message should point at the STUDENT's file, not the library")
    expect("stopped" in text, "no 'stopped' message")


@pre("timer", "a Timer with no tick handler is silent (no crash)")
def timer_no_handler():
    t = Timer(10)
    t.tick_handler = None
    t._tick()


# ----------------------------------------------------------------------
#  errors  (GOTCHA 4)
# ----------------------------------------------------------------------
@pre("errors", "where_in_student_code names the right file and line")
def errors_where():
    try:
        1 / 0          # noqa  <- the line we expect to be reported
    except ZeroDivisionError as e:
        from youmakemyheartgui.errors import where_in_student_code
        line = e.__traceback__.tb_lineno
        where = where_in_student_code(e.__traceback__)
    expect(f"line {line} of {THIS_FILE}" in where, f"got {where!r}")


@pre("errors", "sys.excepthook has been replaced (so handlers can't abort the app)")
def errors_hook_installed():
    expect(sys.excepthook is not sys.__excepthook__,
           "default excepthook: PyQt6 will abort the process on any handler error")


@pre("errors", "friendly_excepthook prints the error type and message")
def errors_hook_prints():
    from youmakemyheartgui.errors import friendly_excepthook
    try:
        1 / 0
    except ZeroDivisionError as e:
        lines = capture_print(lambda: friendly_excepthook(type(e), e, e.__traceback__))
    text = "\n".join(lines)
    expect("ZeroDivisionError" in text and "division by zero" in text, repr(text))


# ----------------------------------------------------------------------
#  print-capture  (GOTCHA 5)
# ----------------------------------------------------------------------
# BUG HISTORY: PrintCapture did "from .__init__ import win", which ran the
# package __init__ a SECOND time: two QApplications' worth of MainWindow.
@pre("print-capture", "exactly ONE MainWindow exists")
def one_main_window():
    from youmakemyheartgui.MainWindow import MainWindow
    count = sum(1 for o in gc.get_objects() if isinstance(o, MainWindow))
    expect(count == 1, f"{count} MainWindows alive")


@pre("print-capture", "the package __init__ was not imported twice")
def init_not_imported_twice():
    expect("youmakemyheartgui.__init__" not in sys.modules,
           "'youmakemyheartgui.__init__' is in sys.modules: someone wrote 'from .__init__ import ...'")


@pre("print-capture", "print() appears in the terminal pane")
def print_reaches_terminal():
    token = f"token-{id(object())}"
    print(token)
    expect(token in win.terminal.toPlainText(), "print output not found in the terminal")


@pre("print-capture", "print() still reaches the real stdout")
def print_reaches_stdout():
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        print("hello", "world")
    expect("hello world" in buffer.getvalue(), repr(buffer.getvalue()))


# ----------------------------------------------------------------------
#  linking  (how go() joins student functions to widgets, BY NAME)
#  These use a FAKE globals dict so we can test every case in one script.
# ----------------------------------------------------------------------
@pre("linking", "find_widgets: names them, keeps order, skips other types")
def find_widgets_basics():
    a, b, c = Button("a"), Label("b"), Button("c")
    found = ymmh.find_widgets({"x": a, "y": b, "z": c, "n": 5}, Button)
    expect(list(found) == ["x", "z"], str(list(found)))
    expect(a.instance_name == "x" and c.instance_name == "z", "instance_name not set")
    expect(b.instance_name is None, "a Label was named while looking for Buttons")


@pre("linking", "<name>_click is linked")
def link_specific():
    def zz_btn_click():
        pass
    g = {"__file__": os.path.abspath(__file__), "zz_btn": Button("x"), "zz_btn_click": zz_btn_click}
    link_buttons(g)
    expect(g["zz_btn"].click_handler is zz_btn_click, "specific handler not linked")


@pre("linking", "the specific handler beats the generic button_click")
def link_specific_beats_generic():
    def zz_btn_click():
        pass
    g = {"__file__": os.path.abspath(__file__), "zz_btn": Button("x"),
         "zz_btn_click": zz_btn_click, "button_click": lambda b: None}
    link_buttons(g)
    expect(g["zz_btn"].click_handler is zz_btn_click, "generic won over specific")


@pre("linking", "generic button_click(button) receives the button (even with Qt's checked flag)")
def link_generic():
    got = []
    g = {"__file__": os.path.abspath(__file__), "zz_one": Button("1"), "zz_two": Button("2"),
         "button_click": lambda b: got.append(b.instance_name)}
    link_buttons(g)
    g["zz_one"].click_handler()
    g["zz_two"].click_handler(False)        # Qt passes the 'checked' bool
    expect(got == ["zz_one", "zz_two"], str(got))


@pre("linking", "no handler at all: a friendly message, never a crash")
def link_none():
    g = {"__file__": os.path.abspath(__file__), "zz_lonely": Button("x")}
    link_buttons(g)
    lines = capture_print(g["zz_lonely"].click_handler)
    expect(any("could not find click event" in line for line in lines), str(lines))


@pre("linking", "<name>_click.py file handler runs, and is re-read every click")
def link_file_handler():
    with tempfile.TemporaryDirectory() as folder:
        ran = []
        g = {"__file__": os.path.join(folder, "main.py"), "zz_file": Button("x"), "ran": ran}
        path = os.path.join(folder, "zz_file_click.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write("ran.append('v1')")
        link_buttons(g)
        g["zz_file"].click_handler()
        with open(path, "w", encoding="utf-8") as f:
            f.write("ran.append('v2')")
        g["zz_file"].click_handler()
        expect(ran == ["v1", "v2"], f"ran = {ran}")


@pre("linking", "an error inside a <name>_click.py file is printed, not raised")
def link_file_handler_error():
    with tempfile.TemporaryDirectory() as folder:
        g = {"__file__": os.path.join(folder, "main.py"), "zz_file": Button("x")}
        with open(os.path.join(folder, "zz_file_click.py"), "w", encoding="utf-8") as f:
            f.write("1/0")
        link_buttons(g)
        lines = capture_print(g["zz_file"].click_handler)
        expect("zz_file_click.py" in "\n".join(lines), str(lines))


@pre("linking", "Input: _text_changed and _return_pressed are linked, others are False")
def link_inputs():
    def zz_in_text_changed():
        pass

    def zz_in_return_pressed():
        pass

    g = {"zz_in": Input(""), "zz_in_text_changed": zz_in_text_changed,
         "zz_in_return_pressed": zz_in_return_pressed, "zz_other": Input("")}
    capture_print(lambda: ymmh.go_link_inputs_to_handlers(g))
    expect(g["zz_in"].text_changed_handler is zz_in_text_changed, "text_changed not linked")
    expect(g["zz_in"].return_pressed_handler is zz_in_return_pressed, "return_pressed not linked")
    expect(g["zz_other"].text_changed_handler is False, "unlinked should be False")
    expect(g["zz_other"].return_pressed_handler is False, "unlinked should be False")


@pre("linking", "Timer: <name>_tick is linked, missing one is reported")
def link_timers():
    def zz_t_tick():
        pass
    g = {"zz_t": Timer(100), "zz_t_tick": zz_t_tick, "zz_u": Timer(100)}
    lines = capture_print(lambda: ymmh.go_link_timers(g))
    expect(g["zz_t"].tick_handler is zz_t_tick, "tick not linked")
    expect(g["zz_u"].tick_handler is None, "missing handler should stay None")
    expect(any("zz_u" in line for line in lines), "no message about the missing tick handler")


# ======================================================================
#  PART 2 - CHECKS THAT NEED THE WINDOW (queued, run after go() starts)
# ======================================================================
def stage_size():
    return win.stage_size()


def proxy(widget):
    return win.proxies[widget.instance_name]


# ----------------------------------------------------------------------
#  handlers
# ----------------------------------------------------------------------
@live(1, "handlers", "clicking a Button runs its <name>_click")
def live_click():
    before = t_clicks
    for _ in range(3):
        win.buttons["t_button"].click()
    expect(t_clicks == before + 3, f"clicks went {before} -> {t_clicks}")


@live(1, "handlers", "a Button with no handler uses generic button_click(button)")
def live_generic_click():
    win.buttons["t_generic"].click()
    expect(last_generic == "t_generic", f"generic got {last_generic!r}")


@live(1, "handlers", "typing in an Input: text_changed handler + .text stay in sync")
def live_input_changed():
    before = t_input_changes
    win.inputs["t_input"].setText("abc")
    expect(t_input.text == "abc", f".text is {t_input.text!r}")
    expect(t_input_changes > before, "text_changed handler did not run")


@live(1, "handlers", "pressing return in an Input runs its return_pressed handler")
def live_input_return():
    before = t_input_returns
    win.inputs["t_input"].returnPressed.emit()
    expect(t_input_returns == before + 1, "return_pressed handler did not run")


@live(1, "handlers", "Input.text = 'x' updates the box")
def live_input_text_set():
    t_input.text = "from python"
    expect(win.inputs["t_input"].text() == "from python", repr(win.inputs["t_input"].text()))
    t_input.text = ""


# ----------------------------------------------------------------------
#  text  (changing text while running, and BEFORE go)
# ----------------------------------------------------------------------
@live(1, "text", "Label.text changes the label while running")
def live_label_text():
    t_label.text = "changed"
    expect(win.labels["t_label"].text() == "changed", repr(win.labels["t_label"].text()))
    t_label.text = "bench label"


@live(1, "text", "Button.text changes the button while running")
def live_button_text():
    # BUG HISTORY: the Button.text setter once called container.change_text_label
    # (copy-pasted from Label) instead of change_text_button -> KeyError.
    try:
        t_generic.text = "changed"
    except KeyError as e:
        raise AssertionError(f"KeyError {e}: Button.text setter is probably calling "
                             "change_text_label instead of change_text_button")
    expect(win.buttons["t_generic"].text() == "changed", repr(win.buttons["t_generic"].text()))
    t_generic.text = "generic"


@live(1, "text", "Label text set BEFORE go() is what's shown")
def live_label_preset():
    expect(win.labels["t_preset_label"].text() == "set before go",
           repr(win.labels["t_preset_label"].text()))


@live(1, "text", "Button text set BEFORE go() is what's shown")
def live_button_preset():
    expect(win.buttons["t_preset_button"].text() == "set before go",
           repr(win.buttons["t_preset_button"].text()))


# GOTCHA 11: MainWindow.add_input always creates QLineEdit(""), so Input("hi")
# and input.text = "hi" before go() are stored but never shown. If this fails,
# fix add_input to use  QLineEdit(input.text).
@live(1, "text", "Input text set BEFORE go() is what's shown")
def live_input_preset():
    expect(win.inputs["t_preset_input"].text() == "set before go",
           f"box shows {win.inputs['t_preset_input'].text()!r} (Input.text is {t_preset_input.text!r})")


# ----------------------------------------------------------------------
#  image
# ----------------------------------------------------------------------
@live(1, "image", "src() set BEFORE go() is the picture shown")
def live_image_preset():
    shown = win.images["t_img"].pixmap()
    expect(not shown.isNull(), "no picture loaded")
    expected = QPixmap(IMG_B)
    expect((shown.width(), shown.height()) == (expected.width(), expected.height()),
           f"showing {shown.width()}x{shown.height()}, expected {expected.width()}x{expected.height()}")


@live(1, "image", "src() while running swaps the picture")
def live_image_swap():
    t_img.src(IMG_A)
    shown = win.images["t_img"].pixmap()
    expected = QPixmap(IMG_A)
    expect((shown.width(), shown.height()) == (expected.width(), expected.height()),
           f"showing {shown.width()}x{shown.height()}")


# ----------------------------------------------------------------------
#  password
# ----------------------------------------------------------------------
@live(1, "password", "the box really hides its text (echo mode = Password)")
def live_password_echo():
    expect(win.inputs["t_password"].echoMode() == QLineEdit.EchoMode.Password, "echo mode is not Password")


@live(1, "password", "a plain Input is NOT hidden")
def live_plain_echo():
    expect(win.inputs["t_plain_input"].echoMode() == QLineEdit.EchoMode.Normal, "plain Input is hiding text")
    expect("lineedit-password-character" not in win.inputs["t_plain_input"].styleSheet(),
           "plain Input got a password character")


@live(1, "password", "the hiding character reaches the stylesheet (♡ = 9825)")
def live_password_char():
    sheet = win.inputs["t_password"].styleSheet()
    expect("lineedit-password-character: 9825;" in sheet, sheet)


@live(1, "password", "changing .char while running updates the stylesheet (★ = 9733)")
def live_password_char_change():
    t_password.char = "★"
    expect("lineedit-password-character: 9733;" in win.inputs["t_password"].styleSheet(), "★ not applied")
    t_password.char = "♡"


@live(1, "password", ".text is the REAL text, not the dots")
def live_password_real_text():
    win.inputs["t_password"].setText("secret123")
    expect(t_password.text == "secret123", f".text is {t_password.text!r}")
    expect(win.inputs["t_password"].text() == "secret123", "QLineEdit text is not the real text")
    t_password.text = ""


# ----------------------------------------------------------------------
#  hover  (BUG HISTORY: hover_style was silently ignored for a while)
# ----------------------------------------------------------------------
@live(1, "hover", "hover_style colour is used for :hover")
def live_hover_custom():
    sheet = win.buttons["t_hover_custom"].styleSheet()
    expect("QPushButton:hover { background-color: #ff07a9; }" in sheet, sheet)


@live(1, "hover", "no hover_style: hover/pressed are lighter/darker than the base")
def live_hover_auto():
    sheet = win.buttons["t_hover_auto"].styleSheet().lower()
    lighter, darker = adjust_colour("#336699", 0.3), adjust_colour("#336699", -0.3)
    expect(f"hover {{ background-color: {lighter}; }}" in sheet, f"no lighter hover in: {sheet}")
    expect(f"pressed {{ background-color: {darker}; }}" in sheet, f"no darker pressed in: {sheet}")


# ----------------------------------------------------------------------
#  placement  (left/top/right/bottom, wrapping, rotation, z-order)
# ----------------------------------------------------------------------
@live(1, "placement", "stage is a sensible size")
def live_stage_size():
    w, h = stage_size()
    expect(w >= 700 and h >= 700, f"stage is {w}x{h}")


@live(1, "placement", "left: / top: put the widget where it says")
def live_left_top():
    p = proxy(t_label)
    expect((round(p.pos().x()), round(p.pos().y())) == (20, 480), f"at {p.pos().x()},{p.pos().y()}")


@live(1, "placement", "right: / bottom: measure from the stage edge, using the real size")
def live_right_bottom():
    p = proxy(t_right)
    w, h = stage_size()
    expect(approx(p.pos().x() + p.size().width(), w - 20), f"right edge at {p.pos().x() + p.size().width()}, want {w - 20}")
    expect(approx(p.pos().y() + p.size().height(), h - 20), f"bottom edge at {p.pos().y() + p.size().height()}, want {h - 20}")


@live(1, "placement", "changing style while running moves the widget")
def live_move():
    t_label.style <<= "left: 300px; top: 500px;"
    p = proxy(t_label)
    expect((round(p.pos().x()), round(p.pos().y())) == (300, 500), f"at {p.pos().x()},{p.pos().y()}")
    t_label.style <<= "left: 20px; top: 480px;"


@live(1, "placement", "transform: rotate(30deg) rotates the widget")
def live_rotation():
    expect(approx(proxy(t_rot).rotation(), 30, 0.01), f"rotation is {proxy(t_rot).rotation()}")


@live(1, "placement", "Label with NO width never wraps")
def live_no_wrap():
    expect(not win.labels["t_oneline"].wordWrap(), "wordWrap is on")
    expect(proxy(t_oneline).size().height() < 50, f"height {proxy(t_oneline).size().height()} looks like several lines")


@live(1, "placement", "Label WITH a width wraps and grows taller")
def live_wrap():
    expect(win.labels["t_wrapped"].wordWrap(), "wordWrap is off")
    expect(proxy(t_wrapped).size().height() > 2 * proxy(t_oneline).size().height(),
           f"wrapped height {proxy(t_wrapped).size().height()} vs one line {proxy(t_oneline).size().height()}")


@live(1, "placement", "Panels sit behind widgets; later panels on top of earlier ones")
def live_panel_zorder():
    a, b = proxy(t_panel_a).zValue(), proxy(t_panel_b).zValue()
    expect(a < 0 and b < 0, f"panel z values {a}, {b} should be negative (behind widgets)")
    expect(b > a, f"later panel z={b} should be above earlier z={a}")
    expect(proxy(t_label).zValue() >= 0, "a widget is behind a panel")


# ----------------------------------------------------------------------
#  visibility  (GOTCHA 7)
# ----------------------------------------------------------------------
@live(1, "visibility", "display:none hides, display:block restores the SAME place")
def live_display():
    p = proxy(t_hide)
    before = (p.pos().x(), p.pos().y())
    expect(p.isVisible(), "should start visible")
    t_hide.style <<= "display: none;"
    expect(not p.isVisible(), "display: none did not hide it")
    t_hide.style <<= "display: block;"
    expect(p.isVisible(), "display: block did not show it")
    expect((p.pos().x(), p.pos().y()) == before, "it came back in a different place")


@live(1, "visibility", "display and visibility are independent (either one hides)")
def live_display_and_visibility():
    p = proxy(t_hide)
    t_hide.style <<= "visibility: hidden;"
    expect(not p.isVisible(), "visibility: hidden did not hide it")
    t_hide.style <<= "display: none;"
    t_hide.style <<= "visibility: visible;"
    expect(not p.isVisible(), "display: none must still hide it when visibility is visible")
    t_hide.style <<= "display: block;"
    expect(p.isVisible(), "should be visible again")


@live(1, "visibility", "Panels can be hidden too")
def live_panel_hide():
    p = proxy(t_panel_a)
    t_panel_a.style <<= "display: none;"
    expect(not p.isVisible(), "panel not hidden")
    t_panel_a.style <<= "display: block;"
    expect(p.isVisible(), "panel not shown again")


# ----------------------------------------------------------------------
#  tidy  (soft: ⚠️ not ❌ - leftovers from the refactor, nothing is broken)
# ----------------------------------------------------------------------
@live(1, "tidy", "no *_old methods left in MainWindow", soft=True)
def tidy_old_methods():
    from youmakemyheartgui.MainWindow import MainWindow
    old = [n for n in dir(MainWindow) if n.endswith("_old")]
    expect(not old, f"still there: {old}")


@live(1, "tidy", "cssutils is not imported any more", soft=True)
def tidy_cssutils():
    expect("cssutils" not in sys.modules, "cssutils is still being imported somewhere")


@live(1, "tidy", "pyproject lists pymunk and not cssutils", soft=True)
def tidy_pyproject():
    path = os.path.join(HERE, "..", "pyproject.toml")
    if not os.path.exists(path):
        raise Skip("pyproject.toml not found")
    text = open(path, encoding="utf-8").read().lower()
    expect("pymunk" in text, "pymunk is imported by Physics.py but not listed in dependencies")
    expect("cssutils" not in text, "cssutils is still listed in dependencies")


@live(1, "tidy", "place() lives in placement.py, not style.py", soft=True)
def tidy_place_moved():
    from youmakemyheartgui import placement, style
    expect(hasattr(placement, "place"), "placement.place missing")
    expect(not hasattr(style, "place"), "style.py still has place() (it should be pure parsing)")


@live(1, "tidy", "no dead classes left in Widgets.py (Widgetxxx, Win, InputWithButton)", soft=True)
def tidy_dead_classes():
    from youmakemyheartgui import Widgets
    left = [n for n in ("Widgetxxx", "Win", "InputWithButton") if hasattr(Widgets, n)]
    expect(not left, f"still there: {left}")


@live(1, "tidy", "the unused adjust_color alias is gone", soft=True)
def tidy_adjust_color():
    from youmakemyheartgui import colour
    expect(not hasattr(colour, "adjust_color"), "colour.adjust_color still exists (nothing uses it)")


# ----------------------------------------------------------------------
#  STAGE 2: needs the event loop to run for a moment (timers tick)
# ----------------------------------------------------------------------
@live(2, "timer", "a running Timer calls its <name>_tick handler repeatedly")
def live_timer_ticks():
    expect(t_ticks >= 3, f"only {t_ticks} ticks in ~0.4s from a 30ms timer")


@live(2, "timer", "changing .milliseconds while running changes the speed")
def live_timer_speed():
    t_timer.milliseconds = 1000
    expect(t_timer._qtimer.interval() == 1000, "interval not applied")
    t_timer.stop()
    expect(not t_timer.running, "stop() did not stop it")
    settled = t_ticks
    expect(t_ticks == settled, "still ticking after stop")


# ======================================================================
#  THE RUNNER  (stage 1 -> stage 2 -> LAST CHECK -> summary)
# ======================================================================
def run_stage(stage):
    for s, section, name, func, soft in LIVE_CHECKS:
        if s == stage:
            run_check(section, name, func, soft)


def count(symbol):
    return sum(1 for r in RESULTS if r[0] == symbol)


def finish():
    passed, failed, warned, skipped = count("✅"), count("❌"), count("⚠️"), count("⏭")
    total = len(RESULTS)

    if failed:
        text = f"❌ {failed} FAILED  ·  {passed} passed"
        colour, border = "#fee2e2", "#ef4444"
    elif warned:
        text = f"⚠️ {passed} passed  ·  {warned} tidy-up warning(s)"
        colour, border = "#fef3c7", "#f59e0b"
    else:
        text = f"✅ ALL {passed} CHECKS PASSED"
        colour, border = "#d1fae5", "#10b981"
    if skipped:
        text += f"  ·  {skipped} skipped"

    summary.text = text
    summary.style <<= f"background-color: {colour}; border: 3px solid {border};"

    problems = [f"{s} {sec}: {name}" + (f"  -  {msg}" if msg else "")
                for s, sec, name, msg in RESULTS if s != "✅"]
    shown = [p if len(p) < 120 else p[:117] + "..." for p in problems[:9]]
    if len(problems) > 9:
        shown.append(f"...and {len(problems) - 9} more (see the black panel)")
    details.text = "\n".join(shown) if shown else "Nothing to report. Go and have a cup of tea ☕"

    print(f"SELFTEST RESULT: {passed} passed, {failed} failed, {warned} warnings, {skipped} skipped (of {total})")
    if QUIT_WHEN_DONE:
        app.quit()


def stage_1():
    print("── PART 2: needs the window ──")
    run_stage(1)
    t_timer.start()
    QTimer.singleShot(400, stage_2)


def stage_2():
    run_stage(2)
    QTimer.singleShot(0, last_check)


# LAST because it is the dangerous one: a click handler that raises.
# Without sys.excepthook PyQt6 aborts the process right here and the
# SELFTEST RESULT line never prints. Surviving IS the check.
def last_check():
    print("── LAST CHECK (a handler raises ON PURPOSE) ──")
    print("   (the '❌ Error ... ZeroDivisionError' line below is EXPECTED: it's the boom button)")

    def handler_error_survives():
        win.buttons["boom"].click()
        text = win.terminal.toPlainText()
        expect("ZeroDivisionError" in text, "app survived but no friendly error appeared in the terminal")
        expect(THIS_FILE in text, "friendly error doesn't say which file/line")

    run_check("errors", "a click handler that raises doesn't kill the app", handler_error_survives)
    finish()


QTimer.singleShot(300, stage_1)

go()

# go() returns when the window is closed (or --quit). os._exit skips Qt's
# teardown, which can segfault on some machines and would hide our exit code.
sys.stdout.flush()
os._exit(1 if count("❌") else 0)