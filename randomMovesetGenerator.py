import random

import constants


def get_random_move(attack_type, distribution):
    key_str = ""

    if attack_type not in ['PHY', 'SPE', 'STA']:
        key_str = attack_type
    else:
        roll = random.randrange(1, 100)
        if roll <= distribution[0]:
            key_str = attack_type + "1"
        elif roll <= distribution[1]:
            key_str = attack_type + "2"
        elif roll <= distribution[2]:
            key_str = attack_type + "3"
        elif roll <= distribution[3]:
            key_str = attack_type + "4"
        elif roll > distribution[4]:
            key_str = attack_type + "5"
        elif roll <= distribution[5]:
            key_str = attack_type + "6"
        elif roll <= distribution[6]:
            key_str = attack_type + "7"

    return random.choice(constants.kanto_attack_dict[key_str])

def get_type_name(type_num):
    if random.random() < 0.5:
        type_str = type_num.hex()[0:2].upper()
    else:
        type_str = type_num.hex()[2:].upper()
    
    if type_str == '01':
        return 'FIGHTING'
    elif type_str == '02':
        return 'FLYING'
    elif type_str == '03':
        return 'POISON'
    elif type_str == '04':
        return 'GROUND'
    elif type_str == '05':
        return 'ROCK'
    elif type_str == '07':
        return 'BUG'
    elif type_str == '08':
        return 'GHOST'
    elif type_str == '14':
        return 'FIRE'
    elif type_str == '15':
        return 'WATER'
    elif type_str == '16':
        return 'GRASS'
    elif type_str == '17':
        return 'ELECTRIC'
    elif type_str == '18':
        return 'PSYCHIC'
    elif type_str == '19':
        return 'ICE'
    elif type_str == '1A':
        return 'DRAGON'
    else: # type == '00' or a bad value got in here
        return 'NORMAL'

class MovesetGenerator:
    @staticmethod
    def get_random_moveset(bst_list, rando_factor, pkm_type):
        bst = sum(bst_list)

        # first type of move is always a damaging move that lines up with higher attacking stat
        first_type = "PHY" if bst_list[1] > bst_list[4] else "SPE"
        
        # second move is a STAB damaging move if factor is 1
        if (rando_factor == 1):
            if random.random() < 0.4:
                second_type = get_type_name(pkm_type)
            else:
                if random.random() < 0.5:
                    second_type = "PHY"
                else:
                    second_type = "SPE"
        else:
            one_in_three = random.randrange(1, 99)
            if one_in_three <= 33:
                second_type = "PHY"
            elif one_in_three <= 66:
                second_type = "SPE"
            else:
                second_type = "STA"

        # third move afflicts a status or affects stats if factor is 1 or 2
        if (rando_factor < 3):
            third_type = "STA"
        else:
            one_in_three = random.randrange(1, 99)
            if one_in_three <= 33:
                third_type = "PHY"
            elif one_in_three <= 66:
                third_type = "SPE"
            else:
                third_type = "STA"

        # fourth move is random
        one_in_three = random.randrange(1, 99)
        if one_in_three <= 33:
            fourth_type = "PHY"
        elif one_in_three <= 66:
            fourth_type = "SPE"
        else:
            fourth_type = "STA"

        attack_types = [first_type, second_type, third_type, fourth_type]
        moveset = []
        if (rando_factor == 1):
            if bst <= 225:
                distribution = constants.stat_distribution_list[0]
            elif bst <= 300:
                distribution = constants.stat_distribution_list[1]
            elif bst <= 375:
                distribution = constants.stat_distribution_list[2]
            elif bst <= 450:
                distribution = constants.stat_distribution_list[3]
            else:
                distribution = constants.stat_distribution_list[4]
        elif (rando_factor == 2):
            if bst <= 300:
                distribution = constants.stat_distribution_list[random.randrange(0, 1)]
            elif bst <= 450:
                distribution = constants.stat_distribution_list[random.randrange(2, 3)]
            else:
                distribution = constants.stat_distribution_list[4]
        else:
            distribution = constants.stat_distribution_list[random.randrange(0, 4)]

        for atk_type in attack_types:
            random_move = get_random_move(atk_type, distribution)
            while True:
                if random_move in moveset:
                    random_move = get_random_move(atk_type, distribution)
                else:
                    break
            moveset.append(random_move)

        return moveset
