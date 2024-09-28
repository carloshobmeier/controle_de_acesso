# Carlos Eduardo Domingues Hobmeier e Amanda Queiroz sobral
# se já não tiverem instalados dê: pip install mysql-connector-python bcrypt
# tem que rodar o modelo físico antes de rodar aqui

# importações
import mysql.connector
import bcrypt
from getpass import getpass
import os
import time


# funções para aprimorar a interface
def dormir():
    time.sleep(2)

def transicao():
    tipo_sistema = os.name
    if tipo_sistema == "nt":
        os.system("cls")
    else:   # como o professor usa mac
        os.system("clear")


# conexão com o banco
def conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="PUC@1234",
        database="controleAcesso"
    )


# inserts no banco de dados
def registrar_usuario(conn, username, password):
    cursor = conn.cursor()
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)", (username, hashed))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()

def registrar_permissao(conn, username, file, action):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT usuario_id FROM usuarios WHERE username = %s", (username,))
        user_id = cursor.fetchone()[0]  # Obtendo o usuario_id correspondente ao username
        cursor.execute("INSERT INTO permissoes (usuario_id, arquivo, acao) VALUES (%s, %s, %s)", (user_id, file, action))
        conn.commit()
        print("Permissão registrada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()


# autenticação do usuário
def autenticar_usuario(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM usuarios WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        print("Usuário autenticado com sucesso!")
        dormir()
        transicao()
        return True
    else:
        print("Falha na autenticação.")
        dormir()
        transicao()
        return False


# verificação da permissão para determinado arquivo
def checar_permissao(conn, username, action, file):
    cursor = conn.cursor()
    cursor.execute("SELECT p.acao FROM permissoes p JOIN usuarios u ON p.usuario_id = u.usuario_id WHERE u.username = %s AND p.arquivo = %s AND p.acao = %s", (username, file, action))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


# principal
def main():
    conn = conexao()
    while True:
        transicao()
        print("Bem-vindo ao sistema de controle de acesso da nossa equipe!")
        print("Escolha uma opção")
        print("[1] Registrar usuário")
        print("[2] Registrar permissão")
        print("[3] Autenticar e acessar")
        print("[4] Sair")

        choice = input("Qual é a sua opção: ")
        transicao()
        if choice == '1':
            transicao()
            usr = input("Nome de usuário: ")
            pwd = getpass("Senha: ")
            registrar_usuario(conn, usr, pwd)
            print("Usuário cadastrado com sucesso!")
            dormir()
            transicao()
        elif choice == '2':
            transicao()
            usrID = input("nome do usuário: ")
            nomeArquivo = input("Digite o nome do arquivo: ")

            print("Que ação deseja fazer: ")
            print("[1] ler")
            print("[2] escrever")
            print("[3] executar")
            acao = int(input("Qual é a sua escolha: "))
            action = ""
            if acao == 1:
                action = "ler"
            elif acao == 2:
                action = "escrever"
            elif acao == 3:
                action = "executar"
            nomeAcao = action
            registrar_permissao(conn, usrID, nomeArquivo, nomeAcao)
            dormir()
            transicao()
        elif choice == '3':
            transicao()
            usr = input("Nome de usuário: ")
            pwd = getpass("Senha: ")
            if autenticar_usuario(conn, usr, pwd):
                file = input("Qual arquivo deseja selecionar: ")
                print("Que ação deseja fazer: ")
                print("[1] ler")
                print("[2] escrever")
                print("[3] executar")
                acao = int(input("Qual é a sua escolha: "))
                action = ""
                if acao == 1:
                    action = "ler"
                elif acao == 2:
                    action = "escrever"
                elif acao == 3:
                    action = "executar"
                if checar_permissao(conn, usr, action, file):
                    print("Acesso permitido")
                    dormir()
                    transicao()
                else:
                    print("Acesso negado")
                    dormir()
                    transicao()
        elif choice == '4':
            transicao()
            break
    conn.close()



main()
