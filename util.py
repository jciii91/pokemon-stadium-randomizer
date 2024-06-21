import math
import random


class Util:

    @staticmethod
    def calculate_stat(stat, ev, iv, level):
        return int((((stat + iv) * 2 + math.ceil(math.sqrt(ev) / 4)) * level)/100)

    @staticmethod
    def random_int_set(min_val, max_val, count):
        return random.sample(range(min_val, max_val), count)

    @staticmethod
    def random_string_hex(length):
        int_set = random.sample(range(0, 15), length)
        return_hex = ""
        for integer in int_set:
            return_hex = return_hex + hex(integer)[2:]
        return return_hex
