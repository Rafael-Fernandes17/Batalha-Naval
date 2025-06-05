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
     while coluna != 1 and coluna != 2 and coluna != 3 and coluna != 4 and coluna != 5 and coluna != 6 and coluna != 7 and coluna != 8 and coluna != 9 and coluna != 10:
            print("Opção inválida")
            coluna = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))

#Printa qualquer matriz que for adicionada como parametro          
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


#Definindo o tabuleiro do computador
for embarcacao_computador in range(0,5):
    
    #Definindo a linha e coluna onde serão adicionadas as embarcações do computador
    linha_computador = random.randint(0,4)
    coluna_computador = random.randint(0,9)
    
    #Enquanto a cordenada já possuir uma embarcação ele vai sortear de novo
    while tabuleiro_computador[linha_computador][coluna_computador] == 1:
        linha_computador = random.randint(0,4)
        coluna_computador = random.randint(0,9)
        
    #Depois de já conferir ele define onde a embarcação vai ficar e soma +1 ao número de embarcações
    tabuleiro_computador[linha_computador][coluna_computador] = 1
    embarcacoes_computador += 1

    #printando a quantidade de embarcações do computador
    if embarcacoes_computador == 1:
        print("O COMPUTADOR possui {} embarcação.".format(embarcacoes_computador))            
    else:
        print("O COMPUTADOR possui {} embarcações.".format(embarcacoes_computador))
    time.sleep(1.5)
    
#comecando a guerra
#Player atirando
print("\nA GUERRA COMEÇOU!!!!!!!!!!!!!!!!!!!!!")
print()
enter = input("Pressione ENTER")

while embarcacoes_player1 != 0 and embarcacoes_computador != 0:
    print("\nPlayer 1 - Esse é o seu tabuleiro:" )
    exibe_matriz(tabuleiro_vazio1)
    print("Você possui {} embarcações.".format(embarcacoes_player1))
    time.sleep(3)
    print("\nTabuleiro do computador: ")
    exibe_matriz(tabuleiro_computador)
    print("O computador possui {} embarcações.".format(embarcacoes_computador))
    enter = input("Pressione ENTER")
    
    print("\nPLAYER 1 ATIREEEEE!!!!")
    jogador_quer_acertar_linha = int(input("Player 1 - Escreva a LINHA de cordenada onde você quer atirar: "))
    linha_invalida(jogador_quer_acertar_linha)

    jogador_quer_acertar_coluna = int(input("Player 1 - Escreva a  COLUNA de cordenada onde você quer atirar: "))
    coluna_invalida(jogador_quer_acertar_coluna)

    #Se não derrubou nenhuma embarcação do computador ele faz isso
    if tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 0:
        print("\nVocê não derrubou nenhuma embarcação!")
        print("O computador possui {} embarcações".format(embarcacoes_computador))
        tabuleiro_vazio2[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] = "x"
        enter = input("Pressione ENTER")
        print()
    
    #se derrubou ele faz isso  
    elif tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 1:
        embarcacoes_computador -= 1
        print("\nVocê derrubou uma embarcação do computador!!!!")
        print("O computador possui {} embarcações".format(embarcacoes_computador))
        tabuleiro_vazio2[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] = "x"
        enter = input("Pressione ENTER")
        print()
        
        
    #Computador atirando
    linha_atira = random.randint(0,4)
    coluna_atira = random.randint(0,9)

    print("O COMPUTADOR ESTÁ ATIRANDOOOOO!!!!!")
    print("O computador vai atirar na LINHA: ", linha_atira)
    enter = input("Pressione ENTER")

    print("O computador quer atirar na COLUNA: ", coluna_atira)
    enter = input("Pressione ENTER")

    #Se o computador não derrubou nenhuma embarcação sua o bloco executado é:
    if tabuleiro_player[linha_atira][coluna_atira] == 0:
        print("\nO computador NÃO acertou sua embarcação!")
        time.sleep(1)
        print("\nVocê possui {} embarcações!".format(embarcacoes_player1))
        tabuleiro_vazio1[linha_atira][coluna_atira] = "x"
        enter = input("Pressione ENTER")
        
    #Se ele derrubou o bloco executado é:   
    elif tabuleiro_player[linha_atira][coluna_atira] == 1:
        embarcacoes_player1 -= 1
        print("\nO computador derrubou uma embarcação sua!")
        time.sleep(1)
        print("\nVocê possui {} embarcações!".format(embarcacoes_player1))
        tabuleiro_vazio1[linha_atira][coluna_atira] = "x"
        enter = input("Pressione ENTER")
        
    if embarcacoes_computador == 0:
        print("\nO JOGADOR AFUNDOU A FROTA DO COMPUTADOR!!!!!!")
        print("TEMOS UM NOVO CAPITÃO DOS MARES!!!")
        print("O JOGADOR VENCEUUUUU!!!!!!")
        print("\nPLACAR FINAL: ")
        print("Embarcações do Player: {}. Embarcações do Computador {}.".format(embarcacoes_player1, embarcacoes_computador))
        
    elif embarcacoes_player1 == 0:
        print("\nO JOGADOR AFUNDOU A FROTA DO COMPUTADOR!!!!!!")
        print("TEMOS UM NOVO CAPITÃO DOS MARES!!!")
        print("O JOGADOR VENCEUUUUU!!!!!!")
        print("\nPLACAR FINAL: ")
        print("Embarcações do Player: {}. Embarcações do Computador {}.".format(embarcacoes_player1, embarcacoes_computador))
        
    elif embarcacoes_player1 == 0 and embarcacao_computador == 0:
        print("\nESSA GUERRA FOI SANGRENTA, NINGUÉM SOBREVIVEU")
        