import sys

from PyQt6.QtWidgets import QApplication

from .resources.resources import Resources
from .window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Resources.load()

    window = Window()
    window.show()

    sys.exit(app.exec())
