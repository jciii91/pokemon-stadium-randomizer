import stadium_randomizer

def main():
    settings_dict = {
        "base_stats" : 3,
        "rentals_round1" : 1,
        "gymcastle_round1" : 1
    }
    with open("C:\\Users\\jcost\\Documents\\games\\PKStadium1-0US.z64", "rb") as file:
        binary_data = bytearray(file.read())

    rom = stadium_randomizer.randomizer_func(binary_data, settings_dict)

    with open("base_stats_3.z64", "wb") as file:
        file.write(rom)  # Writes the raw binary data back

if __name__ == "__main__":
    main()
