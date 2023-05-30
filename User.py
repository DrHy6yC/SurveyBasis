accessRights = ["user", "admin", "teacher"]


class User():
    def __init__(self):
        self.idUser = 0
        self.nameUser = ""
        self.fullName = ""
        self.levelUser = "Unknown (A0)"
        self.accessRights = accessRights[0]
        self.emailUser = ""
        self.phone = 0
        self.loginTelegram = ""
