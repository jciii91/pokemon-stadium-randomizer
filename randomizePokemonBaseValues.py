import random
import constants

class BaseValuesRandomizer:
    def __init__(self, rando_factor):
        self.min_val = 20
        self.max_val = 235
        self.stats = bytearray()
        self.rando_factor = rando_factor

    def set_original_stats(self, stats_array):
        self.stats = stats_array

    def select_index(self):
        weight_map = {
            1: constants.bst_weights[0] if random.random() < 0.5 else constants.bst_weights[1],
            2: constants.bst_weights[2],
            3: constants.bst_weights[3]
        }
        
        return random.choices([0, 1, 2, 3, 4], weights=weight_map.get(self.rando_factor, constants.bst_weights[0]))[0]

    def randomize_stats(self):
        bst_list = []
        for stat in self.stats:
            bst_list.append(stat)
        bst = sum(bst_list)
        new_stats_bytes = bytearray()

        # Start with an array of 5 numbers, all at the minimum value
        new_stats = [self.min_val] * 5
        current_sum = sum(new_stats)

        # Increment numbers until we reach BST
        while current_sum < bst:
            # Randomly select an index to increase
            idx = self.select_index()

            # Only increase if it won't exceed max_val
            if new_stats[idx] < self.max_val:
                new_stats[idx] += 1
                current_sum += 1
            else:
                # Check if all numbers are maxed out (should never happen with correct BST input)
                if all(n == self.max_val for n in new_stats):
                    raise RuntimeError("All stats reached max_val but BST is not yet met. Something went wrong!")

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
