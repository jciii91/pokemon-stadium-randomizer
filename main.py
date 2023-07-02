import sys
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
display_writer = writeDisplayData.DisplayDataWriter()

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

    rom.seek(9119640)
    for i in range(0, 151):
        evs = []
        for j in range(0, 5):
            evs.append(rom.read(2))
        iv_str = rom.read(2)

        rom.seek(6, 1)
        disp = display_writer.write_gym_tower_display(new_display_stats[i], evs, iv_str)
        rom.write(disp)
        rom.seek(56, 1)

n64CS = n64Checksum.CheckSum(exePath, romPath)
n64CS.callsubprocess()
