import ReadFile
class Survey():
    def __init__(self):
        self.questions = dict()
        self.answers = dict()
        self.answersTrue = dict()
        self.answersUser = dict()
        self.resultSurvey = False
        self.NUMBER_QUESTION = 1
        self.inputSurvey("miniTest.csv")

    def inputSurvey(self, fileName):
        listColumn = ["Question", "Answer1", "Answer2", "Answer3", "Answer4", "TrueAnswer"]
        listDictsSurvey = ReadFile.CSV.getSurvey(fileName, listColumn)
        self.questions = listDictsSurvey[0]
        self.answers = listDictsSurvey[1]
        self.answersTrue = listDictsSurvey[2]

    
    def setAnswersUser (self,numberQuestion, numberAnswerUser):
        self.answersUser[numberQuestion] = numberAnswerUser
    
    def isEndSurvey(self):
        isEnd = False
        if len(self.answers) == len(self.answersUser):
            isEnd = True
        return isEnd
    
    def compareAnswer(self):
        if self.isEndSurvey:
            for keyDict in self.questions:
                if self.answersTrue[keyDict] == self.answersUser[keyDict]:
                    self.resultSurvey = True
                else:
                    self.resultSurvey = False
                    break
    
    def getDict(self, dict, key):
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
        text = f"Пользователь набрал {str(self.getScoreUser())} баллов\nЭто уровень {self.getLevelUser()}!\n"
        for numberAnswer, answer in self.answersUser.items():
            text = text + "Question №"+ str(numberAnswer) + " Answer: " + str(answer) + "\n"
        return text
    
    def getUserAnswers(self):
        for numberAnswer, answer in self.answersUser.items():
            print(numberAnswer, answer)

    def getLastIndexQuestions(self):
        return len(self.questions)

    def getScoreUser(self):
        scoreUser = 0
        if self.isEndSurvey:
            for key in self.answersTrue.keys():
                if self.answersTrue[key] == self.answersUser[key]:
                    scoreUser += 1
        return scoreUser


    def getLevelUser(self):
        levelUser = ""
        if self.getScoreUser() <= 30:
            levelUser = "Elementary (A1)"
        elif 30 > self.getScoreUser() >= 60:
            levelUser = "Pre-Intermediate (A2)"
        elif 60 > self.getScoreUser() >= 90:
            levelUser = "Intermediate (B1)"
        else:
            levelUser = "Upper Intermediate (B2)"
        return levelUser