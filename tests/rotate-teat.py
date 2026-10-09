from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPainter
import math

# in MainWindow, instead of absolutely-positioned child widgets:
self.scene = QGraphicsScene(0, 0, 1200, 760)
self.view = QGraphicsView(self.scene, self)
self.view.setRenderHints(QPainter.RenderHint.Antialiasing |
                         QPainter.RenderHint.SmoothPixmapTransform)

def add_widget_to_scene(self, qwidget, x, y):
    proxy = self.scene.addWidget(qwidget)
    proxy.setPos(x, y)
    proxy.setTransformOriginPoint(qwidget.width() / 2, qwidget.height() / 2)
    return proxy

# each physics tick, per widget:
def sync(proxy, body, w, h):
    proxy.setPos(body.position.x - w / 2, body.position.y - h / 2)
    proxy.setRotation(math.degrees(body.angle))