import random

menu = """
Bem vindo ao jogo de dados
as regras são simples:
rode dois dados, tire
números iguais, vença,
tire números diferentes,
perca.
Boa Sorte!
==========================
digite 1 para jogar e 2 para sair
-->"""

dado01 = random.randint(1,6)
dado02 = random.randint(1,6)

while True:

    opcao = input(menu)

    if opcao == "1":
        print (f"Esses são seus números: {dado01} e {dado02}")

        if dado01 == dado02:
            print("Parabéns, você venceu!")
            break
        else:
            print("Infelizmente você perdeu, tente novamente")
            break

    elif opcao == "2":
        break

    else:
        print("Operação inválida, tente novamente")
