from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow

from .menu_bar import MenuBar
from .resources.resources import Resources


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(Resources.icon))
        self.setWindowTitle("Spooky Editor")
        self.resize(1024, 768)
        # Center window
        fg = self.frameGeometry()
        fg.moveCenter(self.screen().availableGeometry().center())
        self.move(fg.topLeft())

        self.setMenuBar(MenuBar(self))
