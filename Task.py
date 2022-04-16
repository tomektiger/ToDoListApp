import sqlite3
from colorama import Fore, init

connection = sqlite3.connect('TaskList.db')
cursor = connection.cursor()


class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        cursor.execute(f"INSERT INTO List ('name','status')"
                       f"VALUES ('{self.name}','{self.status}');"
                       )
        connection.commit()

    @classmethod
    def delete_task(cls, name):
        cursor.execute(f"DELETE FROM List WHERE name = '{name}';")
        connection.commit()

    @classmethod
    def delete_done_tasks(cls):
        cursor.execute(f"DELETE FROM List WHERE status = '1';")
        connection.commit()

    @classmethod
    def update_task_status(cls, name, status):
        cursor.execute(f'''UPDATE List
                        SET status = '{status}'
                        WHERE name = '{name}';''')
        connection.commit()


class TaskList:

    @classmethod
    def count_tasks(cls):
        cursor.execute('''SELECT COUNT(*)
                          FROM List;''')
        return list(cursor.fetchone())

    @classmethod
    def create_table(cls):
        cursor.execute("CREATE TABLE List"
                       "(name text, status integer);")
        connection.commit()

    @classmethod
    def print_task_list(cls):
        print(f"{Fore.LIGHTBLUE_EX}Tasks: ")
        cursor.execute(f'''SELECT * 
                           FROM List
                           ORDER BY status ASC;''')

        tasks = cursor.fetchall()

        counter = 1
        for task, status in tasks:
            if status == 0:
                print(f"{counter}. {task} ❌")
            else:
                print(f"{counter}. {task} ✅")
            counter += 1

        print(f"\nTotal tasks: {TaskList.count_tasks()}")
        print(f"{Fore.LIGHTBLUE_EX}-" * 20 + "\n")

