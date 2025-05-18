from Database_Helper.Db_Helper import Db_Helper

class Delete_User:
    def __init__(self, username):
        self.username = username

    def delete_user(self):
        db = Db_Helper()
        db.connect_db()
        query = "DELETE FROM users WHERE username = %s"
        db.cursor.execute(query, (self.username,))
        db.connection.commit()
        db.close_connection()
        print(f"User '{self.username}' has been deleted.")
