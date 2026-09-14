from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont


class TerminalLabel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setStyleSheet("background-color: black; color: white;")
        self.setFont(QFont("Consolas", 10))  # fixed-width font

        self._auto_scroll = True
        self.verticalScrollBar().valueChanged.connect(self._on_user_scroll)

    def append_line(self, text):
        self.append(text)
        #self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
        if self._auto_scroll:
            bar = self.verticalScrollBar()
            bar.setValue(bar.maximum())

    def _on_user_scroll(self):
        bar = self.verticalScrollBar()
        # if user scrolls up (not at bottom), disable auto-scroll
        if bar.value() < bar.maximum():
            self._auto_scroll = False
        else:
            # re-enable when back at bottom
            self._auto_scroll = True