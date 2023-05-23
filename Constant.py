import ReadFile
import WriteFile

def changeIdLast(self):
    self.idLast += 1

def changeNumberLastRegUnknownUser(self):
    self.numberLastRegUnknownUser += 1

def getParam(nameParam):
    parametrsDict = ReadFile.JSON.getDict("parametrs.json" )
    param = parametrsDict[nameParam]
    return param

def setParam(nameParam, newValueParam):
    parametrsDict = ReadFile.JSON.getDict("parametrs.json" )
    parametrsDict[nameParam] = newValueParam
    WriteFile.JSON.setParametrs(fileWithParametrs, parametrsDict)

numberQuestionStart = 1
numberQuestenStep = 1
testGrammar = "miniTest" #"English Level test. Grammar" 
nameEventEndTest = 'endTestEvent'
numberFirstUser = 1
numberLastRegUnknownUser = getParam("numberLastRegUnknownUser")
fileWithParametrs = "parametrs.json" 
accessRights = ["user", "admin", "teacher"]
idLast = getParam("idLast")


