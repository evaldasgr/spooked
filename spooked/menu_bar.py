from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenuBar, QMenu

from spooked.dialogs.about_dialog import AboutDialog


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(QMenuBar, self).__init__(parent)

        self._init_file()
        self._init_edit()
        self._init_view()
        self._init_level()
        self._init_help()

    def _init_file(self):
        menu = QMenu(self)
        menu.setTitle("File")

        item_new = QAction(self)
        item_new.setText("New")
        item_new.setShortcut("Ctrl+N")
        menu.addAction(item_new)

        item_open = QAction(self)
        item_open.setText("Open")
        item_open.setShortcut("Ctrl+O")
        menu.addAction(item_open)

        item_save = QAction(self)
        item_save.setText("Save")
        item_save.setShortcut("Ctrl+S")
        menu.addAction(item_save)

        item_save_as = QAction(self)
        item_save_as.setText("Save As...")
        item_save_as.setShortcut("Ctrl+Shift+S")
        menu.addAction(item_save_as)

        menu.addSeparator()

        item_exit = QAction(self)
        item_exit.setText("Exit")
        item_exit.setShortcut("Ctrl+Q")
        menu.addAction(item_exit)

        self.addAction(menu.menuAction())

    def _init_edit(self):
        menu = QMenu(self)
        menu.setTitle("Edit")

        item_undo = QAction(self)
        item_undo.setText("Undo")
        item_undo.setShortcut("Ctrl+Z")
        menu.addAction(item_undo)

        item_redo = QAction(self)
        item_redo.setText("Redo")
        item_redo.setShortcut("Ctrl+Y")
        menu.addAction(item_redo)

        menu.addSeparator()

        item_preferences = QAction(self)
        item_preferences.setText("Preferences...")
        menu.addAction(item_preferences)

        self.addAction(menu.menuAction())

    def _init_view(self):
        menu = QMenu(self)
        menu.setTitle("View")

        item_show_grid = QAction(self)
        item_show_grid.setText("Show Grid")
        item_show_grid.setShortcut("Ctrl+G")
        item_show_grid.setCheckable(True)
        item_show_grid.setChecked(True)
        menu.addAction(item_show_grid)

        menu.addSeparator()

        item_zoom_in = QAction(self)
        item_zoom_in.setText("Zoom In")
        item_zoom_in.setShortcut("Ctrl++")
        menu.addAction(item_zoom_in)

        item_zoom_out = QAction(self)
        item_zoom_out.setText("Zoom Out")
        item_zoom_out.setShortcut("Ctrl+-")
        menu.addAction(item_zoom_out)

        item_normal_size = QAction(self)
        item_normal_size.setText("Normal Size")
        item_normal_size.setShortcut("Ctrl+0")
        menu.addAction(item_normal_size)

        item_fit_in_view = QAction(self)
        item_fit_in_view.setText("Fit in View")
        item_fit_in_view.setShortcut("Ctrl+/")
        menu.addAction(item_fit_in_view)

        self.addAction(menu.menuAction())

    def _init_level(self):
        menu = QMenu(self)
        menu.setTitle("Level")

        item_resize = QAction(self)
        item_resize.setText("Resize...")
        menu.addAction(item_resize)

        self.addAction(menu.menuAction())

    def _init_help(self):
        menu = QMenu(self)
        menu.setTitle("Help")

        item_about = QAction(self)
        item_about.setText("About...")
        item_about.triggered.connect(lambda: AboutDialog(self.parent()).open())
        menu.addAction(item_about)

        self.addAction(menu.menuAction())
