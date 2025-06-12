from PyQt6.QtWidgets import QDockWidget


class TilesPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Tiles")
        self.setMinimumWidth(150)
