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

print("Bem vindo ao jogo de Batalha Naval!!!!")
for embarcacao in range(0, 5):
        linha_player1 = int(input("\nIndique a LINHA onde você deseja inserir uma embarcação: "))
        while linha_player1 != 1 and linha_player1 != 2 and linha_player1 != 3 and linha_player1 != 4 and linha_player1 != 5:
            print("Opção inválida")
            linha_player1 = int(input("Indique a LINHA onde você deseja inserir uma embarcação: "))

        coluna_player1 = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
        while coluna_player1 != 1 and coluna_player1 != 2 and coluna_player1 != 3 and coluna_player1 != 4 and coluna_player1 != 5 and coluna_player1 != 6 and coluna_player1 != 7 and coluna_player1 != 8 and coluna_player1 != 9 and coluna_player1 != 10:
            print("Opção inválida\n")
            coluna_player1 = int(input("Indique a COLUNA onde você deseja inserir uma embarcação: "))
            
        tabuleiro_player[linha_player1 - 1][coluna_player1 - 1] = 1
        print()
        print("Seu tabuleiro atual é: ")
        for linha in range(0, 5):
            print(tabuleiro_player[linha])
    
