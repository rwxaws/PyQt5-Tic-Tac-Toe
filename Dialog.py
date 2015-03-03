import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dialog(QDialog):

    def __init__(self, parent=None, state=None):
        super(Dialog, self).__init__(parent)
        self.setModal(True)

        layout = QGridLayout(self)

        pixmapLabel = QLabel("")
        label = QLabel("")
        okButton = QPushButton("Ok")

        winPixmap = QPixmap(os.path.join("Icons", "winIcon.png"))
        losePixmap = QPixmap(os.path.join("Icons", "loseIcon.png"))
        drawPixmap = QPixmap(os.path.join("Icons", "drawIcon.png"))

        if state == 1:
            pixmapLabel.setPixmap(winPixmap)
            label.setText("You have won")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        elif state == 2:
            pixmapLabel.setPixmap(losePixmap)
            label.setText("You have lost")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        else:
            pixmapLabel.setPixmap(drawPixmap)
            label.setText("It's a draw")
            layout.addWidget(pixmapLabel, 0, 0)
            layout.addWidget(label, 0, 1)
            layout.addWidget(okButton, 1, 1)

        okButton.clicked.connect(self.hide)


if __name__ == "__main__":
    app = QApplication([])
    dialog = Dialog(state=3)
    dialog.show()
    app.exec_()
