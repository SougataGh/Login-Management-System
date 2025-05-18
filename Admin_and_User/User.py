from Functions.Register import Register
from Functions.Login import Login
from Functions.Update_Info import Update_Info
from Functions.Show_User_Info import Show_User_Info

class User:
    def __init__(self, username, password=None, email=None, new_password=None, new_email=None):
        self.username = username
        self.password = password
        self.email = email
        self.new_password = new_password
        self.new_email = new_email

    def register(self):
        reg = Register(self.username, self.password, self.email)
        reg.register_user()

    def login(self):
        login = Login(self.username, self.password)
        return login.authenticate_user()

    def update_info(self):
        update = Update_Info(self.username, self.new_password, self.new_email)
        update.update_user_info()

    def show_info(self):
        show_info = Show_User_Info(self.username)
        show_info.show_info()
