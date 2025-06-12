from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow

from .menu_bar import MenuBar
from .panels.entities_panel import EntitiesPanel
from .panels.layers_panel import LayersPanel
from .panels.level_panel import LevelPanel
from .panels.properties_panel import PropertiesPanel
from .panels.tiles_panel import TilesPanel
from .resources.resources import Resources
from .status_bar import StatusBar


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
        self.setStatusBar(StatusBar(self))

        self.setCentralWidget(LevelPanel(self))
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, EntitiesPanel(self))
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, TilesPanel(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, LayersPanel(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, PropertiesPanel(self))
