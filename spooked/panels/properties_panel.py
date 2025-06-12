from PyQt6.QtWidgets import QDockWidget


class PropertiesPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Properties")
        self.setMinimumWidth(150)
