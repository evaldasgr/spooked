from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Spooky Editor")
        self.resize(1024, 768)
        # Center window
        fg = self.frameGeometry()
        fg.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(fg.topLeft())
