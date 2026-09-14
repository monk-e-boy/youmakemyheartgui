from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtWidgets import (QWidget)
#from PyQt6.QtWidgets import (
#    QApplication, QWidget, QMainWindow, QHBoxLayout,
#    QPushButton, QVBoxLayout, QLabel, QFrame
#)

class GridWidget(QWidget):
    # Grid constants
    GRID_STEP = 50
    MAX_SIZE = 350
    GRID_COLOR = QColor(200, 200, 200) # Pale grey
    TEXT_COLOR = QColor(100, 100, 100) # Darker grey for labels
    
    # Minimum size to ensure all labels and lines up to 350 are visible
    LABEL_WIDTH = 27 
    
    def __init__(self):
        super().__init__()
        # Set a fixed size based on the grid and label width
        total_width = self.MAX_SIZE + self.LABEL_WIDTH 
        #self.setFixedSize(QSize(total_width, self.MAX_SIZE + 5)) # +5 for a little margin


    def resizeEvent(self, event):
        current_width = self.width() 
        current_height = self.height()
        # print(f"GridWidget resized: Width = {current_width}px, Height = {current_height}px")

        # IMPORTANT: Always call the base class implementation
        super().resizeEvent(event)

        # repaint ourself
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # --- Drawing Setup ---
        
        # 1. Set font and color for labels
        painter.setFont(QFont('Arial', 8))
        painter.setPen(QPen(self.TEXT_COLOR))
        
        # 2. Set pen for the pale grey grid lines
        grid_pen = QPen(self.GRID_COLOR)
        grid_pen.setWidth(1)
        painter.setPen(grid_pen)
        
        # --- Drawing Loop ---
        
        # The drawing area starts after the space reserved for labels
        start_x = self.LABEL_WIDTH 
        #grid_end = self.MAX_SIZE
        grid_end = self.width()
        
        for i in range(0, grid_end + 1, self.GRID_STEP):
            # i represents the current pixel position (0, 50, 100, ...)
            
            # Vertical Line (x-coordinate)
            painter.drawLine(i, 0, i, grid_end)
            
            # Horizontal Line (y-coordinate)
            painter.drawLine(0, i, grid_end, i)
            
            # --- Draw Labels ---
            
            label_text = str(i)+"px"
            
            # Label on the left (Vertical Axis)
            # Draw text just before the line, centered on the line's position
            text_rect = painter.fontMetrics().boundingRect(label_text)
            
            # Position for Y-axis label (align right, center vertically on line)
            y_label_x = 5
            
            y_label_y = i + text_rect.height()
            if i > 0:
                y_label_y = int( i + (text_rect.height()/2) + painter.fontMetrics().ascent() )
            
            # vertical labels
            painter.drawText(y_label_x, y_label_y, label_text)

            if i > 0:
                painter.drawText(i+5, 10, label_text)