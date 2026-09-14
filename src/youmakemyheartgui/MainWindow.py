from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from .TerminalLabel import TerminalLabel
from .Grid import GridWidget
import cssutils
from .colour import adjust_colour

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(1200, 760)

        layout = QHBoxLayout(self)

        # remove the top borders and margins, this puts the
        # grid up at 0, 0 accurately
        # left, top, right, bottom
        layout.setContentsMargins(0, 0, 0, 0)

        left = GridWidget()
        layout.addWidget(left, 2)
        #
        # TODO toolbar
        #
        # Hide / Expand console
        # Show / Hide grid ⌗
        self.terminal = TerminalLabel()
        layout.addWidget(self.terminal, 1)

        self.buttons = {}
        self.labels = {}
        self.inputs = {}
        self.images = {}

        #self.label = QLabel(self)
        #pixmap = QPixmap('tests/08-bg1.jpg')
        #self.label.setPixmap(pixmap)
        #self.label.setScaledContents(True)

        #self.label.setStyleSheet("QLabel {width: 100px; height: 100px;}")
        #w = 4800 * 0.1
        #h = 3600 * 0.1
        #tmp = f"QLabel {{min-width: {w}px; min-height: {h}px; max-width: {w}px; max-height: {h}x;}}"
        #print(tmp)
        #self.label.setStyleSheet(tmp)
        #self.label.setFixedSize(100, 100)
        #self.label.setWordWrap(True)

        #self.label.adjustSize()
        #self.label.move(50, 50)
        #layout.addWidget(self.label, 2)



    def terminal_append(self, msg):
        self.terminal.append_line(msg)


    def change_text_input(self, input):
        inp = self.inputs[input.instance_name]
        inp.setText(input.text)
        ##print("TODO fix this")


    def change_text_button(self, button):
        btn = self.buttons[button.instance_name]
        btn.setText(button.text)
        btn.adjustSize()
        self.update_button(button)

    def change_text_label(self, label):
        lbl = self.labels[label.instance_name]
        lbl.setText(label.text)
        self.update_label(label)


    def update_input(self, input):
        inp = self.inputs[input.instance_name]
        # Parse CSS
        sheet = cssutils.parseString("QLineEdit   {" + str(input.style) +"}") ## TODO why do I have to do str() here?
        if len(sheet.cssRules) == 0:
            print("CSS error in:" + str(input.style))
            # TODO: do something nicer here
            return
        
        rule = sheet.cssRules[0]
        props = {p.name: p.value for p in rule.style}

        # Convert px values → ints
        def px(key, default=0):
            val = props.get(key)
            if val and val.endswith("px"):
                return int(val[:-2])
            return default

        width = px("width", -1)
        if width < 0:
            width = px("max-width", 320)
        
        if "right" in props:
            x = self.width() - px("right") - width
        else:
            x = px("left", 0)
        y = px("top", 0)
        if "bottom" in props:
            y = self.height() - px("bottom") - h

        

        # Build a cleaned-up stylesheet (ignore position/size)
        style_for_qt = "\n".join(
            f"{k}: {v};"
            for k, v in props.items()
            if k not in ("left", "right", "top", "bottom", "width", "height")
        )

        inp.setStyleSheet(f"QLineEdit {{ {style_for_qt} }}")
        #lbl.setWordWrap(True)
        inp.adjustSize()
        inp.move(x, y)
        print(input.instance_name, "Geometry CHANGED:", x, y)


    def update_label(self, label):
        lbl = self.labels[label.instance_name]
        # Parse CSS
        sheet = cssutils.parseString("QLabel  {" + str(label.style) +"}") ## TODO why do I have to do str() here?
        if len(sheet.cssRules) == 0:
            print("CSS error in:" + str(label.style))
            # TODO: do something nicer here
            return
        
        rule = sheet.cssRules[0]
        props = {p.name: p.value for p in rule.style}

        # Convert px values → ints
        def px(key, default=0):
            val = props.get(key)
            if val and val.endswith("px"):
                return int(val[:-2])
            return default

        width = px("width", -1)
        if width < 0:
            width = px("max-width", 320)
        
        if "right" in props:
            x = self.width() - px("right") - width
        else:
            x = px("left", 0)
        y = px("top", 0)
        if "bottom" in props:
            y = self.height() - px("bottom") - h

        

        # Build a cleaned-up stylesheet (ignore position/size)
        style_for_qt = "\n".join(
            f"{k}: {v};"
            for k, v in props.items()
            if k not in ("left", "right", "top", "bottom", "width", "height")
        )

        lbl.setStyleSheet(f"QLabel {{ {style_for_qt} }}")
        lbl.setWordWrap(True)
        lbl.adjustSize()
        lbl.move(x, y)
        print(label.instance_name, "Geometry CHANGED:", x, y)


        #btn.setStyleSheet(sheet.cssText.decode("utf-8"))


    def update_button(self, button):
        btn = self.buttons[button.instance_name]
        # Parse CSS
        ##sheet = cssutils.parseString("QPushButton " + css_text)
        
        
        
        #
        # while I figure out default styles:
        #
        #sheet = cssutils.parseString("QPushButton {" + str(button.style) +"}") ## TODO why do I have to do str() here?
        sheet = cssutils.parseString("QPushButton {" \
                                    + str(button.style) \
                                    + "; background-gradient: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #66bb6a, stop:1 #4CAF50);" \
                                    +"}")
        
        if len(sheet.cssRules) == 0:
            print("CSS error in:" + str(button.style))
            # TODO: do something nicer here
            return
        
        rule = sheet.cssRules[0]
        props = {p.name: p.value for p in rule.style}

        # Build a cleaned-up stylesheet (ignore position/size)
        style_for_qt = "\n".join(
            f"{k}: {v};"
            for k, v in props.items()
            if k not in ("left", "right", "top", "bottom", "width", "height")
        )
        #####btn.setStyleSheet(f"QPushButton {{ {style_for_qt} }}")

        # TODO if the button has NO hover style
        if "background-color" in props:
            base_colour = props["background-color"]
        else:
            base_colour = "#4CAF50"
                

        # --- Handle hover/pressed fallbacks ---
        #base_colour = "#4CAF50"# visual_props.get("background-color", "#4CAF50")
        #hover_rule = rules.get("QPushButton:hover")
        #pressed_rule = rules.get("QPushButton:pressed")

        if len(str(button.hover_style)) > 0:
            print(f"Has hover: {str(button.hover_style)}")
            hover_sheet = cssutils.parseString("QPushButton {" + str(button.hover_style) +"}") ## TODO why do I have to do str() here?
            if len(hover_sheet.cssRules) == 0:
                print("CSS error in:" + str(button.hover_sheet))
            else:    
                rule = hover_sheet.cssRules[0]
                props2 = {p.name: p.value for p in rule.style}
                if "background-color" in props:
                    sheet.add(f"QPushButton:hover {{ background-color: {props2["background-color"]}; }}")
        else:
            hover_color = adjust_colour(base_colour, 0.3)
            #sheet.addRule(f"QPushButton:hover {{ background-color: {hover_color}; }}")
            sheet.add(f"QPushButton:hover {{ background-color: {hover_color}; }}")

        pressed_colour = adjust_colour(base_colour, -0.3)
        sheet.add(f"QPushButton:pressed {{ background-color: {pressed_colour}; }}")

        # --- Apply final stylesheet ---
        btn.setStyleSheet(sheet.cssText.decode("utf-8"))
        print("BUTTON Style:", sheet.cssText.decode("utf-8"))

        # Convert px values → ints
        def px(key, default=0):
            val = props.get(key)
            if val and val.endswith("px"):
                return int(val[:-2])
            return default

        x = px("left", 0)
        if "right" in props:
            x = self.width() - px("right") - w

        y = px("top", 0)
        if "bottom" in props:
            y = self.height() - px("bottom") - h
        
        # NORMALLY we calculate the width depending on the text
        # but sometimes the user will override it:
        if "width" in props:
            w = px("width", 100)
            h = px("height", 40)

            # turn off all things that may move the button
            btn.setAutoDefault(False)
            btn.setDefault(False)
            btn.setGeometry(x, y, w, h)
            print(button.instance_name, "Geometry:", x, y, w, h)
        else:
            btn.adjustSize()
            btn.move(x, y)
            print(button.instance_name, "Position:", x, y)


    def add_button(self, button):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        button.container = self

        btn = QPushButton(button.text, self)
        # make the mouse a pointing hand on mouse-hover
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.clicked.connect(button.click_handler)

        # stop the button from getting focus when it is clicked
        # typing in a input, then clicking a button should NOT
        # move focus away from the input (this is my personal
        # preference for a student written application - they should
        # not need to worry about why a button can be "clicked"
        # with the keyboard)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.buttons[button.instance_name] = btn
        self.update_button(button)

    def add_label(self, label):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        label.container = self

        lbl = QLabel(label.text, self)

        self.labels[label.instance_name] = lbl
        self.update_label(label)

    def add_input(self, input):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        input.container = self

        # inp = QLineEdit(input.text, self)
        inp = QLineEdit("", self)
        # we need to tell our Widget that the text has changed
        inp.textChanged.connect(input.internal_text_changed_handler)
        
        # these handlers are optional (defined by the user) so
        # may not exists
        if input.text_changed_handler:
            inp.textChanged.connect(input.text_changed_handler)

        if input.return_pressed_handler:
            inp.returnPressed.connect(input.return_pressed_handler)

        self.inputs[input.instance_name] = inp
        self.update_input(input)


    def change_img_src(self, image, path):
        # Images are actually labels
        lbl = self.images[image.instance_name]
        #pixmap = QPixmap(image.text)
        pixmap = QPixmap(path)
        lbl.setPixmap(pixmap)
        #lbl.setScaledContents(True)

        #self.images[image.instance_name] = lbl
        #self.update_image(image)



    def update_image(self, image):

        #
        # This is a label that contains an image
        # it's just the way QT does things
        #
        img = self.images[image.instance_name]


        # Parse CSS
        sheet = cssutils.parseString("QLabel {" + str(image.style) +"}") ## TODO why do I have to do str() here?
        if len(sheet.cssRules) == 0:
            print("CSS error in:" + str(image.style))
            # TODO: do something nicer here
            return
        
        rule = sheet.cssRules[0]
        props = {p.name: p.value for p in rule.style}

        # Build a cleaned-up stylesheet (ignore position/size)
        style_for_qt = "\n".join(
            f"{k}: {v};"
            for k, v in props.items()
            if k not in ("left", "right", "top", "bottom", "width", "height")
        )

        #
        # TODO filter out all the stuff we don't want to do in the image
        #      background colours, borders, margins, etc
        #      if the student wants to do those things, they should alter
        #      the image in an image editor
        #
        # TODO: warn the user that hover and click styles are not supported
        #

        # --- Apply final stylesheet ---
        img.setStyleSheet(sheet.cssText.decode("utf-8"))

        # Convert px values → ints
        def px(key, default=0):
            val = props.get(key)
            if val and val.endswith("px"):
                return int(val[:-2])
            return default

        x = px("left", 0)
        if "right" in props:
            x = self.width() - px("right") - w

        y = px("top", 0)
        if "bottom" in props:
            y = self.height() - px("bottom") - h
        
        # NORMALLY we calculate the width depending on the text
        # but sometimes the user will override it:
        if "width" in props:
            w = px("width", 100)
            h = px("height", 40)

            img.setGeometry(x, y, w, h)
            print(image.instance_name, "Geometry:", x, y, w, h)
        else:
            img.adjustSize()
            img.move(x, y)
            print(image.instance_name, "Position:", x, y)
    

    def add_image(self, image):
        image.container = self

        lbl = QLabel(self)
        pixmap = QPixmap(image.text)
        lbl.setPixmap(pixmap)
        lbl.setScaledContents(True)

        self.images[image.instance_name] = lbl
        self.update_image(image)

