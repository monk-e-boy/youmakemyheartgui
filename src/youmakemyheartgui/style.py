import math
import re

POSITION_KEYS = ("left", "right", "top", "bottom", "width", "height")

# ---------- parsing ----------

def parse_style(style_str):
    """'left: 50px; background: x' -> {'left': '50px', ...}. Never raises."""
    props = {}
    for decl in str(style_str).strip().strip("{}").split(";"):
        decl = decl.strip()
        if not decl:
            continue
        if ":" not in decl:
            print(f"⚠️  Could not parse style declaration: {decl!r}")
            continue
        key, value = decl.split(":", 1)   # first colon only
        props[key.strip()] = value.strip()
    return props


def _split_top_level(s):
    """Split on commas that aren't inside brackets, so rgb(1,2,3) survives."""
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts

# ---------- gradients ----------

_DIRECTIONS = {  # CSS angle: 0deg = up, 90deg = right, 180deg = down
    "to top": 0, "to top right": 45, "to right": 90, "to bottom right": 135,
    "to bottom": 180, "to bottom left": 225, "to left": 270, "to top left": 315,
}

def css_gradient_to_qt(value):
    """
    'linear-gradient(#f7f8fa, #e7e9ec)'
    'linear-gradient(to right, red, yellow 30%, green)'
    'linear-gradient(45deg, rgb(255,0,0), blue)'
      -> 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 ..., stop:1 ...)'
    Returns None if it isn't a linear-gradient we can understand.
    """
    m = re.fullmatch(r"linear-gradient\((.*)\)", value.strip(), re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    args = _split_top_level(m.group(1))
    if len(args) < 2:
        return None

    # optional first argument: direction or angle
    angle = 180  # CSS default is "to bottom"
    first = args[0].lower()
    if first in _DIRECTIONS:
        angle = _DIRECTIONS[first]
        args = args[1:]
    elif re.fullmatch(r"-?\d+(\.\d+)?deg", first):
        angle = float(first[:-3])
        args = args[1:]
    if len(args) < 2:
        return None

    # colour stops, with optional "30%" positions; fill gaps evenly
    colours, positions = [], []
    for a in args:
        pm = re.fullmatch(r"(.*?)\s+(\d+(?:\.\d+)?)%", a)
        if pm:
            colours.append(pm.group(1).strip())
            positions.append(float(pm.group(2)) / 100)
        else:
            colours.append(a)
            positions.append(None)
    positions[0] = 0.0 if positions[0] is None else positions[0]
    positions[-1] = 1.0 if positions[-1] is None else positions[-1]
    i = 0
    while i < len(positions):
        if positions[i] is None:
            j = i
            while positions[j] is None:
                j += 1
            step = (positions[j] - positions[i - 1]) / (j - i + 1)
            for k in range(i, j):
                positions[k] = positions[i - 1] + step * (k - i + 1)
            i = j
        i += 1

    # angle -> Qt start/end points (0..1, relative to the widget)
    rad = math.radians(angle)
    dx, dy = math.sin(rad), -math.cos(rad)
    x1, y1 = 0.5 - dx / 2, 0.5 - dy / 2
    x2, y2 = 0.5 + dx / 2, 0.5 + dy / 2

    stops = ", ".join(f"stop:{p:g} {c}" for p, c in zip(positions, colours))
    return f"qlineargradient(x1:{x1:g}, y1:{y1:g}, x2:{x2:g}, y2:{y2:g}, {stops})"


def translate_props(props):
    """Rewrite student-friendly CSS into Qt-friendly CSS."""
    out = {}
    for k, v in props.items():
        if k in ("background", "background-image", "background-color") \
                and v.lower().startswith("linear-gradient"):
            qt = css_gradient_to_qt(v)
            if qt:
                out["background"] = qt
                continue
            print(f"⚠️  Couldn't understand gradient: {v!r}")
            continue
        out[k] = v
    return out

# ---------- positional vs visual ----------

def split_style(style_str):
    """Returns (layout, qt_props): layout = left/top/right/bottom/width/height in px."""
    props = translate_props(parse_style(style_str))
    layout = {k: _px(props[k], k) for k in POSITION_KEYS if k in props}
    layout = {k: v for k, v in layout.items() if v is not None}
    qt_props = {k: v for k, v in props.items() if k not in POSITION_KEYS}
    return layout, qt_props


def qt_stylesheet(selector, qt_props, extra=""):
    body = "\n".join(f"{k}: {v};" for k, v in qt_props.items())
    return f"{selector} {{ {body} }}\n{extra}"


def _px(value, key=""):
    try:
        return int(float(value.strip().removesuffix("px")))
    except ValueError:
        print(f"⚠️  {key}: expected something like '50px', got {value!r}")
        return None


#
# TODO - dunno if I like this function being in this library.
#
def place(widget, layout, parent_w, parent_h):
    """Size first, then position, so right/bottom can use the real size."""
    # undo any earlier setFixedSize so adjustSize() can work again
    widget.setMinimumSize(0, 0)
    widget.setMaximumSize(16777215, 16777215)
    widget.adjustSize()

    w = layout.get("width", widget.width())
    h = layout.get("height", widget.height())

    # wrapped text: the height depends on the width we were given
    if "width" in layout and "height" not in layout and widget.hasHeightForWidth():
        h = widget.heightForWidth(w)

    if "width" in layout or "height" in layout:
        widget.setFixedSize(w, h)

    x = parent_w - layout["right"] - w if "right" in layout else layout.get("left", 0)
    y = parent_h - layout["bottom"] - h if "bottom" in layout else layout.get("top", 0)
    widget.move(x, y)
