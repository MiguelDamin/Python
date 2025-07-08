"""10. Simulador de Loja Virtual no Terminal
O projeto mais completo: exibe produtos, permite adicionar ao carrinho e finalizar a compra. Tudo
no terminal, simulando um e-commerce. Trabalha organização de dados, lógica condicional e
menus encadeados."""
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
    database="lojavirtual"
)


##console = Console()
print(pyfiglet.figlet_format("Lojinha do Ze"))
##console.rule("[bold magenta]MINHA LOJA[/bold magenta]")


cursor = conexao.cursor() 
cursor.execute("SELECT * FROM produtos")
resultados = cursor.fetchall()
for linha in resultados:
    headers = [
    f"{Fore.GREEN}ID{Style.RESET_ALL}",
    f"{Fore.MAGENTA}Nome{Style.RESET_ALL}",
    f"{Fore.CYAN}Preço (R$){Style.RESET_ALL}"
]
    print(tabulate([linha], headers=headers, tablefmt="fancy_grid"))


cursor.execute("SELECT id_produto FROM produtos")
idsDisponiveis = [linha[0] for linha in cursor.fetchall()]  #Essa linha de cod, pega todos os ids do banco, e coloca numa lista na variavel idsDisponiveis

produto = int(input("Escolha o poduto de acordo com ID ou feche clicando ENTER: "))
if produto in idsDisponiveis:
   print("Produto Adicionado ao carrinho")
   continuar = input("Você está quase lá, deseja continuar a compra(s/n)? ")
   if continuar == "s":
       cursor.execute('INSERT INTO vendas(id_produto) values(%s)', (produto,))
       conexao.commit()
       print(Fore.GREEN + "COMPRA REALIZADA COM SUCESSO")
   else:
       print(Fore.RED + "COMPRA CANCELADO")
else:
    print(Fore.YELLOW + "PRODUTO NÃO EXISTE")

       
       
            
    


    

