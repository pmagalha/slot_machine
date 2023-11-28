import re
import slot_machine
import random
import sys
import bets

deposit_pattern = re.compile(r"^(?:[1-9]|[1-9][0-9]|[1-4][0-9][0-9]|500)$")
bet_pattern = re.compile(r"^[1-3]$")

def main():
    slot_machine_instance = slot_machine.Slot_machine()
    print_matrix(slot_machine_instance.matrix)
    prompt_dep = input("How much to deposit? [1 - 500] (Press 'q' to quit): ")

    if deposit_pattern.match(str(prompt_dep)):
                print("Ok")
                deposit_amount = int(prompt_dep)
                slot_machine_instance.deposit(deposit_amount)
                print("Current balance:", slot_machine_instance.balance)

    while True:
        prompt_bet = input("How much to bet? [1, 2, 3] (Press 'q' to quit): ")
        if prompt_bet == 'q':
            sys.exit(1)("You quit the game")
        try:
            if bet_pattern.match(str(prompt_bet)):
                bet_amount = int(prompt_bet)
                start_slots(slot_machine_instance, prompt_bet)
                print("Matrix after bet:")
                print_matrix(slot_machine_instance.matrix)
                slot_machine_instance.bet_internal(bet_amount)
                check_slot(slot_machine_instance, prompt_bet)
                print("Current balance:", slot_machine_instance.balance)
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError as e:
            print("You lost")
            sys.exit(1)("Game Over")

def check_slot(slot_machine_instance, bet):
    if bet == 1 and (slot_machine_instance.matrix[1][0] == slot_machine_instance.matrix[1][1] == slot_machine_instance.matrix[1][2]):
        bets.usr_bet_1(slot_machine_instance, bet)
    elif bet == 2:
        bets.usr_bet_2(slot_machine_instance, bet)
    elif bet == 3:
        bets.usr_bet_3(slot_machine_instance, bet)

def start_slots(slot_machine_instance, bet):
    for i in range(3):
        for j in range(3):
            slot_machine_instance.matrix[i][j] = random.randint(1, 6) 

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()