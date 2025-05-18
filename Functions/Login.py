from Database_Helper.Db_Helper import Db_Helper

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate_user(self):
        db = Db_Helper()
        db.connect_db()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        db.cursor.execute(query, (self.username, self.password))
        result = db.cursor.fetchone()
        db.close_connection()
        if result:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False
