import random
import math

# [HP, ATK, DEF, SPD, SPC]
# global base stat constants (units are %)
MIN_BASE_PERCENT = [15, 15, 15, 15, 15]
MAX_BASE_PERCENT = [43, 43, 43, 43, 43]


class BaseValuesRandomizer:
    def __init__(self):
        self.stats = bytearray()

    def set_original_stats(self, stats_array):
        self.stats = stats_array

    def randomize_stats(self):
        bst_list = []
        for stat in self.stats:
            bst_list.append(stat)
        bst = sum(bst_list)
        new_stats_bytes = bytearray()

        while True:
            new_stats = [0, 0, 0, 0, 0]
            remaining_percentage = 100
            for i in range(0, 4):
                if remaining_percentage > MIN_BASE_PERCENT[i]:
                    if remaining_percentage < MAX_BASE_PERCENT[i]:
                        bst_percentage = random.randrange(MIN_BASE_PERCENT[i], remaining_percentage)
                    else:
                        bst_percentage = random.randrange(MIN_BASE_PERCENT[i], MAX_BASE_PERCENT[i])
                else:
                    bst_percentage = MIN_BASE_PERCENT[i]
                new_stats[i] = math.floor(bst * (bst_percentage/100))
                remaining_percentage = remaining_percentage - bst_percentage
            if MAX_BASE_PERCENT[4] >= remaining_percentage >= MIN_BASE_PERCENT[4]:
                new_stats[4] = bst - sum(new_stats)
                break

        random.shuffle(new_stats)
        for stat in new_stats:
            try:
                new_stats_bytes.extend(stat.to_bytes(1, "big"))
            except OverflowError:
                print("ERROR: BST is too high.")
                print("BST_STR: " + str(self.stats))
                print("BST: " + str(bst))
                print("STATS: " + str(new_stats))
                exit(1)

        return new_stats_bytes
