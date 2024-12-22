from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from node_scene import Scene
from node_graphics_view import QDMGraphicsView
class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # sets the size of the window
        self.setGeometry(300,300,800,800)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # the graph window needs to be initialized with a graphics scene, doing this gives us scrolling and other features
        self.scene = Scene()
        self.grScene = self.scene.grScene


        # the graphics view lets the graphics scene be viewed...
        self.view = QDMGraphicsView(self.grScene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("MAMA")
        self.show()
        
        self.addDebugContent()
        
        
    def addDebugContent(self):
        greenBrush = QBrush(QColor("green"))
        outlinePen = QPen(QColor("black"))
        outlinePen.setWidth(2)
        
        
        rect = self.grScene.addRect(-100,-100,800,1000,outlinePen,greenBrush)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable,True)
        
        text = self.grScene.addText("Test Text")
        text.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        widget1 = QPushButton("Hey mama")
        proxy1 =self.grScene.addWidget(widget1)
        # proxy1.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable,True)
        proxy1.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        proxy1.setPos(0,40)
        
        
        widget2 = QTextEdit()
        flags =(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable
            | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
        )
        proxy2= self.grScene.addWidget(widget2)
        proxy2.setFlags(flags)
        proxy2.setPos(0,50)