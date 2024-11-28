from Db_Helper import Db_Helper

class Update_Info:
    def __init__(self, username, new_password=None, new_email=None):
        self.username = username
        self.new_password = new_password
        self.new_email = new_email
        self.db_helper = Db_Helper()

    def update_user_info(self):
        try:
            self.db_helper.connect()
            if self.new_password:
                query = "UPDATE users SET password = %s WHERE username = %s"
                values = (self.new_password, self.username)
                self.db_helper.execute_query(query, values)
                print("Password updated successfully.")
            
            if self.new_email:
                query = "UPDATE users SET email = %s WHERE username = %s"
                values = (self.new_email, self.username)
                self.db_helper.execute_query(query, values)
                print("Email updated successfully.")
        except Exception as e:
            print(f"Error updating user info: {e}")
        finally:
            self.db_helper.close_connection()
