import os
import time
from getpass import getpass


# efeitos de interface
def dormir (tempo):
        time.sleep(tempo)

def transicao():
    tipo_sistema = os.name
    if tipo_sistema == "nt":
        os.system("cls")
    else:   
        os.system("clear")


# Funções de segurança da senha
# requisitos de senha
def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

# Função para cadastrar a senha
def cadastrar_senha():
    while True:
        print("-----------------------------------------")
        print("Sua senha deve ter no mínimo 8 caracteres")
        print("Uma letra maiúscula e uma letra minúscula")
        print("Um caracter numérico")
        senha_usuario = getpass("Cadastre uma senha: ")
        if validar_senha(senha_usuario):
            print("Senha cadastrada com sucesso!")
            dormir(2)
            return senha_usuario
        else:
            print("Erro: A senha não cumpriu os requisitos")
            dormir(2)
            sequencia = input("Deseja tentar outra senha? [s/n] ").lower()
            if sequencia == "n":
                break  # Sai do loop se o usuário não quiser tentar outra senha




# Função para adicionar usuários ao arquivo de usuários
def adicionar_usuario(arquivo_usuarios, usuario):
    if usuario == "admin":
        nome_usuario = input("Digite o nome do novo usuário: ")
        senha_usuario = cadastrar_senha()
        if nome_usuario != None and senha_usuario != None:
            with open(arquivo_usuarios, "a") as documento:
                documento.write(f"{nome_usuario},{senha_usuario}\n")
            print(f"Usuário '{nome_usuario}' adicionado com sucesso!")
            dormir(2)
    else:
        print("Você não tem o nível de acesso necessário para adicionar usuários.")
        dormir(3)



# Função para adicionar permissões ao arquivo de permissões
def adicionar_permissao(arquivo_permissoes, usuario):
    if usuario == "admin":
        nome_permissao = input("Digite o nome do usuário para adicionar permissão: ")
        acao = input("Digite a ação para a qual deseja conceder permissão [ler/escrever/executar]: ")
        arquivo = input("Digite o nome do arquivo para o qual deseja conceder permissão: ")

        with open(arquivo_permissoes, "a") as documento:
            documento.write(f"{nome_permissao},{acao},{arquivo}\n")
        print("Permissão adicionada com sucesso!")
        dormir(2)
    else:
        print("Você não tem o nível de acesso necessário para adicionar permissões.")
        dormir(3)


# Função para listar os usuários
def listar_usuarios(arquivo_usuarios):
    print("Lista de Usuários:")
    print("------------------")
    with open(arquivo_usuarios, "r") as documento:
        for line in documento:
            user, _ = line.strip().split(",")
            print(user)
    print("------------------")
    continuar = input("Pressione qualquer tecla para continuar: ")

# Função para listar as permissões
def listar_permissoes(arquivo_permissoes):
    print("Lista de Permissões:")
    print("---------------------------------------------")
    with open(arquivo_permissoes, "r") as documento:
        print("Usuário\t\tAção\t\tArquivo")
        print("---------------------------------------------")
        for line in documento:
            user, act, res = line.strip().split(",")
            print(f"{user.ljust(10)}\t{act.ljust(10)}\t{res.ljust(10)}")
    print("---------------------------------------------")
    continuar = input("Pressione qualquer tecla para continuar: ")


# autenticação do usuário
def autenticacao(arquivo_usuarios):
    seguir = True
    tentativas = 0
    while seguir:
        tentativas += 1

        usuario = input("Digite o seu nome: ")
        senha = getpass("Digite a sua senha: ")
        transicao()

        with open(arquivo_usuarios, "r") as documento:
            for line in documento:
                user, password = line.strip().split(",")
                if user == usuario and password == senha:
                    print(f"Usuário '{usuario}' autenticado com sucesso!")
                    dormir(2)
                    transicao()
                    return usuario  # Retorna o usuário se autenticado com sucesso
            print(f"Usuário ou senha inválidos. Você usou a tentativa {tentativas}/3 até ser bloqueado.")
            if tentativas == 3:
                dormir(3)
                print("Você excedeu o número permitido de tentativas. O programa será encerrado!")
                dormir(2)
                break # o break vai sair do progrma em si, pq a função não vai ter retorno
            dormir(2)
            transicao()
            escolha = input("Deseja tentar novamente? [s/n]: ").lower()
            if escolha != "s":
                seguir = False
    return None  # mesmo que retornar o boolean False


# Função para verificar as permissões do usuário
def checagem(usuario, arquivo_permissoes, acao, arquivo):
    with open(arquivo_permissoes, "r") as documento:
        for line in documento:
            user, act, res = line.strip().split(",")
            if user == usuario and act == acao and res == arquivo:
                return True
    return False



# Função principal do programa
def main():
    seguir = True
    while seguir:
        transicao()
        arquivo_usuarios = "usuarios.txt"
        arquivo_permissoes = "permissoes.txt"

        print("Bem-vindo ao sistema de controle de acesso da nossa equipe!")
        dormir(2)
        transicao()

        print("Menu Principal")
        print("[1] cadastrar usuário")
        print("[2] cadastrar permissão")
        print("[3] testar permissão")
        print("[4] listar usuários")
        print("[5] listar permissões")
        print("[6] sair")
        escolha = int(input("O que gostaria de fazer: "))

        if escolha == 1:
            print("---------------------")
            print("Somente o administrador pode realizar esta ação.")
            print("Primeiro vamos checar as suas credenciais.")
            dormir(3)
            transicao()
            #autenticação
            usuario = autenticacao(arquivo_usuarios)
            if not usuario:
                return # sai do main e encerra o programa
            adicionar_usuario(arquivo_usuarios, usuario)
        elif escolha == 2:
            print("---------------------")
            print("Somente o administrador pode realizar esta ação.")
            print("Primeiro vamos checar as suas credenciais.")
            dormir(3)
            transicao()
            #autenticação
            usuario = autenticacao(arquivo_usuarios)
            if not usuario:
                return # sai do main e encerra o programa
            adicionar_permissao(arquivo_permissoes, usuario)            
        elif escolha == 3:
            print("Faça o login com o usuário para o qual deseja checar as permissões.")
            dormir(2)
            transicao()
            #autenticação
            usuario = autenticacao(arquivo_usuarios)
            if not usuario:
                return # sai do main e encerra o programa

            print(f"Qual ação o usuário '{usuario}' deseja fazer: ")
            print("[1] ler")
            print("[2] escrever")
            print("[3] executar")
            acao = int(input("Escolha: "))
            action = ""
            if acao == 1:
                action = "ler"
            elif acao == 2:
                action = "escrever"
            elif acao == 3:
                action = "executar"
            acao = action
            arquivo = input("[nome.extensão] do arquivo (ex:notas.txt): ")

            if checagem(usuario, arquivo_permissoes, acao, arquivo):
                print("Acesso permitido")
                print(f"{usuario} tem permissão para {acao} {arquivo}")
                dormir(3)
            else:
                print("Acesso negado")
                print(f"{usuario} não tem permissão para {acao} {arquivo}")
                dormir(3)
        elif escolha == 4:
            transicao()
            listar_usuarios(arquivo_usuarios)
        elif escolha == 5:
            transicao()
            listar_permissoes(arquivo_permissoes)
        
        else:
            break # sair


main()

