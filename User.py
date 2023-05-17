import Constant
import random
class User():
    def __init__(self):
        self.nameUser = "User_" + str(Constant.numberLastRegUser)
        self.passUser = self.generatedPass()
        self.levelUser = "Unknown (A0)"
        self.accessRights = Constant.accessRights[0]
        self.emailUser = "dr.hy6yc@gmail.com"
        self.phone = 89181385293
        self.loginTelegram = "dr.hy6yc"

    def generatedPass(self):
        x = random.randint(9000000000000, 10000000000000000000000)
        return str(x)