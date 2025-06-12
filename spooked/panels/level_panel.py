from PyQt6.QtWidgets import QDockWidget


class LevelPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Level")
