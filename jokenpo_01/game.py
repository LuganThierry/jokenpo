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
    
    return game_res(choice, computer)


def game_res(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "Empate!"
    
    if [user_choice, computer_choice] == [1, 2]:
        return "Você perdeu, sua pedra é enrolada pelo papel"
    
    if [user_choice, computer_choice] == [1, 3]:
        return "Você ganhou, sua pedra quebra a tesoura"
    
    if [user_choice, computer_choice] == [2, 1]:
        return "Você ganhou, seu papel enrola a pedra"
    
    if [user_choice, computer_choice] == [2, 3]:
        return "Você perdeu, seu papel é cortado pela tesoura"
    
    if [user_choice, computer_choice] == [3, 1]:
        return "Você perdeu, sua tesoura é quebrada pela pedra"
    
    if [user_choice, computer_choice] == [3, 2]:
        return "Você ganhou, sua tesoura corta o papel"

choice = input("1 - Pedra\n2 - Papel\n3 - Tesoura\n")

print(game(choice))