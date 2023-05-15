from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from SurveyUI import Ui_MainWindow
from Survey import Survey
import Constant 
import sys

class Test(QMainWindow, Survey): # главное окно
    def __init__(self):
        super(Test, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inputSurvey("users.csv")
        self.addFunctionButton()
        self.numberQuestion = Constant.numberQuestionStart
        self.setButtons(self.numberQuestion)


    
    def addFunctionButton(self):
    
        self.ui.pushButton_1.clicked.connect(lambda: self.nextQuestion(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.nextQuestion(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.nextQuestion(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.nextQuestion(4))
    
    def nextQuestion(self, numberButton):
        if self.numberQuestion < self.getLastIndex():
            self.setAnswersUser(self.numberQuestion, numberButton)
            self.numberQuestion += Constant.numberQuestenStep
            self.setButtons(self.numberQuestion)
    
        else:
            self.answersUser[self.numberQuestion] = numberButton
            _translate = QtCore.QCoreApplication.translate
            self.ui.textEdit.setText(_translate("MainWindow", self.getResultSelectedAnswer()))
        
    
    def setButtons(self, numberQuestion):
        _translate = QtCore.QCoreApplication.translate
        self.ui.textEdit.setText(_translate("MainWindow", self.questions[numberQuestion]))
        self.ui.pushButton_1.setText(_translate("MainWindow", self.answers[numberQuestion][1])) 
        self.ui.pushButton_2.setText(_translate("MainWindow", self.answers[numberQuestion][2])) 
        self.ui.pushButton_3.setText(_translate("MainWindow", self.answers[numberQuestion][3])) 
        self.ui.pushButton_4.setText(_translate("MainWindow", self.answers[numberQuestion][4])) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Test()
    win.show()
    sys.exit(app.exec_())