from Db_Helper import Db_Helper

class Register:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.db_helper = Db_Helper()

    def register_user(self):
        try:
            self.db_helper.connect()
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            values = (self.username, self.password, self.email)
            self.db_helper.execute_query(query, values)
            print("User registered successfully!")
        except Exception as e:
            print(f"Error registering user: {e}")
        finally:
            self.db_helper.close_connection()
