from Db_Helper import Db_Helper

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db_helper = Db_Helper()

    def authenticate_user(self):
        try:
            self.db_helper.connect()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            values = (self.username, self.password)
            result = self.db_helper.fetch_data(query, values)
            if result:
                print("Login successful!")
                return True
            else:
                print("Invalid credentials.")
                return False
        except Exception as e:
            print(f"Error logging in: {e}")
        finally:
            self.db_helper.close_connection()
