import random

# global base stat constants
MIN_BASE_STATS = [10, 5, 5, 15, 20]


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
            for i in range(0, 4):
                if remaining_bst > MIN_BASE_STATS[i]:
                    if remaining_bst < 255:
                        new_stats[i] = random.randrange(MIN_BASE_STATS[i], remaining_bst)
                    else:
                        new_stats[i] = random.randrange(MIN_BASE_STATS[i], 255)
                else:
                    new_stats[i] = MIN_BASE_STATS[i]
                remaining_bst = remaining_bst - new_stats[i]
            new_stats[4] = bst - sum(new_stats)
            if new_stats[4] <= 255:
                break

        for stat in new_stats:
            new_stats_bytes.extend(stat.to_bytes(1, "big"))

        return new_stats_bytes
