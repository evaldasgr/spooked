from PyQt6.QtWidgets import QDockWidget


class LayersPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Layers")
        self.setMinimumWidth(150)
