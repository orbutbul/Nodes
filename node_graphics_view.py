from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QDMGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)
        self.grScene = grScene
        self.initUI()
        self.setScene(self.grScene)
        
        # zoom parameters
        self.zoomInFactor = 1.25
        self.zoom = 5
        self.zoomStep = 1
        self.zoomRange= [0,10]
        self.zoomClamp = False
        self.zoomClampMax = False
        

    def initUI(self):
        hints = (QPainter.RenderHint.Antialiasing
                 | QPainter.RenderHint.TextAntialiasing
                 | QPainter.RenderHint.SmoothPixmapTransform)
        self.setRenderHints(hints)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)        
        
        # hide scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # zoom on mouse
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.MouseButton.LeftButton:
            self.rightMouseButtonPress(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightMouseButtonPress(event)

        else:
            super().mousePressEvent(event)
        
    def middleMouseButtonPress(self,event):
        # have a qmosue event that presses the left mouse button at the event position
        fakeEvent =QMouseEvent(QMouseEvent.Type.MouseButtonPress,
                    event.position(),
                    Qt.MouseButton.LeftButton,
                    Qt.MouseButton.LeftButton,
                    event.modifiers()
                    )
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        super().mousePressEvent(fakeEvent)
        
    def leftMouseButtonPress(self, event):
         super().mousePressEvent(event)

    def rightMouseButtonPress(self, event):
         super().mousePressEvent(event)
        
        
        
    def mouseReleaseEvent(self,event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.MouseButton.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.MouseButton.RightButton:
            self.rightMouseButtonRelease(event)

        else:
            super().mouseReleaseEvent(event)
            
        
    def middleMouseButtonRelease(self,event):
        # have a qmosue event that releases the left mouse button at the event position
        fakeEvent =QMouseEvent(QMouseEvent.Type.MouseButtonRelease,
                    event.position(),
                    Qt.MouseButton.LeftButton,
                    Qt.MouseButton.LeftButton,
                    event.modifiers()
                    )
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)

    def leftMouseButtonRelease(self, event):
         super().mouseReleaseEvent(event)


    def rightMouseButtonRelease(self, event):
         super().mouseReleaseEvent(event)
    
    
    
    def wheelEvent(self, event):        
  

        # TODO rewrite for branchless later
        # zoomfactor = self.zoomInFactor
        # self.zoom +=  (event.angleDelta().y() >0)*self.zoomStep + (event.angleDelta().y()<0)*self.zoomStep
        
        # zoom in
        if (event.angleDelta().y() >0 and self.zoom <self.zoomRange[1]):
            self.zoom +=self.zoomStep
            self.scale(self.zoomInFactor, self.zoomInFactor)
        # zoom out
        elif (event.angleDelta().y() <0 and self.zoom > self.zoomRange[0]):
            self.zoom -=self.zoomStep
            self.scale(1/self.zoomInFactor, 1/self.zoomInFactor)
