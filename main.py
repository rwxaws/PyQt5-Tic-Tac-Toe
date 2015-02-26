import os
import random
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound

from tictactoe_ui import Ui_tictactoe


class Game(QMainWindow, Ui_tictactoe):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.turn = None
        self.timer = QTimer()

        # Shows only the close button
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.sounds = dict(circle=QSound("circle.wav"),
                           cross=QSound("cross.wav"),
                           win=QSound("win.wav"),
                           lose=QSound("lose.wav"))

        xIconPath = os.path.join("Icons", "x.png")
        oIconPath = os.path.join("Icons", "o.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

        # To make the icons appear in full color while disabled
        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        self.allButtons = self.frame.findChildren(QToolButton)
        self.availabeButtons = self.allButtons[:]

        # across the top
        self.buttonGroup1 = [
            self.button1, self.button2, self.button3]

        # across the middle
        self.buttonGroup2 = [
            self.button4, self.button5, self.button6]

        # across the bottom
        self.buttonGroup3 = [
            self.button7, self.button8, self.button9]

        # down the left side
        self.buttonGroup4 = [
            self.button1, self.button4, self.button7]

        # down the middle
        self.buttonGroup5 = [
            self.button2, self.button5, self.button8]

        # down the right side
        self.buttonGroup6 = [
            self.button3, self.button6, self.button9]

        # diagonal
        self.buttonGroup7 = [
            self.button1, self.button5, self.button9]

        # diagonal
        self.buttonGroup8 = [
            self.button3, self.button5, self.button7]

        # connections
        for button in self.allButtons:
            button.clicked.connect(self.button_clicked)
        self.actionNew_Game.triggered.connect(self.new_game)
        self.action_Exit.triggered.connect(self.close)

        self.setFocus()  # sets the focus to the main window
        self.new_game()  # starts a new game

    def new_game(self):
        self.reset()
        self.turn = 1

    def reset(self):
        self.turn = None
        self.frame.setEnabled(True)
        self.availabeButtons = self.allButtons[:]

        for button in self.availabeButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)

    def check(self):
        if self.check_list(self.buttonGroup1):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup2):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup3):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup4):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup5):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup6):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup7):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup8):
            return self.end_game(self.turn)

    def check_list(self, lst):
        for member in lst:
            if member.text() != str(self.turn):
                return False
        return True

    def end_game(self, state):
        """Ends the game"""

        if state == 1:
            self.sounds["win"].play()
            QMessageBox.information(self, ("Tic Tac Toe"), "You Win!")

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 2:
            self.sounds["lose"].play()
            QMessageBox.information(self, ("Tic Tac Toe"), "You Lose!")

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 3:
            QMessageBox.information(self, ("Tic Tac Toe"), "It's a draw!")

            for button in self.allButtons:
                button.setEnabled(False)
            return True
        return False

    def button_clicked(self):
        button = self.sender()

        self.sounds["cross"].play()

        button.setText("1")
        button.setIcon(self.xIcon)
        button.setEnabled(False)
        self.availabeButtons.remove(button)

        if self.check():
            return

        self.turn = 2
        self.frame.setEnabled(False)

        self.timer.singleShot(400, self.com_play)

    def com_play(self):
        try:
            random_button = random.choice(self.availabeButtons)
        except:  # The available button list is empty
            self.end_game(3)
            return

        self.sounds["circle"].play()
        random_button.setText("2")
        random_button.setIcon(self.oIcon)
        random_button.setEnabled(False)
        self.availabeButtons.remove(random_button)

        if self.check():
            return
        self.frame.setEnabled(True)
        self.turn = 1

app = QApplication(sys.argv)

if len(sys.argv) > 1 and sys.argv[1] == "dark":
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)

    palette.setColor(QPalette.Base, QColor(15, 15, 15))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Highlight, QColor(0, 24, 193).lighter())
    palette.setColor(QPalette.HighlightedText, Qt.black)
    palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)

    app.setPalette(palette)

game = Game()
game.show()
app.exec_()
