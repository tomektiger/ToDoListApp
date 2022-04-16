from colorama import Fore


def print_text_list():
    print(f'''{Fore.LIGHTBLUE_EX}
█████████████████████████████████████████████████
█─▄─▄─█─▄▄─███▄─▄▄▀█─▄▄─███▄─▄███▄─▄█─▄▄▄▄█─▄─▄─█
███─███─██─████─██─█─██─████─██▀██─██▄▄▄▄─███─███
▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
    ''')


def print_options():
    print(f"{Fore.LIGHTBLUE_EX}Options: ")
    print("1. Add new")
    print("2. Delete existing")
    print("3. Mark as done")
    print("4. Mark as undone")
    print("5. Delete all done")
    print("6. Exit App")
