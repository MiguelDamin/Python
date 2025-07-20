"""10. Simulador de Loja Virtual no Terminal
O projeto mais completo: exibe produtos, permite adicionar ao carrinho e finalizar a compra. Tudo
no terminal, simulando um e-commerce. Trabalha organização de dados, lógica condicional e
menus encadeados."""
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint
from rich.text import Text
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Miguel11!",
    database="lojavirtual"
)

def desenhar_cabecalho(texto_do_titulo):
    """Limpa a tela e desenha um cabeçalho estilizado."""
    limpar_tela() 
    
    # Gera o texto em ASCII Art
    titulo_ascii = pyfiglet.figlet_format(texto_do_titulo, font="slant")
    
    # Imprime o título em verde e dentro de um painel
    console.print(Panel.fit(f"[green]{titulo_ascii}[/]", subtitle="[Miguel]"))
    console.print() # Imprime uma linha em branco para dar espaço


cursor = conexao.cursor() 
cursor.execute("SELECT * FROM produtos")
resultados = cursor.fetchall()
for linha in resultados:
     print(f"{linha[0]} - {linha[1]} - R${linha[2]}")

cursor.execute("SELECT id_produto FROM produtos")
idsDisponiveis = [linha[0] for linha in cursor.fetchall()]  #Essa linha de cod, pega todos os ids do banco, e coloca numa lista na variavel idsDisponiveis

produto = int(input("Escolha o poduto de acordo com ID ou feche clicando ENTER: "))
if produto in idsDisponiveis:
   print("Produto Adicionado ao carrinho")
   continuar = input("Você está quase lá, deseja continuar a compra(s/n)? ")
   if continuar == "s":
       cursor.execute('INSERT INTO vendas(id_produto) values(%s)', (produto,))
       conexao.commit()
       print("COMPRA REALIZADA COM SUCESSO")
   else:
       print("Compra Cancelada")
else:
    print("PRODUTO NÃO EXISTE")

       
       
            
    


    

