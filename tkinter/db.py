import sqlite3
from pathlib import Path

FILE_NAME = 'database.db'
DIR_NAME = Path(__file__).parent
HABILIDADE_TABLE_NAME = 'habilidades_table'


def create_tables():
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {HABILIDADE_TABLE_NAME}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "habilidade_name TEXT"
        ")"
    )

    cursor.close()
    conn.close()


create_tables()

