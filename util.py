import math


class Util:

    @staticmethod
    def calculate_stat(stat, ev, iv, level):
        return int((((stat + iv) * 2 + (math.sqrt(ev) / 4)) * level)/100)
