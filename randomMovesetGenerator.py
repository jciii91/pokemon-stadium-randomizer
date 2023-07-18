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
    def get_random_moveset(bst):
        attack_types = ["PHY", "PHY", "SPE", "STA"]
        moveset = []
        distribution = []
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

        for atk_type in attack_types:
            moveset.append(get_random_move(atk_type, distribution))

        return moveset
