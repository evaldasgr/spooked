from PyQt6.QtGui import QPixmap


class Resources:
    icon = None

    @staticmethod
    def load():
        Resources.icon = QPixmap("spooked/resources/icon.png")
