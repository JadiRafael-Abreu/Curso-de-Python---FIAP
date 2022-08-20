def menu() :
    return int(input("Escolha entre as opções a seguir:\n" +
                 "(1) Criar um cadastro de usuário\n" +
                 "(2) Editar um usuário existente\n" +
                 "(3) Remover um usuário\n" +
                 "(4) Relatório de usuários\n" +
                 "(0) Sair do programa\n"))

def cadastrar(dicionario) :
    print("\n=================== CADASTRO DE USUÁRIO ======================\n")
    nome = input("Digite o nome do novo usuário: ")
    endereco = input(f"Digite o endereço do usuário {nome}: ")
    telefone = input(f"Digite o telefone do usuário {nome}: ")
    email = input(f"Digite o email do usuário {nome}: ")
    id = len(dicionario) + 1
    dicionario [id] = [nome, endereco, telefone, email]