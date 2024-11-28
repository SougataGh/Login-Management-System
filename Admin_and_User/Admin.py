from Update_Info import Update_Info
from Delete_User import Delete_User
from Show_All_Users import Show_All_Users

class Admin:
    def __init__(self):
        pass

    def update_user_info(self, username, new_password=None, new_email=None):
        update = Update_Info(username, new_password, new_email)
        update.update_user_info()

    def delete_user(self, username):
        delete = Delete_User(username)
        delete.delete_user()

    def show_all_users(self):
        show = Show_All_Users()
        show.show_all_users()
