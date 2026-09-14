from PyQt6.QtGui import QColor

def adjust_colour(colour_str, factor):
    """Lighten or darken a color string like '#4CAF50' by a factor (-1.0 to 1.0)."""
    c = QColor(colour_str)
    h, s, v, a = c.getHsvF()
    v = max(0, min(1, v * (1 + factor)))  # adjust brightness
    c.setHsvF(h, s, v, a)
    return c.name()

# Ugh
def adjust_color(color_str, factor):
    return adjust_colour(color_str, factor)