import random

import constants
import util
import randomizePokemonBaseValues
import randomMovesetGenerator
import writeDisplayData

def randomizer_func(rom, settings_dict):
    setting_version = settings_dict['version']
    setting_base_stats = settings_dict['base_stats']
    setting_rentals_round1 = settings_dict['rentals_round1']
    setting_gymcastle_round1 = settings_dict['gymcastle_round1']

    randomizer = randomizePokemonBaseValues.BaseValuesRandomizer(setting_base_stats)

    new_display_stats = []
    bst_list = []
    evs = []
    ivs = []
    for ev_set in range(0, 151):
        evs.append(util.Util.random_int_set(0, 65535, 5))
        ivs.append(util.Util.random_string_hex(4))

    # disable checksum
    print("Disabling checksum...")
    offset = constants.rom_offsets[setting_version]["CheckSum1"]
    new_bytes = bytes.fromhex("3C1C8041")
    rom[offset:offset + len(new_bytes)] = new_bytes

    offset = constants.rom_offsets[setting_version]["CheckSum2"]
    new_bytes = bytes.fromhex("00000000")
    rom[offset:offset + len(new_bytes)] = new_bytes
    
    # randomize base stats, unless setting set to 'Vanilla'
    if setting_base_stats > 0:
        print("Randomizing base stats...")
        offset = constants.rom_offsets[setting_version]["BaseStats"]
        for _ in range(151):
            stats = rom[offset:offset + 5]  # Read 5 bytes
            randomizer.set_original_stats(stats)
            randomized_base_stats = randomizer.randomize_stats()

            # Convert to list of integers for BST processing
            bst_list.append(list(randomized_base_stats))

            # Store modified stats for display
            new_display_stats.append(randomized_base_stats)

            # Write the new randomized stats back
            rom[offset:offset + 5] = randomized_base_stats

            # Move to the next Pokémon entry (skip 18 additional bytes)
            offset += 23

    # change pointer for gym castle round 1 rentals to custom table
    if setting_gymcastle_round1 > 0:
        print("Redirecting round 1 rental table pointer...")
        offset = constants.rom_offsets[setting_version]["Rental_GymCastle_Round1_Pointer"]
        new_bytes = bytes.fromhex(constants.rom_offsets[setting_version]["OffsetToNewTable"]) # write new offset and new table size
        rom[offset:offset + len(new_bytes)] = new_bytes

    # randomize round 1 gym castle Pokémon
    if setting_gymcastle_round1 > 0:
        print("Randomizing round 1 gym castle trainers...")
        offset = constants.rom_offsets[setting_version]["GymCastle_Round1"]
        for q in range(10):
            team_count = 4 if q < 9 else 7
            for r in range(team_count):
                new_team = random.sample(range(151), 6)
                for s in range(6):
                    pokedex_num = new_team[s]
                    rom[offset] = pokedex_num + 1  # Write Pokémon index
                    offset += 1

                    offset += 5  # Seek forward by 5 bytes

                    new_type = bytes.fromhex(constants.kanto_dex_names[pokedex_num]["type"])
                    rom[offset:offset + len(new_type)] = new_type  # Write Pokémon type
                    offset += len(new_type)

                    offset += 1  # Seek forward by 1 byte

                    # Random moveset
                    new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst_list[pokedex_num], setting_gymcastle_round1, new_type)
                    for attack in new_attacks:
                        rom[offset] = attack
                        offset += 1

                    offset += 4  # Seek forward by 4 bytes

                    exp = int.to_bytes(int(constants.kanto_dex_names[pokedex_num]["exp"]), 3, "big")
                    rom[offset:offset + 3] = exp
                    offset += 3

                    for t in range(5):
                        ev = int.to_bytes(evs[pokedex_num][t], 2, "big")
                        rom[offset:offset + 2] = ev
                        offset += 2

                    ivs_bytes = bytes.fromhex(ivs[pokedex_num])
                    rom[offset:offset + len(ivs_bytes)] = ivs_bytes
                    offset += len(ivs_bytes)

                    offset += 6  # Seek forward by 6 bytes

                    disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(
                        new_display_stats[pokedex_num], evs[pokedex_num], ivs[pokedex_num]
                    )
                    rom[offset:offset + len(disp)] = disp
                    offset += len(disp)

                    pokemon_name = constants.kanto_dex_names[pokedex_num]["name"].encode()
                    rom[offset:offset + len(pokemon_name)] = pokemon_name
                    offset += len(pokemon_name)

                    # Check if a Nidoran is being written in to add their gender symbol
                    if pokedex_num == 28:
                        rom[offset:offset + 1] = bytes.fromhex("BE")  # Female symbol
                        offset += 1
                        pokemon_name += b" "
                    elif pokedex_num == 31:
                        rom[offset:offset + 1] = bytes.fromhex("A9")  # Male symbol
                        offset += 1
                        pokemon_name += b" "

                    # Fill in blank spaces to make the name 11 bytes long
                    if len(pokemon_name) < 11:
                        blanks = 11 - len(pokemon_name)
                        rom[offset:offset + blanks] = b"\x00" * blanks
                        offset += blanks

                    offset += 25  # Seek forward by 25 bytes
                offset += 56  # Seek forward by 56 bytes
            offset += 16  # Seek forward by 16 bytes

    # randomize gym castle rentals
    if setting_rentals_round1 > 0:
        print("Randomizing round 1 gym castle rentals...")
        offset = constants.rom_offsets[setting_version]["EmptyRomSpace"]

        # Write expected number of returned Pokémon
        rom[offset:offset + 4] = bytes.fromhex("00000097")
        offset += 4

        for j in range(151):
            rom[offset] = j + 1  # Write Dex number
            offset += 1

            rom[offset:offset + 1] = bytes.fromhex("00")
            offset += 1

            rom[offset:offset + 2] = bytes.fromhex("0080")  # "Current HP"
            offset += 2

            rom[offset:offset + 1] = bytes.fromhex("32")  # Level
            offset += 1

            rom[offset:offset + 1] = bytes.fromhex("00")  # Status
            offset += 1

            pkm_type = bytes.fromhex(constants.kanto_dex_names[j]["type"])
            rom[offset:offset + 2] = pkm_type # Type(s)
            offset += 2

            rom[offset:offset + 1] = bytes.fromhex("00")
            offset += 1

            # Random moveset
            new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst_list[j], setting_rentals_round1, pkm_type)
            for attack in new_attacks:
                rom[offset] = attack
                offset += 1

            rom[offset:offset + 1] = bytes.fromhex("00")
            offset += 1

            rom[offset:offset + 2] = bytes.fromhex("1110")  # Trainer ID
            offset += 2

            rom[offset:offset + 1] = bytes.fromhex("00")
            offset += 1

            exp_bytes = int.to_bytes(int(constants.kanto_dex_names[j]["exp"]), 3, "big")
            rom[offset:offset + 3] = exp_bytes  # Experience
            offset += 3

            for k in range(5):
                ev = int.to_bytes(evs[j][k], 2, "big")
                rom[offset:offset + 2] = ev
                offset += 2

            ivs_bytes = bytes.fromhex(ivs[j])
            rom[offset:offset + len(ivs_bytes)] = ivs_bytes
            offset += len(ivs_bytes)

            rom[offset:offset + 4] = bytes.fromhex("00000000")
            offset += 4  # I think setting these to 0 gives you the vanilla PP for moves

            rom[offset:offset + 1] = bytes.fromhex("32")  # Level again
            offset += 1

            rom[offset:offset + 1] = bytes.fromhex("00")
            offset += 1

            disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(new_display_stats[j], evs[j], ivs[j])
            rom[offset:offset + len(disp)] = disp
            offset += len(disp)

            pokemon_name = constants.kanto_dex_names[j]["name"].encode().ljust(11, b'\x00')
            rom[offset:offset + 11] = pokemon_name  # Name
            offset += 11

            rom[offset:offset + 8] = bytes.fromhex("52414E444F000000")  # Trainer name (RANDO)
            offset += 8

            rom[offset:offset + 17] = bytes.fromhex("0000000000000000000000000000000000")  # Padding
            offset += 17

    return rom
