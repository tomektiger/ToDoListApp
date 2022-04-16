import sys
from TaskOperations.Menu import *
from TaskOperations.TaskMethods import Task
from TaskOperations.TaskListMethods import TaskList
from colorama import Fore, init
import os

os.system('cls')
while True:
    os.system('cls')
    init(autoreset=True)

    print_text_list()
    TaskList.print_task_list()
    print_options()
    try:
        user_choice = int(input(f"{Fore.LIGHTBLUE_EX}Which one do you choose ?:{Fore.WHITE} "))
        if user_choice > 6 or user_choice < 1:
            print(f"{Fore.RED}!!! YOU HAVE TO CHOICE CORRECT NUMBER !!!")
            continue
    except ValueError:
        os.system('cls')
        print(f"{Fore.RED}!!! YOU HAVE TO USE NUMBER  !!!")
    else:
        if user_choice == 1:
            os.system('cls')
            name = input(f"{Fore.LIGHTBLUE_EX}Please provide new task name:{Fore.WHITE} ")
            new_task = Task(name, 0)

        elif user_choice == 2:
            os.system('cls')
            TaskList.print_task_list()
            name = input(f"{Fore.LIGHTBLUE_EX}Which task do you want to delete? (provide name):{Fore.WHITE} ")
            Task.delete_task(name)

        elif user_choice == 3:
            os.system('cls')
            TaskList.print_task_list()
            name = input(f"{Fore.LIGHTBLUE_EX}Which task do you want to mark as done? (provide name):{Fore.WHITE} ")
            Task.update_task_status(name, 1)

        elif user_choice == 4:
            os.system('cls')
            TaskList.print_task_list()
            name = input(f"{Fore.LIGHTBLUE_EX}Which task do you want to mark as undone? (provide name):{Fore.WHITE} ")
            Task.update_task_status(name, 0)

        elif user_choice == 5:
            os.system('cls')
            TaskList.print_task_list()
            decision = input(f"{Fore.LIGHTBLUE_EX}Are you sure to delete all done tasks ? :{Fore.WHITE} ")
            if decision in ["yes", "y", "Y", "Yes"]:
                Task.delete_done_tasks()
        elif user_choice == 6:
            sys.exit()
