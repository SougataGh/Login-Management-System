from Database_Helper.Db_Helper import Db_Helper

class Update_Info:
    def __init__(self, username, new_password=None, new_email=None):
        self.username = username
        self.new_password = new_password
        self.new_email = new_email

    def update_user_info(self):
        db = Db_Helper()
        db.connect_db()
        if self.new_password:
            query = "UPDATE users SET password = %s WHERE username = %s"
            db.cursor.execute(query, (self.new_password, self.username))
        if self.new_email:
            query = "UPDATE users SET email = %s WHERE username = %s"
            db.cursor.execute(query, (self.new_email, self.username))
        db.connection.commit()
        db.close_connection()
        print("User information updated successfully.")
