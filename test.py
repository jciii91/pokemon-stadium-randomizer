import stadium_randomizer

def main():
    settings_dict = {
        "version" : 'US_1.0',
        "base_stats" : 1,
        "rentals_round1" : 1,
        "gymcastle_round1" : 1
    }
    with open("C:\\Users\\jcost\\Documents\\games\\PKStadium1-0US.z64", "rb") as file:
        binary_data = bytearray(file.read())

    rom = stadium_randomizer.randomizer_func(binary_data, settings_dict)

    with open("1-0_reg_support.z64", "wb") as file:
        file.write(rom)  # Writes the raw binary data back

if __name__ == "__main__":
    main()
