from PyQt6.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Spooky Editor")
        self.resize(1024, 768)
        # Center window
        fg = self.frameGeometry()
        fg.moveCenter(self.screen().availableGeometry().center())
        self.move(fg.topLeft())
