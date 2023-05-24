import random
import ReadFile
import WriteFile

def getParam(nameParam):
    parametrsDict = ReadFile.JSON.getDict("parametrs.json" )
    param = parametrsDict[nameParam]
    return param

def setParam(nameParam, newValueParam):
    parametrsDict = ReadFile.JSON.getDict("parametrs.json" )
    parametrsDict[nameParam] = newValueParam
    WriteFile.JSON.setParametrs(fileWithParametrs, parametrsDict)

def generatedPass():
        x = random.randint(9000000000000, 10000000000000000000000)
        return str(x)

numberQuestionStart = 1
numberQuestenStep = 1
testGrammar = "miniTest" #"English Level test. Grammar" 
nameEventEndTest = 'endTestEvent'
numberFirstUser = 1
numberLastRegUnknownUser = getParam("numberLastRegUnknownUser")
fileWithParametrs = "parametrs.json" 
accessRights = ["user", "admin", "teacher"]
idLast = getParam("idLast")



