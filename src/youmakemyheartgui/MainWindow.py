#import math, re
from PyQt6.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit,
                             QGraphicsView, QGraphicsScene, QFrame)
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt
from .TerminalLabel import TerminalLabel
from .Grid import GridWidget
from .style import parse_style, split_style, qt_stylesheet, with_box_defaults
from .placement import place
from .colour import adjust_colour
from .Panel import PanelFrame, parse_bevel, DEFAULT_FACE
from .Physics import Physics
from .Widgets import PasswordInput


DEBUG = False

# rotate(45)
# rotate(45deg)
# rotate(-0.25turn)
# rotate(3.142rad)
#


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

        #left = GridWidget()
        #layout.addWidget(left, 2)
        self.grid = GridWidget()
        layout.addWidget(self.grid, 2)
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
        self.panels = {}

        # WHY - so we can redraw widgets at angles, capture click and
        #       drag events etc.
        # Transparent overlay that holds every widget, so the grid shows through
        # It covers the grid only (not the terminal), so the terminal still
        # gets its own mouse and scroll events.
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setFrameShape(QFrame.Shape.NoFrame)
        self.view.setStyleSheet("background: transparent;")
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.view.setRenderHints(QPainter.RenderHint.Antialiasing |
                                 QPainter.RenderHint.SmoothPixmapTransform)
        self.proxies = {}
        self.objs = {}   # instance_name -> the student's widget object
        self.physics = Physics(self)

        # run the layout now (the window is fixed size) so the grid has its
        # real size before any widget is placed - go() adds widgets BEFORE show()
        # part of the ROTATE / Gravity / Physics are implemented
        layout.activate()
        g = self.grid.geometry()
        self.view.setGeometry(g)
        self.scene.setSceneRect(0, 0, g.width(), g.height())


    def stage_size(self):
        """Size of the area widgets are placed in (right: / bottom: measure from here)."""
        r = self.scene.sceneRect()
        return int(r.width()), int(r.height())


    def _add_to_scene(self, obj, qwidget):
        # no parent on the QWidget: the proxy takes ownership of it
        self.proxies[obj.instance_name] = self.scene.addWidget(qwidget)
        self.objs[obj.instance_name] = obj


    def _place(self, obj, qwidget, layout):
        w, h = self.stage_size()
        # place(qwidget, layout, w, h, self.proxies[obj.instance_name])
        place(qwidget, layout, w, h, self.proxies[obj.instance_name],
              physics_on=self.physics.active)


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

        layout, qt_props = split_style(input.style)

        if isinstance(input, PasswordInput):
            # Qt wants the hiding character as a number
            qt_props["lineedit-password-character"] = ord(input.char)

        inp.setStyleSheet(qt_stylesheet("QLineEdit", qt_props))

        self._place(input, inp, layout)


    def update_label(self, label):
        lbl = self.labels[label.instance_name]
        layout, qt_props = split_style(label.style)

        lbl.setStyleSheet(qt_stylesheet("QLabel", qt_props))

        # wrap only if the student gave a width; otherwise one line, sized to the text
        lbl.setWordWrap("width" in layout)

        # place(lbl, layout, self.width(), self.height())
        self._place(label, lbl, layout)


    def update_button(self, button):
        btn = self.buttons[button.instance_name]
        layout, qt_props = split_style(button.style)
        qt_props = with_box_defaults(qt_props)

        # hover/pressed need a *colour*; if there's a gradient, use its first stop
        base = qt_props.get("background-color", "#4CAF50")

        hover = adjust_colour(base, 0.3)
        hover_props = parse_style(str(button.hover_style))
        if "background-color" in hover_props:
            hover = hover_props["background-color"]

        pressed = adjust_colour(base, -0.3)

        btn.setStyleSheet(qt_stylesheet(
            "QPushButton", qt_props,
            f"QPushButton:hover {{ background-color: {hover}; }}\n"
            f"QPushButton:pressed {{ background-color: {pressed}; }}"))

        # place(btn, layout, self.width(), self.height())
        # btn.adjustSize()

        self._place(button, btn, layout)

        if DEBUG:
            print("BUTTON Style:", btn.styleSheet())


    def add_button(self, button):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        button.container = self

        btn = QPushButton(button.text)
        btn.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

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
        self._add_to_scene(button, btn)
        self.update_button(button)


    def add_label(self, label):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        label.container = self

        # lbl = QLabel(label.text, self)
        lbl = QLabel(label.text)

        self.labels[label.instance_name] = lbl
        self._add_to_scene(label, lbl)
        self.update_label(label)


    def add_input(self, input):
        # tell the button who we are so it can tell us things (e.g.
        # the text has changed, or a style has changed)
        input.container = self

        # inp = QLineEdit(input.text, self)
        # inp = QLineEdit("", self)
        #inp = QLineEdit("")
        inp = QLineEdit(input.text)
        
        if isinstance(input, PasswordInput):
            inp.setEchoMode(QLineEdit.EchoMode.Password)

        # we need to tell our Widget that the text has changed
        inp.textChanged.connect(input.internal_text_changed_handler)
        
        # these handlers are optional (defined by the user) so
        # may not exists
        if input.text_changed_handler:
            inp.textChanged.connect(input.text_changed_handler)

        if input.return_pressed_handler:
            inp.returnPressed.connect(input.return_pressed_handler)

        self.inputs[input.instance_name] = inp
        self._add_to_scene(input, inp)
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

        self.update_image(image)


    def update_image(self, image):
        #
        # This is a label that contains an image
        # it's just the way QT does things
        #
        img = self.images[image.instance_name]

        layout, qt_props = split_style(image.style)

        #
        # TODO filter out all the stuff we don't want to do in the image
        #      background colours, borders, margins, etc
        #      if the student wants to do those things, they should alter
        #      the image in an image editor
        #
        # TODO: warn the user that hover and click styles are not supported
        #
        img.setStyleSheet(qt_stylesheet("QLabel", qt_props))
        self._place(image, img, layout)


    def add_image(self, image):
        image.container = self

        lbl = QLabel()
        pixmap = QPixmap(image.text)
        lbl.setPixmap(pixmap)
        lbl.setScaledContents(True)

        self.images[image.instance_name] = lbl
        self._add_to_scene(image, lbl)
        self.update_image(image)


    def add_panel(self, panel, order=0):
        panel.container = self
        frame = PanelFrame()
        self.panels[panel.instance_name] = frame
        self._add_to_scene(panel, frame)
        # panels live behind every other widget (which sit at z = 0);
        # a panel defined later in the script is drawn on top of earlier ones
        self.proxies[panel.instance_name].setZValue(-10000 + order)
        self.update_panel(panel)


    def update_panel(self, panel):
        frame = self.panels[panel.instance_name]
        layout, qt_props = split_style(panel.style)
        style, width, border_colour, qt_props = parse_bevel(qt_props)

        # the 3D edge is derived from border-color, else the face colour
        base = border_colour
        if base is None:
            base = QColor(qt_props.get("background-color", DEFAULT_FACE))
            if not base.isValid():
                base = QColor(DEFAULT_FACE)   # gradients, bad colour names
        frame.set_bevel(style, width, base)

        frame.setStyleSheet(qt_stylesheet("QFrame", qt_props))
        self._place(panel, frame, layout)

