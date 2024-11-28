from User import User
from Admin import Admin

def main():
    user = User(username="john_doe", password="1234", email="john@example.com")
    user.register()
    if user.login():
        user.show_info()
        user.update_info()

    admin = Admin()
    admin.show_all_users()
    admin.update_user_info("john_doe", new_password="new_pass")
    admin.delete_user("john_doe")

if __name__ == "__main__":
    main()
