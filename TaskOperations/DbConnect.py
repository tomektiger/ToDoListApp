import sqlite3


class Database:
    connection = sqlite3.connect('../TaskList.db')
    cursor = connection.cursor()