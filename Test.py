import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from SurveyUI import MainWinUI, EventUI
from LoginUI import LogWinUI
from Survey import Survey
from User import User
import Constant 

class LoginWin(QMainWindow):
    def __init__(self):
        super(LoginWin,self).__init__()
        self.logWinUI = LogWinUI()
        self.logWinUI.setupUi(self)
        self.logWinUI.pushButtonLogin.clicked.connect(showMainWin)
        self.logWinUI.pushButtonSignUp.clicked.connect(self.addUser)
    
    

    def addUser(self):
        with open("users.csv", "a", newline="") as file:
            columns = ["nameUser", "passUser"]
            writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
            writer.writerow({"nameUser": self.logWinUI.lineEditLogin.text(), 
                                "passUser": self.logWinUI.lineEditPass.text()})        


class Test(QMainWindow, Survey): 
    def __init__(self):
        super(Test, self).__init__()
        self.mainWinUI = MainWinUI()
        self.mainWinUI.setupUi(self)
        self.inputSurvey(Constant.testGrammar + ".csv")
        self.dictButtons = dict()
        self.setDictButtons()
        self.setFunctionButton()
        self.numberQuestion = Constant.numberQuestionStart
        self.setTextOnTestUI(self.numberQuestion)
        self.setTextObjectUI(self.mainWinUI.label, Constant.testGrammar)
        self.createEvent(Constant.nameEventEndTest, self.endChangeUI)

    def createEvent(self, nameEvent, funcEvent):
        setattr(self, nameEvent, EventUI())
        print(getattr(self, nameEvent))
        getattr(self, nameEvent).signalUI.connect(funcEvent)

    def setDictButtons(self):
        i = 1
        for typeUI in self.mainWinUI.__dict__.values():
            if  type(typeUI) == QPushButton: 
                self.dictButtons[i] = typeUI
                i += 1

    def setFunctionButton(self):
        self.dictButtons[1].clicked.connect(lambda: self.nextQuestion(1))
        self.dictButtons[2].clicked.connect(lambda: self.nextQuestion(2))
        self.dictButtons[3].clicked.connect(lambda: self.nextQuestion(3))
        self.dictButtons[4].clicked.connect(lambda: self.nextQuestion(4))
    
    def setTextObjectUI(self, objectUI, inputText):
        _translate = QtCore.QCoreApplication.translate
        objectUI.setText(_translate("MainWindow", inputText))

    def setTextOnTestUI(self, numberQuestion):
        self.setTextObjectUI(self.mainWinUI.textEdit, self.questions[numberQuestion])
        for key, button in self.dictButtons.items():
            self.setTextObjectUI(button, self.answers[numberQuestion][key])
    
    def endChangeUI(self):
        for button in self.dictButtons.values():
            button.setVisible(False)
        self.mainWinUI.textEdit.setGeometry(QtCore.QRect(20, 100, 450, 490))

    def nextQuestion(self, numberButton):
        self.setAnswersUser(self.numberQuestion, numberButton)
        if self.numberQuestion < self.getLastIndexQuestions():
            self.numberQuestion += Constant.numberQuestenStep
            self.setTextOnTestUI(self.numberQuestion)
        
        else:
            self.setTextObjectUI(self.mainWinUI.textEdit, self.getResultSelectedAnswer())
            getattr(self, Constant.nameEventEndTest).signalUI.emit()



if __name__ == "__main__":
    def showMainWin():
        mainWin.show()
        logWin.close()

    app = QApplication(sys.argv)
    logWin = LoginWin()
    logWin.show()
    mainWin = Test()
    
    sys.exit(app.exec_())