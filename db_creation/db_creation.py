import sqlite3

from db_creation.empty_db_creation import create_empty_db
from db_creation.db_fill import fill_db
import config as config

DB_NAME = config.DB_NAME
TABLE_NAME = config.TABLE_NAME
LANG = config.LANG
VIDEOS_COUNT = config.VIDEOS_COUNT

def open_connection():
    global CON
    global CUR
    CON = sqlite3.connect(DB_NAME)
    CUR = CON.cursor()


def close_connection():
    CON.close()


def create_db():
    open_connection()
    create_empty_db(CON, CUR)
    fill_db(CON, CUR, LANG, VIDEOS_COUNT)
    close_connection()
