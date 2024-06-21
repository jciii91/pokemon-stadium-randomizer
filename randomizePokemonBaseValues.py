import random
import math

# [HP, ATK, DEF, SPD, SPC]
# global base stat constants (units are %)
# example shown here is default settings
# MIN_BASE_PERCENT = [15, 15, 15, 15, 15]
# MAX_BASE_PERCENT = [43, 43, 43, 43, 43]


class BaseValuesRandomizer:
    def __init__(self, rando_factor):
        self.stats = bytearray()
        if (rando_factor == 2):
            self.MIN_BASE_PERCENT = [5, 5, 5, 5, 5]
            self.MAX_BASE_PERCENT = [53, 53, 53, 53, 53]
        elif (rando_factor == 3):
            self.MIN_BASE_PERCENT = [1, 1, 1, 1, 1]
            self.MAX_BASE_PERCENT = [96, 96, 96, 96, 96]
        else:
            self.MIN_BASE_PERCENT = [15, 15, 15, 15, 15]
            self.MAX_BASE_PERCENT = [43, 43, 43, 43, 43]

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
                if remaining_percentage > self.MIN_BASE_PERCENT[i]:
                    if remaining_percentage < self.MAX_BASE_PERCENT[i]:
                        bst_percentage = random.randrange(self.MIN_BASE_PERCENT[i], remaining_percentage)
                    else:
                        bst_percentage = random.randrange(self.MIN_BASE_PERCENT[i], self.MAX_BASE_PERCENT[i])
                else:
                    bst_percentage = self.MIN_BASE_PERCENT[i]
                new_stats[i] = math.floor(bst * (bst_percentage/100))
                remaining_percentage = remaining_percentage - bst_percentage

            # check that the remaining percentage of BST to be assigned falls within the randomizer settings
            if self.MAX_BASE_PERCENT[4] >= remaining_percentage >= self.MIN_BASE_PERCENT[4]:
                new_stats[4] = bst - sum(new_stats)
            
            # if all new stats are between the inclusive limits of 1 and 255 then move on
            if not(any(isinstance(x, int) and x > 255 for x in new_stats) or any(isinstance(x, int) and x < 1 for x in new_stats)):
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
