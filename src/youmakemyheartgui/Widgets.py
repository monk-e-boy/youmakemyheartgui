

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


class Widget:
    def __init__(self, text):
        self._text = text
        self.instance_name = None # store variable name (e.g., 'button1')
        self.click_handler = None # store function name (e.g., button1_click)
        #
        self._style = ""
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
            "height: 40px;"
        )

    def add_style(self, s):
        super().add_style(s)
        # debug output
        # print(f"[{self._text}] style = {self._style}")
        #self.needs_repaint = True
        if self.container:
            print(f"[{self.text}] Update GUI")
            self.container.update_button(self)
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self.container.change_text_button(self)

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
        self.container.change_text_input(self)

    def internal_text_changed_handler(self):
        self._text = self.container.inputs[self.instance_name].text()


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
        self.container.change_text_label(self)

    def add_style(self, s):
        super().add_style(s)
        # debug output
        print(f"[{self._text}] style = {self._style}")
        #self.needs_repaint = True
        if self.container:
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
        self.container.change_img_src(self, path)

    def add_style(self, s):
        super().add_style(s)
        # debug output
        print(f"[{self._text}] style = {self._style}")

        #
        # TODO when do we need to repaint?
        # resize?
        # change image?
        #
        #if self.container:
        #    print(f"[{self.text}] Update GUI")
        #    # force a resize/repaint
        #    self.container.update_label(self)

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
