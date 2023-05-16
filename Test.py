import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from SurveyUI import Ui_MainWindow, EventUI
from Survey import Survey
import Constant 


class Test(QMainWindow, Survey): 
    def __init__(self):
        super(Test, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inputSurvey(Constant.testGrammar + ".csv")
        self.dictButtons = dict()
        self.setDictButtons()
        self.setFunctionButton()
        self.numberQuestion = Constant.numberQuestionStart
        self.setTextUI(self.numberQuestion)
        self.setTextObjectUI(self.ui.label, Constant.testGrammar)
        self.createEvent(Constant.nameEventEndTest, self.resultOutput)
        
    def createEvent(self, nameEvent, funcEvent):
        setattr(self, nameEvent, EventUI())
        print(getattr(self, nameEvent))
        getattr(self, nameEvent).signalUI.connect(funcEvent)
    
    def createButtonEvent(self,nameEvent, funcEvent):
        setattr(self, nameEvent, EventUI())
        print(getattr(self, nameEvent))
        getattr(self, nameEvent).signalUI.connect(funcEvent)

    def setDictButtons(self):
        i = 1
        for typeUI in self.ui.__dict__.values():
            if  type(typeUI) == QPushButton: 
                self.dictButtons[i] = typeUI
                i += 1

    def setFunctionButton(self):
        #for value in self.dictButtons.values():
        #    value.clicked.connect()
        
        self.dictButtons[1].clicked.connect(lambda: self.nextQuestion(1))
        self.dictButtons[2].clicked.connect(lambda: self.nextQuestion(2))
        self.dictButtons[3].clicked.connect(lambda: self.nextQuestion(3))
        self.dictButtons[4].clicked.connect(lambda: self.nextQuestion(4))
    
    def setTextObjectUI(self, objectUI, inputText):
        _translate = QtCore.QCoreApplication.translate
        objectUI.setText(_translate("MainWindow", inputText))
    
    def nextQuestion(self, numberButton):
        if self.numberQuestion < self.getLastIndex():
            self.setAnswersUser(self.numberQuestion, numberButton)
            self.numberQuestion += Constant.numberQuestenStep
            self.setTextUI(self.numberQuestion)
        else:
            self.answersUser[self.numberQuestion] = numberButton
            self.setTextObjectUI(self.ui.textEdit, self.getResultSelectedAnswer())
            getattr(self, Constant.nameEventEndTest).signalUI.emit()
    
    def setTextUI(self, numberQuestion):
        self.setTextObjectUI(self.ui.textEdit, self.questions[numberQuestion])
        self.setTextObjectUI(self.dictButtons[1], self.answers[numberQuestion][1])
        self.setTextObjectUI(self.dictButtons[2], self.answers[numberQuestion][2])
        self.setTextObjectUI(self.dictButtons[3], self.answers[numberQuestion][3])
        self.setTextObjectUI(self.dictButtons[4], self.answers[numberQuestion][4])
    
    def resultOutput(self):
        self.dictButtons[1].setVisible(False)
        self.dictButtons[2].setVisible(False)
        self.dictButtons[3].setVisible(False)
        self.dictButtons[4].setVisible(False)
        self.ui.textEdit.setGeometry(QtCore.QRect(20, 100, 450, 490))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Test()
    win.show()
    sys.exit(app.exec_())