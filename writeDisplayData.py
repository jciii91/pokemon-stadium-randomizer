import math

import util

class DisplayDataWriter:
    @staticmethod
    def write_gym_tower_display(new_display_stats_set, evs, iv_str):
        ivs = [0, 0, 0, 0, 0]
        iv_binary = "{0:016b}".format(int(iv_str, 16))
        for i in range(0, 4):
            int_val = int(iv_binary[i * 4:(i * 4 + 4)], 2)
            ivs[i + 1] = int_val
            if int_val % 2 != 0:
                ivs[0] = int(ivs[0] + math.pow(2, 3 - i))

        display_stats = bytearray()
        new_displays_int = [int(x) for x in new_display_stats_set]
        display = util.Util.calculate_stat(new_displays_int[0], evs[0], ivs[0], 50) + 50 + 10
        display_stats.extend(display.to_bytes(2, "big"))
        for j in range(1, 5):
            display = util.Util.calculate_stat(new_displays_int[j], evs[j], ivs[j], 50) + 5
            display_stats.extend(display.to_bytes(2, "big"))
        return display_stats
