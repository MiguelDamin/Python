import pyfiglet
from rich.console import Console
from tabulate import tabulate
from colorama import init, Fore, Style
init(autoreset=True)
import mysql.connector

conexao = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Miguel11!",
      database="Cadastro"
  )

cursor = conexao.cursor()
escolha = int(input(Fore.GREEN + "--------------> 1-CADASTRAR NOVOS CLIENTES, 2-LISTAR, 3-REMOVER <-------------- \n" + Fore.WHITE + "Selecione a Opção: "))

if escolha == 1:
    nomePesquisado = input("NOME DO COMPLETO DO CLIENTE: ")
    cursor.execute("INSERT INTO clientes(nome) VALUES(%s)", (nomePesquisado,)) #Insere um novo Usuário ao Banco
    conexao.commit() #Manda de Fato a Informação pro Banco
elif escolha == 2:
    tipoDeSelect = int(input("____________________________________1-LISTAR CLIENTE ESPECÍFICO, 2-LISTAR TODOS____________________________________________ \n Selecione a Opção: "))
    if tipoDeSelect == 1:
        idPesquisa = int(input("DIGITE O ID DO CLIENTE: "))
        cursor.execute("SELECT nome FROM clientes WHERE id_cliente = %s", (idPesquisa,)) #Usei o %s para evitar SQL Injection
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
    elif tipoDeSelect == 2:
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
elif escolha == 3:
    idPesquisa = int(input("DIGITE O ID DO CLIENTE NO QUAL VOCÊ DESEJA REMOVER: "))
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (idPesquisa,))
    conexao.commit()


    
# Fechar conexão
cursor.close()
conexao.close()



