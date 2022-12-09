from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    turn = "player_1"
    score = [0,0]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 826)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.score_board = QtWidgets.QGroupBox(self.centralwidget)
        self.score_board.setMaximumSize(QtCore.QSize(16777215, 100))
        self.score_board.setObjectName("score_board")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.score_board)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.player_1 = QtWidgets.QLabel(self.score_board)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.player_1.setFont(font)
        self.player_1.setObjectName("player_1")
        self.horizontalLayout_2.addWidget(self.player_1)

        self.player_1_score = QtWidgets.QLabel(self.score_board)
        self.player_1_score.setFont(font)
        self.player_1_score.setText(str(self.score[0]))
        self.player_1.setStyleSheet("border-top: 3px solid green;\n")
        self.player_1_score.setObjectName("player_1_score")
        self.horizontalLayout_2.addWidget(self.player_1_score)

        spacerItem = QtWidgets.QSpacerItem(506, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.player_2 = QtWidgets.QLabel(self.score_board)
        self.player_2.setFont(font)
        self.player_2.setObjectName("player_2")
        self.horizontalLayout_2.addWidget(self.player_2)

        self.player_2_score = QtWidgets.QLabel(self.score_board)
        self.player_2_score.setFont(font)
        self.player_2_score.setText(str(self.score[1]))
        self.player_2_score.setObjectName("player_2_score")
        self.horizontalLayout_2.addWidget(self.player_2_score)
        self.verticalLayout.addWidget(self.score_board)

        self.play_grid = QtWidgets.QFrame(self.centralwidget)
        self.play_grid.setStyleSheet("QPushButton{\n"
                                    "   border: 1px solid black;\n"
                                    "   color: black;"
                                    "}")
        self.play_grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.play_grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.play_grid.setObjectName("play_grid")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.play_grid)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        
        
        self.cell = [[QtWidgets.QPushButton(self.play_grid) for _ in range(3)]for _ in range(3)]
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(72)
        for row in range(3):
            for col in range(3):
                self.cell[row][col].setMinimumSize(QtCore.QSize(200, 200))
                self.cell[row][col].setFont(font)
                self.cell[row][col].setFlat(True)
                self.cell[row][col].setObjectName("cell_{0}{1}".format(row, col))
                self.gridLayout_2.addWidget(self.cell[row][col], row, col, 1, 1)
                self.cell[row][col].clicked.connect(lambda t, r=row, c=col : self.play(self.cell[r][c]))

        self.winner = QtWidgets.QLabel(self.play_grid)
        font.setPointSize(45)
        self.winner.setFont(font)
        self.winner.setStyleSheet("background-color: lightgray;\n")
        self.winner.setText("player 1 wins")
        self.winner.setAlignment(QtCore.Qt.AlignCenter)
        self.winner.setObjectName("winner")
        self.winner.setHidden(True)
        self.gridLayout_2.addWidget(self.winner, 0, 0, 3, 3)

        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.play_grid)

        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setMaximumHeight(70)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.play_again = QtWidgets.QPushButton(self.footer)
        self.play_again.setMinimumSize(QtCore.QSize(0, 50))
        self.play_again.setMaximumSize(QtCore.QSize(200, 16777215))
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(18)
        self.play_again.setFont(font)
        self.play_again.clicked.connect(self.new_game)
        self.play_again.setEnabled(False)
        self.play_again.setObjectName("play_again")

        self.horizontalLayout.addWidget(self.play_again)
        self.verticalLayout.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.play_again.clicked.connect(self.new_game)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def new_game(self):
        for row in range(3):
            for col in range(3):
                self.cell[row][col].setText("")
                self.cell[row][col].setEnabled(True)
        self.play_again.setEnabled(False)
        self.winner.setHidden(True)

    def check_rows(self):
        for row in self.cell:
            if (row[0].text() == row[1].text() == row[2].text() != ""):
                return row[0].text()
        else:
            return ""

    def check_columns(self):
        for col in range(3):
            if (self.cell[0][col].text() == self.cell[1][col].text() == self.cell[2][col].text() != ""):
                return self.cell[0][col].text()
        else:
            return ""

    def check_diagonals(self):
        if (self.cell[0][0].text() == self.cell[1][1].text() == self.cell[2][2].text() != ""):
            return self.cell[0][0].text()
        elif(self.cell[0][2].text() == self.cell[1][1].text() == self.cell[2][0].text() != ""):
            return self.cell[0][2].text()
        else:
            return ""


    def play(self, cell):
        if self.turn == "player_1":
            cell.setText("X")
            cell.setEnabled(False)
            self.turn = "player_2"
            self.player_2.setStyleSheet("border-top: 2.5px solid green;\n")
            self.player_1.setStyleSheet("border-top: none;\n")
        else:
            cell.setText("O")
            cell.setEnabled(False)
            self.turn = "player_1"
            self.player_1.setStyleSheet("border-top: 2.5px solid green;\n")
            self.player_2.setStyleSheet("border-top: none;\n")
        self.check_for_winner()

    def check_for_winner(self):
        empty_cell = 0
        for row in range(3):
            for col in range(3):
                if (self.cell[row][col].text() == ""):
                    empty_cell += 1
        if (empty_cell == 0):
            self.winner.setText("Draw")
        else:
            rows, cols, diags = (self.check_rows(), self.check_columns(), self.check_diagonals())
            if ("X" in [rows, cols, diags]):
                self.score[0] += 1
                self.player_1_score.setText(str(self.score[0]))
                self.winner.setText("Player 1 WINS !!")
            elif ("O" in [rows, cols, diags]):
                self.score[1] += 1
                self.player_2_score.setText(str(self.score[1]))
                self.winner.setText("Player 2 WINS !!")
            else:
                return

        for row in range(3):
            for col in range(3):
                self.cell[row][col].setEnabled(False)
        self.play_again.setEnabled(True)
        self.winner.setHidden(False)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.score_board.setTitle(_translate("MainWindow", "Score Board"))
        self.player_1.setText(_translate("MainWindow", "Player 1: "))
        self.player_2.setText(_translate("MainWindow", "Player 2: "))
        self.play_again.setText(_translate("MainWindow", "New Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
