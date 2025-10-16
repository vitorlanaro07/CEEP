#pip install mysql-connector-python
#instala o conector do Python com o Banco de dados

import mysql.connector #faz a importação do módulo baixado
from datetime import datetime #importa módulo responsável por fazer conversões no fomato da data exemplo: AAAA/MM/DD para -> DD/MM/AAAA

conexao = mysql.connector.connect( # Conecta com o Banco de dados, a conexão será feita e está sendo refernciada pela variável "conexao"
    host="localhost",       # ou o IP do servidor
    user="root",            # seu usuário do MySQL
    password="354555",   # senha do seu MySQL
    database="aula"  # nome do banco que deseja usar
)


seletor = "" #declara seletor do menu

while seletor != 0: #enquanto o seletor for diferente de 0, fique aqui -> 
    print("1 - Cadastrar aluno")
    print("2 - Consultar aluno")
    print("3 - Listar todos os alunos")
    print("0 - Sair")

    seletor = int(input("Selecione uma opção:"))

    if(seletor == 1):
        
        # Criar um cursor. Esse "Cursor" permite executar comandos SQL.
        cursor = conexao.cursor();

        #Permitimos ao usuário a escrita dos dados 
        print("\n-----Cadastro Aluno-----")
        nome = input("Qual o nome do aluno: ")
        sobrenome = input("Qual o sobrenome do aluno:")
        data_nascimento = input("Qual a data de nascimento do aluno (DD/MM/AAAA): ")
        
        # Converter a data para o formato correto (DD/MM/AAAA) para (AAAA-MM-DD) 
        data_nascimento_mysql = datetime.strptime(data_nascimento, "%d/%m/%Y").strftime("%Y-%m-%d")

        #comando para ser executado no SQL: inserindo o aluno criado no DB
        sql = "INSERT INTO aluno (nome_aluno, sobrenome_aluno, data_nascimento) VALUES (%s, %s, %s)"
        
        #valores a serem substituídos aos declaros acima como "(%s, %s, %s)"
        valores = (nome, sobrenome, data_nascimento_mysql)

        #o cursos executa o código SQL com os valores armazenados nas váriaveis: nome, sobrenome, data_nascimento_mysql
        cursor.execute (sql, valores)
        
        #efetua o Commit e os dados são enviados ao banco de dados.
        conexao.commit();


        # # Pegar o id gerado automaticamente
        # id_aluno = cursor.lastrowid

        # print("----------------------------------------------")
        # print("Cadastro Endereço:")
        # rua = input("Qual a rua: ")
        # num = input("Qual o numero: ")
        # cidade = input("Qual a Cidade: ")
        # uf = input("Qual o UF: ")

        # sql = "INSERT INTO endereco_aluno (id_aluno, rua, numero, cidade, uf) VALUES (%s ,%s, %s, %s, %s)"
        # valores = (id_aluno, rua, num, cidade, uf)
        # cursor.execute (sql, valores)
        
        # conexao.commit();


        # print("----------------------------------------------")
        # print("Cadastro contato:")
        # telefone = input("Qual o telefone: ")
        # email = input("Qual o email: ")

        # sql = "INSERT INTO contato_aluno (id_aluno, telefone, email) VALUES (%s, %s, %s)"
        # valores = (id_aluno, telefone, email)
        # cursor.execute (sql, valores)
        # conexao.commit();

        print("\nAluno cadastrado com sucesso!\n")
        cursor.close()# Uma boa prática, fecha o cursor após ser usado. Abriu a porta, agora fecha!

    elif seletor == 2:
        #Criar um cursor. Esse "Cursor" permite executar comandos SQL.
        cursor = conexao.cursor();

        busca = input("\nInforme o nome do aluno que deseja consultar: ")
        
        sql = 'SELECT id_aluno, nome_aluno, sobrenome_aluno, data_nascimento FROM aluno WHERE nome_aluno LIKE %s;'

        cursor.execute(sql, (busca,)) #importante a virgula, pois o sql reconhece como uma lista, um array...
        resultado = cursor.fetchall()
        print(resultado);
        if resultado:
            print("\n-----Resultado da Busca-----")
            print(f"ID: {resultado[0][0]}")
            print(f"Nome: {resultado[0][1]} {resultado[0][2]}")
            print(f"Data de nascimento: {resultado[0][3]}")
            print("-" * 40 + "\n")
        else:
            print("\nNenhum aluno encontrado!\n")
        
        cursor.close()
    elif seletor == 3:
        cursor = conexao.cursor();
        sql = 'SELECT * FROM aluno;'

        cursor.execute(sql)
        resultado = cursor.fetchall()

        if resultado:
            contador = 0
            while contador < len(resultado):
                print("\n-----Resultado da Busca-----")
                print(f"ID: {resultado[contador][0]}")
                print(f"Nome: {resultado[contador][1]} {resultado[contador][2]}")
                print(f"Data de nascimento: {resultado[contador][3]}")
                print("-" * 40 + "\n")
                contador +=1
        else:
            print("\nNenhum aluno encontrado!\n")

    elif seletor == 0:
        # Fechar a conexão (boa prática)
        conexao.close()


        



