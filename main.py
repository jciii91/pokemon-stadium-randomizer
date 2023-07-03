import sys
import util
import n64Checksum
import randomizePokemonBaseValues
import writeDisplayData

#if len(sys.argv) != 3:
#    print("ERROR: Script only accepts 2 arguments.")
#    exit(1)

#romPath = sys.argv[1]
#exePath = sys.argv[2]
new_display_stats = []

romPath = ""
exePath = ""

randomizer = randomizePokemonBaseValues.BaseValuesRandomizer()

evs = []
ivs = []
for ev_set in range(0, 151):
    evs.append(util.Util.random_int_set(0, 65535, 5))
    ivs.append(util.Util.random_string_hex(4))

with open(romPath, "rb+") as rom:
    rom.seek(465825)
    for i in range(0, 151):
        stats = bytearray(rom.read(5))
        rom.seek(-5, 1)
        randomizer.set_original_stats(stats)
        randomized_base_stats = randomizer.randomizestats()
        new_display_stats.append(randomized_base_stats)
        rom.write(randomized_base_stats)
        rom.seek(18, 1)

    rom.seek(9119629)
    for j in range(0, 151):
        new_attacks = util.Util.random_int_set(1, 164, 4)
        new_attacks_bytearray = bytearray()
        for attack in new_attacks:
            new_attacks_bytearray.extend(int.to_bytes(attack, 1, "big"))
        rom.write(new_attacks_bytearray)

        rom.seek(7, 1)
        for k in range(0, 5):
            ev = int.to_bytes(evs[j][k], 2, "big")
            rom.write(ev)
        iv_str = rom.write(bytes.fromhex(ivs[j]))

        rom.seek(6, 1)
        disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(new_display_stats[j], evs[j], ivs[j])
        rom.write(disp)
        rom.seek(45, 1)

n64CS = n64Checksum.CheckSum(exePath, romPath)
n64CS.callsubprocess()
