import random

# global base stat constants
# min stat of each category is smallest seen in game
MIN_BASE_STATS = [10, 5, 5, 15, 20]
# same for max stats except for HP
# Chansey's 250 is too high so Snorlax is being used
MAX_BASE_STATS = [160, 134, 180, 140, 154]


class BaseValuesRandomizer:
    def __init__(self):
        self.stats = []

    def set_original_stats(self, stats_array):
        self.stats = stats_array

    def randomizestats(self):
        bst = sum(self.stats)
        remaining_bst = bst - sum(MIN_BASE_STATS)
        new_stats_bytes = bytearray()

        while True:
            new_stats = [0, 0, 0, 0, 0]
            remaining_bst = bst
            for i in range(0, 4):
                if remaining_bst > MIN_BASE_STATS[i]:
                    if remaining_bst < MAX_BASE_STATS[i]:
                        new_stats[i] = random.randrange(MIN_BASE_STATS[i], remaining_bst)
                    else:
                        new_stats[i] = random.randrange(MIN_BASE_STATS[i], MAX_BASE_STATS[i])
                else:
                    new_stats[i] = MIN_BASE_STATS[i]
                remaining_bst = remaining_bst - new_stats[i]
            new_stats[4] = bst - sum(new_stats)
            if MAX_BASE_STATS[4] >= new_stats[4] >= MIN_BASE_STATS[4]:
                break

        for stat in new_stats:
            new_stats_bytes.extend(stat.to_bytes(1, "big"))

        return new_stats_bytes
