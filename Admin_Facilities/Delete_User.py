from Db_Helper import Db_Helper

class Delete_User:
    def __init__(self, username):
        self.username = username
        self.db_helper = Db_Helper()

    def delete_user(self):
        try:
            self.db_helper.connect()
            query = "DELETE FROM users WHERE username = %s"
            values = (self.username,)
            self.db_helper.execute_query(query, values)
            print(f"User {self.username} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            self.db_helper.close_connection()
