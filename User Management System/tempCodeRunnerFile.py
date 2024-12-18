from user_manager import UserManager
from database import setup_database

def main():
    setup_database()
    manager = setup_database()

    while True:
        print("Sistema de Gerenciamento de Usuários")
        print("[1] Adicionar Usuário")
        print("[2] Listar Usuários")
        print("[3] Editar Usuário")
        print("[4] Excluir Usuário")
        print("[0] Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome: ")
            email = input("Email: ")
            role = input("Função: ")
            manager.add_user(name, email, role)
            print("Usuário adicionado com sucesso!")

        elif choice == '2':
            users = manager.list_users()
            print("\nUsuários cadastrados:")
            for user in users:
                print(f"ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}, Função: {user[3]}")

        elif choice == '3':
            user_id = int(input("ID do usuário a editar: "))
            name = input("Novo nome (pressione Enter para ignorar): ")
            email = input("Novo email (pressione Enter para ignorar): ")
            role = input("Nova função (pressione Enter para ignorar): ")
            manager.edit_user(user_id, name or None, email or None, role or None)
            print("Usuário editado com sucesso!")

        elif choice == '4':
            user_id = int(input("ID do usuário a excluir: "))
            manager.delete_user(user_id)
            print("Usuário excluído com sucesso!")

        elif choice == '0':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()
