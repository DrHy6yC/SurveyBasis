from PyQt5 import QtCore, QtGui, QtWidgets

class EventUI(QtCore.QObject):
    signalUI = QtCore.pyqtSignal()


class MainWinUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 450, 180))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 450, 70))
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        font.setPointSize(20)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 300, 450, 70))
        self.pushButton_1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pushButton_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 380, 450, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 460, 450, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 540, 450, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FUNNY ENGLISH"))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton_1"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
