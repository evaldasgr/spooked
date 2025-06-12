from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QDialogButtonBox, QDialog

from ..resources.resources import Resources


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About")
        self.setModal(True)

        skull = QLabel()
        skull.setFixedSize(128, 128)
        skull.setPixmap(Resources.icon.scaledToHeight(skull.height()))

        text = QLabel("Spooky Editor - Level editor for various game projects.\nProgrammed by Evaldas Granickas.")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(skull, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(buttons)
        self.setLayout(layout)
