import random

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    PEDRA
    """

papel = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    PAPEL
    """

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    TESOURA
    """

def game(choice):

    if not choice.isdigit():
        return "Dígito incorreto"
    
    choice = int(choice)

    if choice not in [1, 2, 3]:
        return "Insira 1, 2, ou 3"
    
    computer = random.randint(1, 3)

    choice_dict = {
        1: pedra,
        2: papel,
        3: tesoura
    }

    print(f'Você escolheu {choice_dict[choice]}')
    print(f'Computador escolheu {choice_dict[computer]}')

    res = game_res(choice, computer)
    
    return print(res)


def game_res(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "Empate!"
    
    outcomes = {
            (1, 2): "Você perdeu, papel enrola pedra",
            (1, 3): "Você ganhou, pedra quebra tesoura",
            (2, 1): "Você ganhou, papel enrola pedra",
            (2, 3): "Você perdeu, tesoura corta papel",
            (3, 1): "Você perdeu, pedra quebra tesoura",
            (3, 2): "Você ganhou, tesoura corta papel"
        }

    return outcomes[(user_choice, computer_choice)]


choice = input("1 - Pedra\n2 - Papel\n3 - Tesoura\n")

game(choice)