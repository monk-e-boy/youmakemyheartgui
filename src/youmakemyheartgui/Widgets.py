#import os
#import traceback
from PyQt6.QtCore import QTimer
from .style import parse_style
from .errors import where_in_student_code

#
# TODO: fix this turd
#
DEBUG = False
#
#
#

class StyleProxy:
    def __init__(self, button):
        self.button = button

    def __ilshift__(self, s):
        """Implements <<= (merge/update style)"""
        self.button.add_style(s)
        return self

    def __str__(self):
        return self.button._style

class HoverStyleProxy:
    def __init__(self, widget):
        self.widget = widget

    def __ilshift__(self, s):
        """Implements <<= (merge/update style)"""
        self.widget.add_hover_style(s)
        return self

    def __str__(self):
        return self.widget._hover_style

class UserData(object):
    pass


# TODO (future): click / input handlers are NOT protected like the timer is.
# PyQt6 aborts the whole app if a handler raises an exception, so a typo in
# a b1_click() makes the window vanish with no explanation on screen.
# Ideas for when we have tested this with real students:
#   - set sys.excepthook in __init__.py (after the PrintCapture import) to
#     print a friendly error to the console pane, or
#   - wrap the handlers in MainWindow.add_button / add_input in a safe_call().
class Timer:
    def __init__(self, milliseconds=1000):
        self.instance_name = None   # set by go(), e.g. 'spinner'
        self.tick_handler = None    # set by go(), e.g. spinner_tick
        self.state = UserData()
        self.stash = UserData()

        self._qtimer = QTimer()
        self._qtimer.setInterval(int(milliseconds))
        self._qtimer.timeout.connect(self._tick)

    def _tick(self):
        if self.tick_handler is None:
            return
        try:
            self.tick_handler()
        except Exception as e:


            # find the innermost line in the STUDENT'S file, not our library
            #library_dir = os.path.dirname(os.path.abspath(__file__))
            #where = ""
            #for frame in reversed(traceback.extract_tb(e.__traceback__)):
            #    if not os.path.abspath(frame.filename).startswith(library_dir):
            #        where = f" (line {frame.lineno} of {os.path.basename(frame.filename)})"
            #        break

            where = where_in_student_code(e.__traceback__)
            print(f"❌ Error in {self.instance_name}_tick{where}:\n   {type(e).__name__}: {e}")
            # stop, otherwise this message would repeat many times a second
            self.stop()
            print(f"⏹ Timer '{self.instance_name}' stopped because of the error above.")

    def start(self):
        self._qtimer.start()

    def stop(self):
        self._qtimer.stop()

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()

    @property
    def running(self):
        return self._qtimer.isActive()

    # students can change the speed while it runs: spinner.milliseconds = 10
    @property
    def milliseconds(self):
        return self._qtimer.interval()

    @milliseconds.setter
    def milliseconds(self, ms):
        self._qtimer.setInterval(int(ms))


class Widget:
    def __init__(self, text):
        self._text = text
        self.instance_name = None # store variable name (e.g., 'button1')
        self.click_handler = None # store function name (e.g., button1_click)
        #
        # The style is kept as a dictionary: {"left": "50px", "color": "red"}
        # so each property can only ever appear once.
        #
        self._props = {}
        self._style_proxy = StyleProxy(self)
        #
        #
        # Hover style will only accept colour changes
        # it will IGNORE location, size (padding, margins),
        # fonts (may change size) as these move the button
        # under the mouse/finger which is super anoying
        #
        self._hover_style = ""
        self._hover_style_proxy = HoverStyleProxy(self)
        #
        self.container = None # set this to the QT window that contains us

        self.state = UserData()
        self.stash = UserData()
        self.inventory = UserData()

        self.fixed = False   # True = physics won't move us (ramps, platforms, control buttons)


    @property
    def style(self):
        return self._style_proxy

    @property
    def hover_style(self):
        return self._hover_style_proxy

    @style.setter
    def style(self, s):
        # Why only strings? "b.style <<= ..." is really:
        #     b.style = b.style.__ilshift__(...)
        # so Python calls this setter with the StyleProxy it just got from
        # the getter. We must ignore that, otherwise we would wipe the style.
        if isinstance(s, str):
            self._props = parse_style(s)

    @hover_style.setter
    def hover_style(self, s):
        # Defensive: only clean if it's a string
        if isinstance(s, str):
            self._hover_style = self._clean(s)

    def _clean(self, s):
        s = s.strip().strip("{}")
        if not s.endswith(";"):
            s += ";"
        return s

    @property
    def _style(self):
        """The style as text, e.g. 'left: 50px; color: red;'
        (this is what the StyleProxy prints and what MainWindow reads)"""
        return " ".join(f"{key}: {value};" for key, value in self._props.items())

    # called from the style proxy <<=
    def add_style(self, s):
        for key, value in parse_style(s).items():
            # Take the old value out first, so the new one goes on the END.
            # In a stylesheet the last declaration wins, and that matters
            # when two properties overlap (background vs background-color).
            self._props.pop(key, None)
            self._props[key] = value


class Widgetxxx:
    def __init__(self, text):
        self._text = text
        self.instance_name = None # store variable name (e.g., 'button1')
        self.click_handler = None # store function name (e.g., button1_click)
        #


        #self._style = ""
        self._props = {}
        self._style_proxy = StyleProxy(self)
        #
        #
        # Hover style will only accept colour changes
        # it will IGNORE location, size (padding, margins),
        # fonts (may change size) as these move the button
        # under the mouse/finger which is super anoying
        #
        self._hover_style = ""
        self._hover_style_proxy = HoverStyleProxy(self)
        #
        self.container = None # set this to the QT window that contains us

        self.state = UserData()
        self.stash = UserData()
        self.inventory = UserData()

        self.fixed = False   # True = physics won't move us (ramps, platforms, control buttons)


    @property
    def style(self):
        return self._style_proxy

    @property
    def hover_style(self):
        return self._hover_style_proxy

    @style.setter
    def style(self, s):
        #self._style = self._clean(s)
        # Defensive: only clean if it's a string
        if isinstance(s, str):
            self._style = self._clean(s)
            
        # TODO figure this out one day
        #else:
        #    self._style = ""

    @hover_style.setter
    def hover_style(self, s):
        #self._style = self._clean(s)
        # Defensive: only clean if it's a string
        if isinstance(s, str):
            self._hover_style = self._clean(s)

    def _clean(self, s):
        s = s.strip().strip("{}")
        if not s.endswith(";"):
            s += ";"
        return s

    # called from the style proxy <<=
    def add_style(self, s):
        s = self._clean(s)
        key = s.split(":")[0].strip()

        # split and filter out any existing style with same key
        parts = [p.strip() for p in self._style.split(";") if p.strip()]
        filtered = [p for p in parts if not p.startswith(key + ":")]

        # add new one at the end
        filtered.append(s.strip(";"))
        self._style = "; ".join(filtered) + ";"


class Button(Widget):
    def __init__(self, text):
        #
        super().__init__(text)
        #
        
        # this seems to kill the border?
        #self.style <<= "border-radius: 8px;"

        self.style <<= (
            "font-family: \"Segoe UI\", Helvetica, Arial, sans-serif;"
            "font-size: 22px;"
            "padding: 8px;"
            #"height: 40px;"
        )

    def add_style(self, s):
        super().add_style(s)
        # debug output
        # print(f"[{self._text}] style = {self._style}")
        #self.needs_repaint = True
        if self.container:
            if DEBUG:
                print(f"[{self.text}] Update GUI")
            self.container.update_button(self)
    
    @property
    def text(self):
        return self._text

#    @text.setter
#    def text(self, text):
#        self._text = text
#        self.container.change_text_button(self)

    @text.setter
    def text(self, text):
        self._text = text

        # if student sets button.text BEFORE go, there
        # is no container yet.
        if self.container:
            self.container.change_text_label(self)


class Input(Widget):
    def __init__(self, text):
        #
        super().__init__(text)
        #
        self.style <<= "background-color: white;"
        self.style <<= "color: rgb(13, 13, 13);"
        self.style <<= "border-radius: 8px;"
        self.style <<= "font-family: \"Segoe UI\", Helvetica, Arial, sans-serif;"
        self.style <<= "font-size: 22px;"
        self.style <<= "padding: 8px;"
        self.style <<= "left: 20px;"
        self.style <<= "top: 20px;"


    @property
    def text(self):
        return self._text


    @text.setter
    def text(self, text):
        self._text = text

        # if student sets button.text BEFORE go, there
        # is no container yet.
        if self.container:
            self.container.change_text_input(self)


    def internal_text_changed_handler(self):
        self._text = self.container.inputs[self.instance_name].text()


    def add_style(self, s):
        super().add_style(s)
        if self.container:
            self.container.update_input(self)


class PasswordInput(Input):
    """An Input that hides what is typed behind a character (a dot by default).
    password.text still gives you the REAL text.

        password = PasswordInput("")           # dots
        password = PasswordInput("", "♡")      # hearts
        password.char = "★"                    # change it while running
    """
    def __init__(self, text="", char="●"):
        super().__init__(text)
        self._char = self._check_char(char)

    @property
    def char(self):
        return self._char

    @char.setter
    def char(self, char):
        self._char = self._check_char(char)
        if self.container:
            self.container.update_input(self)

    def _check_char(self, char):
        # Qt can only draw ONE simple character here (not most emoji)
        if isinstance(char, str) and len(char) == 1 and ord(char) <= 0xFFFF:
            return char
        print(f"⚠️  PasswordInput: {char!r} won't work, it needs ONE simple "
              f"character like ● ♡ ★ or *. Using ● instead.")
        return "●"


class Label(Widget):
    def __init__(self, text):
        super().__init__(text)
        #self._text = text
        self.style <<= "background-color: rgba(13, 13, 13, 13);"
        self.style <<= "color: rgb(13, 13, 13);"
        self.style <<= "border-radius: 8px;"
        self.style <<= "font-family: \"Segoe UI\", Helvetica, Arial, sans-serif;"
        self.style <<= "font-size: 22px;"
        self.style <<= "padding: 8px;"
        #self.style <<= "max-width: 320px;"
        self.style <<= "left: 20px;"
        self.style <<= "top: 20px;"

    @property
    def text(self):
        return self._text


    @text.setter
    def text(self, text):
        self._text = text

        # if student sets button.text BEFORE go, there
        # is no container yet.
        if self.container:
            self.container.change_text_label(self)


    def add_style(self, s):
        super().add_style(s)

        if DEBUG:
            # debug output
            print(f"[{self._text}] style = {self._style}")
        
        
        #self.needs_repaint = True
        if self.container:

            if DEBUG:
                print(f"[{self.text}] Update GUI")

            # force a resize/repaint
            self.container.update_label(self)

class Image(Widget):
    def __init__(self, path):
        super().__init__(path)

        self.path = path
        # min-width: {w}px; min-height: {h}px; max-width: {w}px; max-height: {h}x;
        # self.style <<= "max-width: 320px;"
        self.style <<= "left: 20px;"
        self.style <<= "top: 20px;"

        #
        # TODO override hover and click -- warn the user these are not
        #      implemented for images
        #

    # TODO figure this out - text or path or src?
    @property
    def text(self):
        return self._text


    @text.setter
    def text(self, text):
        self._text = text
        ## self.container.change_text_label(self)


    def src(self, path):
        self._text = path
        if self.container:
            self.container.change_img_src(self, path)


    def add_style(self, s):
        super().add_style(s)

        if DEBUG:
            # debug output
            print(f"[{self._text}] style = {self._style}")

        if self.container:
            self.container.update_image(self)


class Panel(Widget):
    """A styled rectangle drawn BEHIND every other widget (Windows NT style
    by default). Later panels are drawn on top of earlier ones."""
    def __init__(self):
        super().__init__("")
        self.style <<= "background-color: #c0c0c0;"
        self.style <<= "border-style: outset;"
        self.style <<= "border-width: 2px;"
        self.style <<= "left: 20px;"
        self.style <<= "top: 20px;"
        self.style <<= "width: 200px;"
        self.style <<= "height: 120px;"

    def add_style(self, s):
        super().add_style(s)
        if self.container:
            self.container.update_panel(self)


#
#             +------------+-----+
# enter name: | Alice      | Go! |
#             +------------+-----+
#
class InputWithButton:
    def __init__(self, text):
        pass


class Win:
    def __init__(self):
        data = {}
