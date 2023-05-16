import csv
class Survey():
    def __init__(self):
        self.questions = {}
        self.answers = {}
        self.answersTrue = {}
        self.answersUser = {}
        self.resultSurvey = False

    def inputSurvey(self, objectFile):
        FILENAME = objectFile
        with open(FILENAME, "r", newline="") as file:
            dictReaderExt = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_NONE)
            keyDict = 1
            for rowDictExt in dictReaderExt:
                self.questions[keyDict] = rowDictExt["Question"]
                self.answers[keyDict] = {
                    1: rowDictExt["Answer1"],
                    2: rowDictExt["Answer2"],
                    3: rowDictExt["Answer3"],
                    4: rowDictExt["Answer4"]}
                self.answersTrue[keyDict] = int(rowDictExt["TrueAnswer"])
                keyDict += 1
    
    def setAnswersUser (self,numberQuestion, numberAnswerUser):
        self.answersUser[numberQuestion] = numberAnswerUser
    
    def endSurvey(self):
        isEnd = False
        if len(self.answers) == len(self.answersUser):
            isEnd = True
        return isEnd
    
    def compareAnswer(self):
        if self.endSurvey:
            for keyDict in self.questions:
                if self.answersTrue[keyDict] == self.answersUser[keyDict]:
                    self.resultSurvey = True
                else:
                    self.resultSurvey = False
                    break
    
    def getDict(self,dict, key):
        print(dict[key])
        

    def takingSurveyInConsole(self):
        for keyDict in self.questions:
            print(self.questions[keyDict])
            for answer in self.answers[keyDict]:
                print(answer, self.answers[keyDict][answer])
            self.setAnswersUser(keyDict, int(input("Введите номер ответа: ")))

    def getResultSurvey(self):
        if self.resultSurvey:
            print("Тест пройден")
        else:
            print("Тест не пройден")
    
    def getResultSurveyTest(self):
        if self.resultSurvey:
            return "Тест пройден"
        else:
            return "Тест не пройден"

    def getResultSelectedAnswer(self):
        text = ""
        for numberAnswer, answer in self.answersUser.items():
            text = text + "Question №"+ str(numberAnswer) + " Answer: " + str(answer) + "\n"
        return text
    
    def getUserAnswers(self):
        for numberAnswer, answer in self.answersUser.items():
            print(numberAnswer, answer)

    def getLastIndex(self):
        return len(self.questions)