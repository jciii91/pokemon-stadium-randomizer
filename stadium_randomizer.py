import random
import shutil

import constants
import util
import n64Checksum
import randomizePokemonBaseValues
import randomMovesetGenerator
import writeDisplayData

def randomizer_func(rom_path, output_file, settings_dict):
    exe_path = "n64-checksum.exe"
    base_rando_factor = int(settings_dict['base'])
    attack_rando_factor = int(settings_dict['attack'])

    randomizer = randomizePokemonBaseValues.BaseValuesRandomizer(base_rando_factor)

    new_display_stats = []
    bst_list = []
    evs = []
    ivs = []
    for ev_set in range(0, 151):
        evs.append(util.Util.random_int_set(0, 65535, 5))
        ivs.append(util.Util.random_string_hex(4))

    shutil.copy(rom_path, output_file)
    with open(output_file, "rb+") as rom:
        # randomize base stats, unless setting set to 'Vanilla'
        rom.seek(465825)
        if base_rando_factor > 0:
            for i in range(0, 151):
                stats = bytearray(rom.read(5))
                rom.seek(-5, 1)
                randomizer.set_original_stats(stats)
                randomized_base_stats = randomizer.randomize_stats()

                bst_str = randomized_base_stats.hex()
                bst = []
                for offset in range(0, 5):
                    index = offset * 2
                    bst.append(int(bst_str[index:index + 2], 16))
                bst_list.append(bst)

                new_display_stats.append(randomized_base_stats)
                rom.write(randomized_base_stats)
                rom.seek(18, 1)

        # randomize round 1 gym castle Pokémon
        rom.seek(9057228)
        for q in range(0, 10):
            team_count = 4 if q < 9 else 7
            for r in range(0, team_count):
                new_team = random.sample(range(0, 149), 6)
                for s in range(0, 6):
                    pokedex_num = new_team[s]
                    rom.write(int.to_bytes(pokedex_num + 1, 1, "big"))
                    rom.seek(5, 1)
                    new_type = constants.kanto_dex_names[pokedex_num]["type"]
                    rom.write(bytes.fromhex(new_type))

                    rom.seek(1, 1)
                    # randomize moveset unless setting is 'Vanilla'
                    if attack_rando_factor > 0:
                        new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst_list[pokedex_num], attack_rando_factor)
                        new_attacks_bytearray = bytearray()
                        for attack in new_attacks:
                            new_attacks_bytearray.extend(int.to_bytes(attack, 1, "big"))
                        rom.write(new_attacks_bytearray)
                    else:
                        rom.seek(4,1)

                    rom.seek(4, 1)
                    exp = int.to_bytes(int(constants.kanto_dex_names[pokedex_num]["exp"]), 3, "big")
                    rom.write(exp)
                    for t in range(0, 5):
                        ev = int.to_bytes(evs[pokedex_num][t], 2, "big")
                        rom.write(ev)
                    rom.write(bytes.fromhex(ivs[pokedex_num]))

                    rom.seek(6, 1)
                    disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(new_display_stats[pokedex_num], evs[pokedex_num], ivs[pokedex_num])
                    rom.write(disp)

                    pokemon_name = constants.kanto_dex_names[pokedex_num]["name"]
                    rom.write(pokemon_name.encode())
                    # check if a Nidoran is being written in to add their gender symbol
                    if pokedex_num == 28:
                        rom.write(bytes.fromhex("BE"))
                        pokemon_name = pokemon_name + " "
                    elif pokedex_num == 31:
                        rom.write(bytes.fromhex("A9"))
                        pokemon_name = pokemon_name + " "
                    if len(pokemon_name) < 10:
                        blanks = 10 - len(pokemon_name)
                        for blank in range(0, blanks):
                            rom.write(bytes.fromhex("00"))
                    rom.seek(26, 1)
                rom.seek(56, 1)
            rom.seek(16, 1)

        # randomize gym castle rentals
        rom.seek(9119629)
        for j in range(0, 149):
            # randomize moveset unless setting is 'Vanilla'
            if attack_rando_factor > 0:
                new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst_list[j], attack_rando_factor)
                new_attacks_bytearray = bytearray()
                for attack in new_attacks:
                    new_attacks_bytearray.extend(int.to_bytes(attack, 1, "big"))
                rom.write(new_attacks_bytearray)
            else:
                rom.seek(4,1)

            rom.seek(7, 1)
            for k in range(0, 5):
                ev = int.to_bytes(evs[j][k], 2, "big")
                rom.write(ev)
            rom.write(bytes.fromhex(ivs[j]))

            rom.seek(6, 1)
            disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(new_display_stats[j], evs[j], ivs[j])
            rom.write(disp)
            rom.seek(45, 1)

    n64_cs = n64Checksum.CheckSum(exe_path, output_file)
    n64_cs.call_subprocess()
