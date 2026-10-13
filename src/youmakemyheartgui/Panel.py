import re
from PyQt6.QtWidgets import QFrame
from PyQt6.QtGui import QPainter, QColor

DEFAULT_FACE = "#c0c0c0"   # classic Windows NT grey

BORDER_STYLES = ("outset", "inset", "groove", "ridge", "none", "solid")


def _mix(colour, other, t):
    """Blend `colour` towards `other` by t (0..1), in plain RGB."""
    return QColor(
        round(colour.red()   + (other.red()   - colour.red())   * t),
        round(colour.green() + (other.green() - colour.green()) * t),
        round(colour.blue()  + (other.blue()  - colour.blue())  * t),
    )


def parse_bevel(qt_props):
    """Pull every border* property out of qt_props (they're ours, never sent to Qt).
    Returns (style, width_px, border_colour_or_None, remaining_props).
    Understands 'border: 2px outset #c0c0c0' as well as border-style,
    border-width and border-color on their own (the specific ones win)."""
    style, width, colour = "outset", 2, None
    rest = {}
    border_props = {}
    for k, v in qt_props.items():
        if k == "border" or k.startswith("border-style") \
                or k in ("border-width", "border-color"):
            border_props[k] = v
        elif k.startswith("border"):
            pass   # border-radius, border-top... NT panels are square, ignore
        else:
            rest[k] = v

    def apply(token):
        nonlocal style, width, colour
        t = token.strip().lower()
        if t in BORDER_STYLES:
            style = t
        elif re.fullmatch(r"\d+(\.\d+)?(px)?", t):
            width = int(float(t.removesuffix("px")))
        else:
            c = QColor(token.strip())
            if c.isValid():
                colour = c

    if "border" in border_props:                     # shorthand first
        for tok in re.findall(r"\w+\([^)]*\)|\S+", border_props["border"]):
            apply(tok)
    for key in ("border-style", "border-width", "border-color"):  # then specifics
        if key in border_props:
            apply(border_props[key])
    return style, max(0, width), colour, rest


class PanelFrame(QFrame):
    """A flat face (drawn by the Qt stylesheet) with a hand-drawn 3D edge."""

    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.bevel_style = "outset"
        self.bevel_width = 2
        self.bevel_base = QColor(DEFAULT_FACE)

    def set_bevel(self, style, width, base):
        self.bevel_style, self.bevel_width, self.bevel_base = style, width, base
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)          # the background / gradient
        if self.bevel_style in ("none", "solid") or self.bevel_width <= 0:
            return

        base = self.bevel_base
        white, black = QColor("white"), QColor("black")
        light  = _mix(base, white, 0.45)   # NT: #c0c0c0 -> #dfdfdf
        shadow = _mix(base, black, 0.50)   # NT: #c0c0c0 -> #808080

        # (top-left colour, bottom-right colour) for the outer and inner ring
        rings = {
            "outset": ((white,  black), (light,  shadow)),
            "inset":  ((shadow, white), (black,  light)),
            "ridge":  ((white,  shadow), (shadow, white)),
            "groove": ((shadow, white), (white,  shadow)),
        }[self.bevel_style]

        w, h = self.width(), self.height()
        bw = self.bevel_width
        outer_n = (bw + 1) // 2            # 1px bevel = outer ring only
        p = QPainter(self)
        for i in range(bw):
            tl, br = rings[0] if i < outer_n else rings[1]
            x0, y0, x1, y1 = i, i, w - 1 - i, h - 1 - i
            if x1 <= x0 or y1 <= y0:
                break
            p.setPen(tl)
            p.drawLine(x0, y0, x1, y0)     # top
            p.drawLine(x0, y0, x0, y1)     # left
            p.setPen(br)
            p.drawLine(x0, y1, x1, y1)     # bottom
            p.drawLine(x1, y0, x1, y1)     # right
        p.end()