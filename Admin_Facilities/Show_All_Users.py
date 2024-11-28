from Db_Helper import Db_Helper

class Show_All_Users:
    def __init__(self):
        self.db_helper = Db_Helper()

    def show_all_users(self):
        try:
            self.db_helper.connect()
            query = "SELECT * FROM users"
            result = self.db_helper.fetch_data(query)
            if result:
                for user in result:
                    print(user)
            else:
                print("No users found.")
        except Exception as e:
            print(f"Error showing all users: {e}")
        finally:
            self.db_helper.close_connection()
