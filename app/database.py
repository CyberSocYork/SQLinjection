import sqlite3
import os
from sqlite3 import Error


def create_connection():
    try:
        conn = sqlite3.connect('pythonsqlite.db')
        return conn

    except Error as e:
        print(e)

    return None




