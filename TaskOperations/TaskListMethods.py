from colorama import Fore
from TaskOperations.DbConnect import Database


class TaskList(Database):
    @classmethod
    def count_tasks(cls):
        Database.cursor.execute('''SELECT COUNT(*)
                          FROM List;''')
        return list(Database.cursor.fetchone())

    @classmethod
    def create_table(cls):
        Database.cursor.execute('''CREATE TABLE List
                                   (name text, status integer);''')
        Database.connection.commit()

    @classmethod
    def print_task_list(cls):
        Database.cursor.execute(f'''SELECT * 
                           FROM List
                           ORDER BY status ASC;''')

        tasks = Database.cursor.fetchall()

        counter_undone = 1
        counter_done = 1

        print(f"{Fore.LIGHTBLUE_EX}UNDONE: ")
        for task, status in tasks:
            if status == 0:
                print(f"{counter_undone}. {task} ❌")
            counter_undone += 1

        print(f"{Fore.LIGHTBLUE_EX}\nDONE: ")
        for task, status in tasks:
            if status == 1:
                print(f"{counter_done}. {task} ✅")
            counter_done += 1

        print(f"\nTotal tasks: {TaskList.count_tasks()}")
        print(f"{Fore.LIGHTBLUE_EX}-" * 20 + "\n")