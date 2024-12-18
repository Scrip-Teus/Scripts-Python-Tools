import sqlite3

def setup_database(db_path="users.db"):
    
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    cur.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       role TEXT NOT NULL
                       )
                ''')
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    setup_database()
    print("Banco de dados configurado com sucesso!")