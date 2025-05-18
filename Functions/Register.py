from Database_Helper.Db_Helper import Db_Helper

class Register:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register_user(self):
        db = Db_Helper()
        db.connect_db()

        # Check if the username already exists
        check_query = "SELECT * FROM users WHERE username = %s"
        db.cursor.execute(check_query, (self.username,))
        existing_user = db.cursor.fetchall()

        if existing_user:
            print("Username already exists. Try a different one.")
        else:
            insert_query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            db.cursor.execute(insert_query, (self.username, self.password, self.email))
            db.connection.commit()
            print("User registered successfully.")

        db.close_connection()
