import sqlite3

class UserManager():
    
    def __init__(self, db_path='users.db'):
        self.db_path = db_path
        
    def add_user(self, name, email, role):
        
        con = sqlite3.connect(self.db_path) #Cria uma conexão com o banco de dados
        cur = con.cursor() #Cria um cursor para iterar sobre o banco de dados
        
        cursor.execute('''INSERT TO users (name, email, role) VALUES (?, ?, ?)''', (name, email, role))
        con.commit
        con.close
    
    def edit_users(self, user_id, name=None, email=None, role=None):
        
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        query = "UPDATE users SET"
        
        updates = []
        params = []
        
        if name:
            updates.append("name = ?")
            params.append(name)
        if email:
            updates.append("email = ?")
            params.append(email)
        if role:
            updates.append("role = ?")
            params.append(role)
        
        query += ", ".join(updates) +" WHERE id = ?"
        params.append(users_id)
        cur.execute(query, tuple(params))
        con.commit
        con.close
    
    def delete_user(self, user_id):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        con.commit
        con.close
        
    def list_users(self):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        
        cur.execute("SELECT * FROM users")
        users = users.fetchall()
        con.close()
        return users
            
            
        