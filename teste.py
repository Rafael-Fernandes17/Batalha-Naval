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
def linha_invalida(linha):
     while linha != 1 and linha != 2 and linha != 3 and linha != 4 and linha != 5:
            print("Opção inválida")
            linha = int(input("Indique a LINHA onde você deseja inserir uma embarcação: "))
            
def coluna_invalida(coluna):
     while coluna != 1 and coluna != 2 and coluna != 3 and coluna != 4 and coluna != 5:
            print("Opção inválida")
            coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
            
def exibe_matriz(matriz_desejada):
    for linha in range(len(matriz_desejada)):
                print(matriz_desejada[linha])
                
                
#iniciando o jogo
print("Bem vindo ao jogo de Batalha Naval!!!!")
print("Jogadores organizem suas frotas.\n")

#Fazendo o player adicionar 5 embarcacoes
for embarcacao in range(0, 5):
    
        #pedindo a linha que será adicionada uma embarcação
        linha = int(input("\nIndique a LINHA onde você deseja inserir uma embarcação: "))
        #Verificação para saber se o valor inserido é inválido
        linha_invalida(linha)
        
        #pedindo a coluna que será adicionada uma embarcação
        coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
        #Verificação para saber se o valor inserido é inválido
        coluna_invalida(coluna)
        
        #adicionando uma embarcação (número 1) nas cordenadas inseridas    
        tabuleiro_player[linha - 1][coluna - 1] = 1
        print()
        
        #definindo a quantidade de embarcacoes do player
        for linha in range (0,5):
            for coluna in range(0,10):
                if tabuleiro_player[linha][coluna] == 1:
                    embarcacoes_player1 += 1
        
        #apenas fazendo uma verificação para exibir o tabuleiro do player e escrever o plural ou o singular dependendo da quantidade de embarcações 
        if embarcacoes_player1 == 1:
            print("Você possui {} embarcação e seu tabuleiro atual é: ".format(embarcacoes_player1))
            exibe_matriz(tabuleiro_player)
            embarcacoes_player1 = 0
            
        else:
            print("Você possui {} embarcações e seu tabuleiro atual é: ".format(embarcacoes_player1))
            exibe_matriz(tabuleiro_player)
            embarcacoes_player1 = 0

print()

#Definindo o tabuleiro do computador
for embarcacao_computador in range(0,5):
     tabuleiro_computador[random.randint(0,4)][random.randint(0,9)] = 1
     embarcacoes_computador += 1

#printando o tabuleiro do computador
     if embarcacoes_computador == 1:
          print("Você possui {} embarcação e seu tabuleiro atual é: ".format(embarcacoes_computador))
          exibe_matriz(tabuleiro_computador)
               
     else:
          print("Você possui {} embarcações e seu tabuleiro atual é: ".format(embarcacoes_computador))
          exibe_matriz(tabuleiro_computador)
          
     time.sleep(1.5)
    
#comecando a guerra
#Player atirando
print("A GUERRA COMEÇOU!!!!!!!!!!!!!!!!!!!!!")
print()

jogador_quer_acertar_linha = int(input("\nPlayer 1 - Escreva a LINHA de cordenada onde você quer atirar: "))
linha_invalida(jogador_quer_acertar_linha)

jogador_quer_acertar_coluna = int(input("Player 1 - Escreva a  COLUNA de cordenada onde você quer atirar: "))
coluna_invalida(jogador_quer_acertar_coluna)

if tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 0:
    print("\nVocê não derrubou nenhuma embarcação!")
    exibe_matriz(tabuleiro_computador)
    
elif tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 1:
    print("\nVocê derrubou uma embracação do computador!!!!")
    tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] = 0
    exibe_matriz(tabuleiro_computador)
