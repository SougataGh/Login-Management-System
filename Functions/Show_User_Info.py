from Database_Helper.Db_Helper import Db_Helper

class Show_User_Info:
    def __init__(self, username):
        self.username = username

    def show_info(self):
        db = Db_Helper()
        db.connect_db()
        query = "SELECT username, email FROM users WHERE username = %s"
        db.cursor.execute(query, (self.username,))
        user = db.cursor.fetchone()
        db.close_connection()
        if user:
            print(f"Username: {user[0]}, Email: {user[1]}")
        else:
            print("User not found.")
