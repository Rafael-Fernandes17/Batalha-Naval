import random
import time
import emoji
from termcolor import colored
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
            print(colored("❌ Opção inválida", "red" , attrs=['bold']))
            linha = int(input(colored("Indique a LINHA onde você deseja inserir uma embarcação: ", "cyan")))

#Verificação para saber se o valor inserido  na coluna é inválido           
def coluna_invalida(coluna):
     while coluna != 1 and coluna != 2 and coluna != 3 and coluna != 4 and coluna != 5 and coluna != 6 and coluna != 7 and coluna != 8 and coluna != 9 and coluna != 10:
            print(colored("❌ Opção inválida", "red" , attrs=['bold']))
            coluna = int(input(colored("Indique a COLUNA onde você deseja inserir uma embarcação: ", "blue")))

#Printa qualquer matriz que for adicionada como parametro          
def exibe_matriz(matriz_desejada, ocultar_navios=False):
    print('   ', end='')
    for i in range(1, 11):
        print(f'{i:2}', end=' ')
    print()

    for i, linha in enumerate(matriz_desejada):
        print(f'{i + 1:2} ', end=' ')
        for celula in linha:
            if celula == 0:
                simbolo = emoji.emojize('🟦')
                simbolo_colorido = colored(simbolo, 'cyan')
            elif celula == 1 and ocultar_navios:
                simbolo = emoji.emojize('🟦')
                simbolo_colorido = colored(simbolo, 'cyan')
            elif celula == 1 and not ocultar_navios:
                simbolo = emoji.emojize('🚢')
                simbolo_colorido = colored(simbolo, 'green')
            elif celula == 'x':
                if matriz_desejada == tabuleiro_vazio1 and tabuleiro_player[i][linha.index(celula)] == 1:
                    simbolo = emoji.emojize('💥')
                    simbolo_colorido = colored(simbolo, 'red')
                elif matriz_desejada == tabuleiro_vazio2 and tabuleiro_computador[i][linha.index(celula)] == 1:
                    simbolo = emoji.emojize('💥')
                    simbolo_colorido = colored(simbolo, 'red')
                else:
                    simbolo = emoji.emojize('💦')
                    simbolo_colorido = colored(simbolo, 'blue')
            print(simbolo_colorido, end=' ')
        print()
                
                
#iniciando o jogo
print(colored("Bem vindo ao jogo de Batalha Naval!!!!", "green" , attrs=["dark", "bold"]))
print(colored("Jogadores organizem suas frotas.", "green" , attrs=["dark", "bold"]))

#Fazendo o player adicionar 5 embarcacoes
while embarcacoes_player1 < 5:
    
    #pedindo a linha que será adicionada uma embarcação
    linha = int(input(colored("\nIndique a LINHA onde você deseja inserir uma embarcação: ", "cyan")))
    linha_invalida(linha)
    
    #pedindo a coluna que será adicionada uma embarcação
    coluna = int(input(colored("Indique a COLUNA onde você deseja inserir uma embarcação: ", "blue")))
    coluna_invalida(coluna)
    
    #Enquanto ele adicionar uma embarcação em um lugar que já possui embarcação ele vai pedir para tentar de novo
    while True:
        if tabuleiro_player[linha - 1][coluna - 1] == 1:
            print(colored("VOCÊ JÁ POSSUI UMA EMBARCAÇAO NESSA POSIÇÃO. DIGITE NOVAMENTE", "red", attrs=["bold"]))
            linha = int(input(colored("\nIndique a LINHA onde você deseja inserir uma embarcação: ", "cyan")))
            linha_invalida(linha)
            
            coluna = int(input(colored("Indique a COLUNA onde você deseja inserir uma embarcação: ", "blue")))
            coluna_invalida(coluna)
            
        #Se não, ele vai definir o número de embarcações e o tabuleiro atual
        else:
            embarcacoes_player1 += 1
            tabuleiro_player[linha - 1][coluna - 1] = 1
            print()
            break 
        
    #apenas fazendo uma verificação para exibir o tabuleiro do player e escrever o plural ou o singular dependendo da quantidade de embarcações 
    if embarcacoes_player1 == 1:
        print(colored("Você possui {} embarcação e seu tabuleiro atual é: ".format(embarcacoes_player1), "cyan", attrs=["dark"]))
        exibe_matriz(tabuleiro_player)
        
    else:
        print(colored("Você possui {} embarcações e seu tabuleiro atual é: ".format(embarcacoes_player1), "cyan", attrs=["dark"]))
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
        print(colored("🤖 O COMPUTADOR possui {} embarcação.".format(embarcacoes_computador), "magenta"))
    else:
        print(colored("🤖 O COMPUTADOR possui {} embarcações.".format(embarcacoes_computador), "magenta"))
    time.sleep(1.5)
    
#comecando a guerra
#Player atirando
print(colored("\nA GUERRA COMEÇOU!!!!!!!!!!!!!!!!!!!!!", "green", attrs=["dark","bold"]))
print()
enter = input(colored("Pressione ENTER", "yellow"))

while embarcacoes_player1 != 0 and embarcacoes_computador != 0:
    print(colored("\n🧑 Player 1 - Esse é o seu tabuleiro:" , "blue"))
    exibe_matriz(tabuleiro_vazio1)
    print(colored("Você possui {} embarcações.".format(embarcacoes_player1), "magenta"))
    time.sleep(3)
    print(colored("\nTabuleiro do 🤖 computador: ", "red"))
    exibe_matriz(tabuleiro_computador)
    print(colored("O 🤖 computador possui {} embarcações.".format(embarcacoes_computador), "magenta"))
    enter = input(colored("Pressione ENTER", "yellow"))
    
    print(colored("\n🧑 PLAYER 1 ATIREEEEE!!!!", "blue"))
    jogador_quer_acertar_linha = int(input(colored("🧑 Player 1 - Escreva a LINHA de cordenada onde você quer atirar: ", "grey")))
    linha_invalida(jogador_quer_acertar_linha)

    jogador_quer_acertar_coluna = int(input(colored("🧑 Player 1 - Escreva a  COLUNA de cordenada onde você quer atirar: ", "grey")))
    coluna_invalida(jogador_quer_acertar_coluna)

    #Se não derrubou nenhuma embarcação do computador ele faz isso
    if tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 0:
        print(colored("\nVocê não derrubou nenhuma embarcação! 😞", "red"))
        print(colored("O 🤖 computador possui {} embarcações".format(embarcacoes_computador), "magenta"))
        tabuleiro_vazio2[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        print()
    
    #se derrubou ele faz isso  
    elif tabuleiro_computador[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] == 1:
        embarcacoes_computador -= 1
        print(colored("\nVocê derrubou uma embarcação do computador!!! 😎​", "green"))
        print(colored("O computador possui {} embarcações".format(embarcacoes_computador), "magenta"))
        tabuleiro_vazio2[jogador_quer_acertar_linha - 1][jogador_quer_acertar_coluna - 1] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        print()
        
        
    #Computador atirando
    linha_atira = random.randint(0,4)
    coluna_atira = random.randint(0,9)
    
    while tabuleiro_vazio1[linha_atira][coluna_atira] == "x":
        linha_atira = random.randint(1,5)
        coluna_atira = random.randint(1,10)
        

    print(colored("O 🤖 COMPUTADOR ESTÁ ATIRANDOOOOO!!!!!", "red"))
    print(colored(f"O 🤖 computador vai atirar na LINHA: {linha_atira + 1}", "grey"))
    enter = input(colored("Pressione ENTER", "yellow"))

    print(colored(f"O 🤖 computador quer atirar na COLUNA: {coluna_atira + 1}", "grey"))
    enter = input(colored("Pressione ENTER", "yellow"))

    #Se o computador não derrubou nenhuma embarcação sua o bloco executado é:
    if tabuleiro_player[linha_atira][coluna_atira] == 0:
        print(colored("\nO 🤖 computador NÃO acertou sua embarcação!", "red"))
        time.sleep(1)
        print(colored("\nVocê possui {} embarcações!".format(embarcacoes_player1), "blue"))
        tabuleiro_vazio1[linha_atira][coluna_atira] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        
    #Se ele derrubou o bloco executado é:   
    elif tabuleiro_player[linha_atira][coluna_atira] == 1:
        embarcacoes_player1 -= 1
        print(colored("\nO 🤖 computador derrubou uma embarcação sua!", "white", attrs=["dark"]))
        time.sleep(1)
        print(colored("\nVocê possui {} embarcações!".format(embarcacoes_player1), "blue"))
        tabuleiro_vazio1[linha_atira - 1][coluna_atira - 1] = "x"
        enter = input(colored("Pressione ENTER", "yellow"))
        
    if embarcacoes_computador == 0:
        print(colored("\nO 🧑 JOGADOR AFUNDOU A FROTA DO 🤖 COMPUTADOR!!!!!!", "green", attrs=["bold"]))
        print(colored("TEMOS UM NOVO CAPITÃO DOS MARES 🌊", "blue", attrs=["bold"]))
        print(colored("O 🤖 COMPUTADOR VENCEUUUUU ​🏆​​", "red", attrs=["bold"]))
        print(colored("\nPLACAR FINAL: ", "yellow", attrs=["bold"]))
        print(colored("Embarcações do 🧑 Player: {}.Embarcações do 🤖 Computador {}.".format(embarcacoes_player1, embarcacoes_computador), "cyan", attrs=["bold"]))
        
    elif embarcacoes_player1 == 0:
        print(colored("\nO 🤖 COMPUTADOR AFUNDOU A FROTA DO 🧑 JOGADOR!!!!!!", "green", attrs=["bold"]))
        print(colored("TEMOS UM NOVO CAPITÃO DOS MARES 🌊", "blue", attrs=["dark", "bold"]))
        print(colored("O 🧑 JOGADOR VENCEUUUUU 🏆", "blue", attrs=["bold"]))
        print(colored("\nPLACAR FINAL: ", "yellow", attrs=["bold"]))
        print(colored("Embarcações do 🧑 Player: {}.Embarcações do 🤖 Computador {}.".format(embarcacoes_player1, embarcacoes_computador), "cyan", attrs=["bold"]))
        
    elif embarcacoes_player1 == 0 and embarcacao_computador == 0:
        print(colored("\nESSA GUERRA FOI SANGRENTA, NINGUÉM SOBREVIVEU", "grey", attrs=["bold"]))
        