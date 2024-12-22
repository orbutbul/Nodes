import sys
from PyQt6.QtWidgets import *

from node_editor_wnd import NodeEditorWnd


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # where node editor information
    wnd = NodeEditorWnd()

    sys.exit(app.exec())

