from PyQt6.QtWidgets import QDockWidget


class EntitiesPanel(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Entities")
        self.setMinimumWidth(150)
