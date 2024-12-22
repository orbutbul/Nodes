from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import math

class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        
        self.scene = scene
        
        # graphics scene style
        self._color_background = QColor("#1D1D1D")
        self._color_light = QColor("#282828")
        
        # grid size for the dots
        self.gridSize =100

        # pen that draws the dots
        self.pen_light= QPen(self._color_light)
        self.pen_light.setWidth(3)
        
        
        # sets the backround appearance
        self.setBackgroundBrush(self._color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(-width//2, -height//2, width, height)

    # draws the grid
    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # creating grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)


                
        painter.setPen(self.pen_light)

        for x in range(first_left, right, self.gridSize):
            for y in range(first_top, bottom, self.gridSize):
                painter.drawPoint(x,y)
                
                
                
                

