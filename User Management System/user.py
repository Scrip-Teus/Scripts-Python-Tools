import sys
sys.stdout.reconfigure(encoding='utf-8')

class User():
    
    def __init__(self, id, name, email, role):
        
        self.id = id
        self.name = name
        self.email = email
        self.role = role
        
    def __str__(self):
        
        return (f"ID: {self.id} Name: {self.name} Email: {self.email} Role: {self.role}")
    
# Bloco para execução de testes

if __name__ == "__main__":
    #Teste classe User()
    result = User(1, "Usuário1", "testando@gmail.com", "Administrador")
    print(result)