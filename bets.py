#bets file

def usr_bet_1(slot_machine_instance, bet):
    prize_sum = prize_distribution(slot_machine_instance, slot_machine_instance.matrix[1][0])
    slot_machine_instance.balance += prize_sum
    print ("You win {} dinheiros".format(prize_sum))

def usr_bet_2(slot_machine_instance, bet):
    prize_sum = 0
    pos = slot_machine_instance.matrix
    if pos[1][0] == pos[1][1] == pos[1][2]:
        relevant_position = pos[1][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[2][0] == pos[2][1] == pos[2][2]:
        relevant_position = pos[2][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[0][0] == pos[0][1] == pos[0][2]:
        relevant_position = pos[0][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if prize_sum > 0:
        slot_machine_instance.balance += prize_sum
        print("You win {} dinheiros".format(prize_sum))

def usr_bet_3(slot_machine_instance, bet):
    prize_sum = 0
    pos = slot_machine_instance.matrix
    if pos[1][0] == pos[1][1] == pos[1][2]:
        relevant_position = pos[1][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[2][0] == pos[2][1] == pos[2][2]:
        relevant_position = pos[2][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[0][0] == pos[0][1] == pos[0][2]:
        relevant_position = pos[0][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[0][0] == pos[1][1] == pos[2][2]:
        relevant_position = pos[0][0]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if pos[0][2] == pos[1][1] == pos[2][0]:
        relevant_position = pos[0][2]
        prize_sum += prize_distribution(slot_machine_instance, relevant_position)
    if prize_sum > 0:
        slot_machine_instance.balance += prize_sum
        print("You win {} dinheiros".format(prize_sum))

def prize_distribution(slot_machine_instance, relevant_position):
    if relevant_position == 1:
        return 300
    elif relevant_position == 2:
        return 50
    elif relevant_position == 3:
        return 15
    elif relevant_position == 4:
        return 10
    elif relevant_position == 5:
        return 8
    elif relevant_position == 6:
        return 6
    else:
        return 0
