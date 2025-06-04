import random

while True:
        # Menu onde o usuário pode escolher entre jogar ou sair.
        # Usei o \033["numero da cor" "texto" \033[0m para mudar a cor do texto. e para fazer as bordas usei os +, o - para o meio e | para as laterais.
        print("\033[1;34m+" + "-" * 38 + "+\033[0m")
        print("\033[1;34m|\033[0m     \033[1;31m*** BEM VINDO AO JOKEMPO ***\033[0m     \033[1;34m|\033[0m")
        print("\033[1;34m|" + " " * 38 + "|\033[0m")
        print("\033[1;34m|\033[0m   \033[1;34mEscolha um modo de jogar:\033[0m          \033[1;34m|\033[0m")
        print("\033[1;34m|" + " " * 38 + "|\033[0m")
        print("\033[1;34m|\033[0m   \033[36m1. Player vs Player\033[0m                \033[1;34m|\033[0m")
        print("\033[1;34m|\033[0m   \033[36m2. Player vs Computador\033[0m            \033[1;34m|\033[0m")
        print("\033[1;34m|\033[0m   \033[36m3. Computador vs Computador\033[0m        \033[1;34m|\033[0m")
        print("\033[1;34m|\033[0m   \033[36m4. Sair do jogo\033[0m                    \033[1;34m|\033[0m")
        print("\033[1;34m+" + "-" * 38 + "+\033[0m")
        
        modo = input("\033[1;37mResposta:\033[0m ")
        if modo == "1" or modo == "2" or modo == "3" or modo == "4": # esse serve para caso a pessoa escoha uma opção nao valida ele tente novamente.
                
                pontos_player1 = 0 # contador para o jogador 1
                pontos_player2 = 0 # contador para o jogador 2
                
                if modo == "1": # caso a pessoa escoha o modo 1 iniciara o jogo com dois jogadores.
                        while True:
                                print("\n--------------------------------------------")
                                print("          \033[1;35mModo Player vs Player\033[0m ")
                                print("--------------------------------------------")
                        
                                escolha = input("\n\033[32mPlayer 1 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 1 escolhe sua jogada.
                                escolha2 = input("\n\033[31mPlayer 2 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 2 escolhe sua jogada.
                                                
                                if escolha == "pedra" and escolha2 == "papel": # essa parte serve para ver qual jogador ganhou a rodada.
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "pedra" and escolha2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and escolha2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and escolha2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "tesoura" and escolha2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "tesoura" and escolha2 == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == escolha2:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                else:
                                        print("\n\033[1;37mOpção inválida! Ninguém ganha.\033[0m")
                                
                                print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontos_player2}\033[0m") # imprime o placar atual do jogo.

                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                                print("\n\033[1;37mOpção inválida\033[0m")
                                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()                
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n--------------------------------------------")   
                                        print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontos_player2}\033[0m") # imprime o placar atual do jogo.
                                        print("--------------------------------------------")   
                                        
                                        if pontos_player1 > pontos_player2: # caso o jogador escolha parar ele mostra quem foi o vencedor
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Player 1 venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------") 
                                        elif pontos_player1 == pontos_player2:
                                                print("\n--------------------------------------------")
                                                print("\n       \033[1;33m*** Empate! Ninguém Ganhou! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        elif pontos_player1 < pontos_player2:
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Player 2 venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        exit()

                pontos_player1 = 0 # contador para o jogador 1
                pontos_bot = 0 # contador para o Bot      

                if modo == "2": # caso a pessoa escoha o modo 2 iniciara o jogo Player vs Bot.
                        while True:
                                print("\n--------------------------------------------")
                                print("       \033[1;35mModo Player vs Computador\033[0m")
                                print("--------------------------------------------")

                                escolha = input("\n\033[32mPlayer escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 1 escolhe sua jogada.
                                        
                                numero = random.randint(1, 3) # essa parte gera um número aleatório entre 1 e 3 para o Bot escolher sua jogada
                                if numero == 1:
                                        escolha_bot = "pedra"
                                elif numero == 2:
                                        escolha_bot = "papel"
                                else:
                                        escolha_bot = "tesoura"
                                print("\n\033[1;31mBot escolheu:\033[0m", escolha_bot) # aqui é mostrada a jogada do Bot para o jogador 1.
                                                
                                if escolha == "pedra" and escolha_bot == "papel": # essa parte serve para ver qual jogador ganhou a rodada.
                                        print("\n--------------------------------------------")
                                        print("              \033[1;31mBot venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_bot += 1
                                elif escolha == "pedra" and escolha_bot == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mPlayer venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and escolha_bot == "pedra":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mPlayer venceu!\033[0m")
                                        print("\--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and escolha_bot == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("              \033[1;31mBot venceu!\033[0m")
                                        print("\--------------------------------------------")
                                        pontos_bot += 1
                                elif escolha == "tesoura" and escolha_bot == "pedra":
                                        print("\n--------------------------------------------")
                                        print("              \033[1;31mBot venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_bot += 1
                                elif escolha == "tesoura" and escolha_bot == "papel":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mPlayer venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == escolha_bot:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                else:
                                        print("\n\033[1;37mOpção inválida! Ninguém ganha.\033[0m")
                                    
                                print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mBot =\033[0m \033[1;37m{pontos_bot}\033[0m")  # aqui é mostrado o placar do jogo.

                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                                print("\n\033[1;37mOpção inválida\033[0m")
                                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()                
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n--------------------------------------------")   
                                        print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontos_bot}\033[0m") # imprime o placar atual do jogo.
                                        print("--------------------------------------------") 

                                        if pontos_player1 > pontos_bot: # aqui é verificado quem ganhou o jogo.
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Player venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        elif pontos_player1 == pontos_bot:
                                                print("\n--------------------------------------------")
                                                print("\n       \033[1;33m*** Empate! Ninguém Ganhou! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        elif pontos_player1 < pontos_bot:
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Bot venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        exit()
                
                pontos_bot1 = 0
                pontos_bot2 = 0        
                
                if modo == "3": # caso a pessoa escolha o modo 3 iniciara o jogo Bot vs Bot.
                        while True:
                                print("\n--------------------------------------------")
                                print(     "\033[1;35mModo Computador vs Computador\033[0m")
                                print("--------------------------------------------")
                                        
                                numero1 = random.randint(1, 3) # essa parte gera um número aleatório entre 1 e 3 para o Bot escolher sua jogada
                                if numero1 == 1:
                                        escolha_bot1 = "pedra"
                                elif numero1 == 2:
                                        escolha_bot1 = "papel"
                                else:
                                        escolha_bot1 = "tesoura"
                                
                                numero2 = random.randint(1, 3)
                                if numero2 == 1:
                                        escolha_bot2 = "pedra"
                                elif numero2 == 2:
                                        escolha_bot2 = "papel"
                                else:
                                        escolha_bot2 = "tesoura"
                                        
                                print("\n\033[1;32mBot 1 escolheu:\033[0m", escolha_bot1)
                                print("\n\033[1;31mBot 2 escolheu:\033[0m", escolha_bot2)     

                                if escolha_bot1 == "pedra" and escolha_bot2 == "papel": # essa parte serve para ver qual jogador ganhou a rodada.
                                        print("\n--------------------------------------------")
                                        print("             \033[1;31mBot 2 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot2 += 1
                                elif escolha_bot1 == "pedra" and escolha_bot2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mBot 1 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot1 += 1
                                elif escolha_bot1 == "papel" and escolha_bot2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mBot 1 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot1 += 1
                                elif escolha_bot1 == "papel" and escolha_bot2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;31mBot 2 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot2 += 1
                                elif escolha_bot1 == "tesoura" and escolha_bot2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;31mBot 2 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot2 += 1
                                elif escolha_bot1 == "tesoura" and escolha_bot2 == "papel":
                                        print("\n--------------------------------------------")
                                        print("             \033[1;32mBot 1 venceu!\033")
                                        print("--------------------------------------------")
                                        pontos_bot1 += 1
                                elif escolha_bot1 == escolha_bot2:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                else:
                                        print("\n\033[1;37mOpção inválida! Ninguém ganha.\033[0m")

                                print("--------------------------------------------")        
                                print(f"\033[1;37mPlacar:\033[0m \033[1;32mBot 1 =\033[0m {pontos_bot1} | \033[1;31mBot 2 =\033[0m {pontos_bot2}")  # aqui é mostrado o placar do jogo.
                                print("--------------------------------------------")
                                                    
                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                                print("\n\033[1;37mOpção inválida\033[0m")
                                                jogar_novamente = input("\n\033[1;37mDeseja continuar jogando? (s/n):\033[0m ").lower()                
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n--------------------------------------------")   
                                        print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_bot1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontos_bot2}\033[0m") # imprime o placar atual do jogo.
                                        print("--------------------------------------------") 
                                       
                                        if pontos_bot1 > pontos_bot2: # aqui é verificado quem ganhou o jogo.
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Bot 1 venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        elif pontos_bot1 == pontos_bot2:
                                                print("\n--------------------------------------------")
                                                print("\n       \033[1;33m*** Empate! Ninguém Ganhou! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        elif pontos_bot1 < pontos_bot2:    
                                                print("\n--------------------------------------------")
                                                print("\n     \033[1;33m*** Bot 2 venceu o jogo! ***\033[0m")
                                                print("\n--------------------------------------------")
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        exit()

                else: # caso a pessoa escolha o modo 4, finalizara o jogo
                        print("\n-------------------------------------------------------------------------------------------")
                        print("                                \033[1;37m*** Volte sempre ***")
                        print("       Agradecimento Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer\033[0m")
                        print("-------------------------------------------------------------------------------------------")
                        break
        else:
                print("\n\033[1;37mOpção inválida!\033[0m\n") # caso o jogador escolha uma opção invalida, ele recebe uma mensagem de erro.