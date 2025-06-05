import random
import time
#Criando tabuleiros
tabuleiro_vazio1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_vazio2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_computador = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tabuleiro_player = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#criando variável de embarcações do player
embarcacoes_player1 = 0
embarcacoes_computador = 0

#Criando as Def's

#Verificação para saber se o valor inserido na linha é inválido
def linha_invalida(linha):
     while linha != 1 and linha != 2 and linha != 3 and linha != 4 and linha != 5:
            print("Opção inválida")
            linha = int(input("Indique a LINHA onde você deseja inserir uma embarcação: "))

#Verificação para saber se o valor inserido  na coluna é inválido           
def coluna_invalida(coluna):
     while coluna != 1 and coluna != 2 and coluna != 3 and coluna != 4 and coluna != 5 and coluna != 7 and coluna != 8 and coluna != 9 and coluna != 10:
            print("Opção inválida")
            coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
            
def exibe_matriz(matriz_desejada):
    for linha in range(len(matriz_desejada)):
                print(matriz_desejada[linha])
                
                
#iniciando o jogo
print("Bem vindo ao jogo de Batalha Naval!!!!")
print("Jogadores organizem suas frotas.")

#Fazendo o player adicionar 5 embarcacoes
while embarcacoes_player1 < 5:
    
    #pedindo a linha que será adicionada uma embarcação
    linha = int(input("\nIndique a LINHA onde você deseja inserir uma embarcação: "))
    linha_invalida(linha)
    
    #pedindo a coluna que será adicionada uma embarcação
    coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
    coluna_invalida(coluna)
    
    #Enquanto ele adicionar uma embarcação em um lugar que já possui embarcação ele vai pedir para tentar de novo
    while True:
        if tabuleiro_player[linha - 1][coluna - 1] == 1:
            print("VOCÊ JÁ POSSUI UMA EMBARCAÇAO NESSA POSIÇÃO. DIGITE NOVAMENTE")
            linha = int(input("\nIndique a LINHA onde você deseja inserir uma embarcação: "))
            linha_invalida(linha)
            
            coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
            coluna_invalida(coluna)
            
        #Se não, ele vai definir o número de embarcações e o tabuleiro atual
        else:
            embarcacoes_player1 += 1
            tabuleiro_player[linha - 1][coluna - 1] = 1
            print()
            break 
        
    #apenas fazendo uma verificação para exibir o tabuleiro do player e escrever o plural ou o singular dependendo da quantidade de embarcações 
    if embarcacoes_player1 == 1:
        print("Você possui {} embarcação e seu tabuleiro atual é: ".format(embarcacoes_player1))
        exibe_matriz(tabuleiro_player)
        
    else:
        print("Você possui {} embarcações e seu tabuleiro atual é: ".format(embarcacoes_player1))
        exibe_matriz(tabuleiro_player)
    time.sleep(1)

print()
