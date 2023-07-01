import sys

import n64Checksum
import randomizePokemonBaseValues

if len(sys.argv) != 3:
    print("ERROR: Script only accepts 2 arguments.")
    exit(1)

romPath = sys.argv[1]
exePath = sys.argv[2]

with open(romPath, "rb+") as rom:
    rom.seek(465825)
    randomizer = randomizePokemonBaseValues.BaseValuesRandomizer()

    for i in range(0, 151):
        stats = bytearray(rom.read(5))
        rom.seek(-5, 1)
        randomizer.set_original_stats(stats)
        rom.write(randomizer.randomizestats())
        rom.seek(18, 1)

n64CS = n64Checksum.CheckSum(exePath, romPath)
n64CS.callsubprocess()
