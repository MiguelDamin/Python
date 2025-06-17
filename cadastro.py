clientes= []


while True:
  
 nome = input("Cadastre um novo cliente ou clique enter para procurar existentes: ").strip().lower()
#strip() para deixar todos os caracteres juntos e lower() para mesmo se for minusculo maiusculo alienigena, vai reconhecer no vetor
 
 if nome == "":
   cliente_busca= input("Busque seu cliente: ").strip().lower()
   if cliente_busca in clientes:
     print("Esse cliente existe")
   else:
       print("Não existe esse cliente no nosso sistema")
 else:
     clientes.append(nome) #vai colocar o nome registrado dentro do vetor do python
     print(f"O cliente {nome} foi cadastrado ")
 sair = input("Você quer parar a busca e os cadastros? (s/n)").strip().lower()
 if sair == "s":
    break
  
     
  