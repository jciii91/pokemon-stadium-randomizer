import random

import constants


def get_random_move(attack_type, distribution):
    key_str = ""
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


class MovesetGenerator:
    @staticmethod
    def get_random_moveset(bst_list, rando_factor):
        bst = sum(bst_list)

        if (rando_factor < 3):
            first_type = "PHY" if bst_list[1] > bst_list[4] else "SPE"
        else:
            one_in_three = random.randrange(1, 99)
            if one_in_three <= 33:
                first_type = "PHY"
            elif one_in_three <= 66:
                first_type = "SPE"
            else:
                first_type = "STA"
        
        if (rando_factor == 1):
            coin_flip = random.randrange(1, 100)
            if coin_flip <= 50:
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

        if (rando_factor == 1):
            third_type = "STA"
        else:
            one_in_three = random.randrange(1, 99)
            if one_in_three <= 33:
                third_type = "PHY"
            elif one_in_three <= 66:
                third_type = "SPE"
            else:
                third_type = "STA"

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
