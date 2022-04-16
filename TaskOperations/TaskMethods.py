from TaskOperations.DbConnect import Database


class Task(Database):
    def __init__(self, name, status):
        self.name = name
        self.status = status

        Database.cursor.execute(f"INSERT INTO List ('name','status')"
                       f"VALUES ('{self.name}','{self.status}');"
                       )
        Database.connection.commit()

    @classmethod
    def delete_task(cls, name):
        Database.cursor.execute(f"DELETE FROM List WHERE name = '{name}';")
        Database.connection.commit()

    @classmethod
    def delete_done_tasks(cls):
        Database.cursor.execute(f"DELETE FROM List WHERE status = '1';")
        Database.connection.commit()

    @classmethod
    def update_task_status(cls, name, status):
        Database.cursor.execute(f'''UPDATE List
                        SET status = '{status}'
                        WHERE name = '{name}';''')
        Database.connection.commit()


