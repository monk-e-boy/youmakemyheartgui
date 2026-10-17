import pymunk
from PyQt6.QtCore import QTimer
from math import degrees, radians

GRAVITY = 900   # pixels/second/second. Positive = down, because Qt's y points down


class Physics:
    def __init__(self, window):
        self.window = window     # the MainWindow: we read its proxies from here
        self.space = None        # the pymunk world. None = never built
        self.items = {}          # instance_name -> (body, w, h)

        # our own timer, separate from the student Timer widget
        self.timer = QTimer()
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.step)

    @property
    def active(self):
        """True once the world exists (even if paused)."""
        return self.space is not None

    def start(self):
        if not self.active:
            self._build()
        self.timer.start()

    def pause(self):
        self.timer.stop()        # world is kept, so step() still works

    
    def step(self):
        """One tick of physics. The timer calls this, and so can a student."""
        if not self.active:
            self._build()
        self.space.step(1 / 60)
        self._sync()

    
    def _physical_widgets(self):
        """Yield (name, proxy) for every widget that takes part in physics:
        not a panel (panels are backgrounds) and currently visible."""
        for name, proxy in self.window.proxies.items():
            if name not in self.window.panels and proxy.isVisible():
                yield name, proxy

    
    def _build(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, GRAVITY)
        self._add_walls()

        for name, proxy in self._physical_widgets():
            w = proxy.size().width()
            h = proxy.size().height()
            centre = (proxy.pos().x() + w / 2, proxy.pos().y() + h / 2)
            angle = radians(proxy.rotation())   # start at the styled rotation

            mass = 1

            if self.window.objs[name].fixed:
                # static body: collides with things but never moves
                body = pymunk.Body(body_type=pymunk.Body.STATIC)
            else:
                body = pymunk.Body(mass, pymunk.moment_for_box(mass, (w, h)))

            body.position = centre
            body.angle = angle
            shape = pymunk.Poly.create_box(body, (w, h))
            shape.friction = 0.5
            shape.elasticity = 0.5

            # the body must always be added with its shape, even a static one
            self.space.add(body, shape)

            if not self.window.objs[name].fixed:
                # only moving widgets go in items, so _sync leaves fixed ones alone
                self.items[name] = (body, w, h)


    def _add_walls(self):
        w, h = self.window.stage_size()
        t = 25   # wall thickness: thick so fast widgets can't tunnel through
        edges = [
            ((0, h + t), (w, h + t)),    # floor
            ((-t, 0), (-t, h)),          # left
            ((w + t, 0), (w + t, h)),    # right
            ((0, -t), (w, -t)),          # ceiling
        ]
        for a, b in edges:
            seg = pymunk.Segment(self.space.static_body, a, b, t)
            seg.friction = 0.5
            seg.elasticity = 0.3
            self.space.add(seg)


    def _sync(self):
        for name, (body, w, h) in self.items.items():
            proxy = self.window.proxies[name]
            # pymunk gives the CENTRE of the body, Qt wants the top-left corner
            proxy.setPos(body.position.x - w / 2, body.position.y - h / 2)
            proxy.setRotation(degrees(body.angle))