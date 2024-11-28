from Db_Helper import Db_Helper

class Show_User_Info:
    def __init__(self, username):
        self.username = username
        self.db_helper = Db_Helper()

    def show_info(self):
        try:
            self.db_helper.connect()
            query = "SELECT * FROM users WHERE username = %s"
            values = (self.username,)
            result = self.db_helper.fetch_data(query, values)
            if result:
                print(f"User Info: {result}")
            else:
                print("User not found.")
        except Exception as e:
            print(f"Error showing user info: {e}")
        finally:
            self.db_helper.close_connection()
