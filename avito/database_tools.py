import sqlite3


DB_FILE = 'base.db'


def insert_into_db(row: tuple) -> None: 
    """ Insert row into table. """  
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO secrets VALUES (?,?,?)', row)
        conn.commit()


def select_from_db(secret_key: str) -> tuple:  
    """ Get row by secret_key. """
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        res = c.execute('SELECT * FROM secrets WHERE secret_key=?', (secret_key,)).fetchone()
    return res


def delete_from_db(secret_key: str) -> None:
    """ Delete row by secret_key. """
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM secrets WHERE secret_key=?', (secret_key,))
        conn.commit()

