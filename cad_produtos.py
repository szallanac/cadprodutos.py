import os
opcao = 0

 
while (opcao != 3):
    print("------ MENU de produtos -----")
    print("1 - para cadastrar")
    print("2 - para listar")
    print("3 - para excluir produto:")
    print("4 - para sair")
 
    opcao = int(input("escolha a opção: "))
    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        codigo = input("Digite o codigo do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
    
        arquivo = open("cade_pessoas.txt", "a")
        arquivo.write(f"{nome},{codigo},{preco},{quantidade}\n")
        arquivo.close()
        print("cadastrar o produto")
        
 
 
        arquivo = open("cade_produtos.txt", "a")
        arquivo.write(f"{nome},{codigo},{preco},{quantidade}\n")
        arquivo.close()

            
        print("cadastrar o produto")
        print("Produto cadastrado com sucesso")
        input()
        os.system("cls")
    elif (opcao == 2):
        print("-----LISTA DE PRODUTOS------")
        
        
        arquivo = open("cade_produtos.txt", "r")

        for linha in arquivo:
                 nome, codigo, preco, quantidade = linha.strip().split(",")
        print(f"nome da produto:\t {nome}")
        print(f"codigo do produto:\t {codigo}")
       
        print(f"preço do produto:\t {preco}")
        print(f"A quantidade desse produto:\t {quantidade}")
    
        print("------------------------------")
        input()
        os.system("cls")

    elif opcao == 3:
     arquivo = open("produtos.txt", "r") # abertura do arquivo para leitura
linhas = arquivo.readlines() # leitura das linhas a armazenamento em uma lista
arquivo.close() #fechei o arquivo produtos.txt

remover = int(input("digite a linha que deseja remover: "))
remover = remover - 1
linhas.pop(remover)

arquivo = open("produtos.txt", "w")
for linha in linhas:
     arquivo.write(linhas)
     arquivo.close()

     print("produto removido com sucesso!")
     input()
     os.system("cls")
 