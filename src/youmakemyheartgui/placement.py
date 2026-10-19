

#def place(widget, layout, parent_w, parent_h, proxy=None):
def place(widget, layout, parent_w, parent_h, proxy=None, physics_on=False):
    """Size first, then position, so right/bottom can use the real size.
    Pass the QGraphicsProxyWidget as `proxy` when the widget lives in the
    scene: position, rotation and visibility then go through the proxy."""

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
    #widget.move(x, y)
    #widget.setVisible(not layout.get("hidden", False))
    
    visible = not layout.get("hidden", False)

    # make the proxy match the widget. It does not always shrink by itself,
    # and the leftover area gets painted as a grey box over the grid
    proxy.setMinimumSize(0, 0)
    proxy.resize(w, h)

    # right/bottom use the un-rotated box, like CSS does
    if not physics_on:
        proxy.setPos(x, y)
    
    proxy.setTransformOriginPoint(w / 2, h / 2)   # rotate about the centre
    
    if not physics_on:
        proxy.setRotation(layout.get("rotate", 0.0))
    proxy.setVisible(visible)
