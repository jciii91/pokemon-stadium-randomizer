package randomizer;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.HexFormat;

import util.constants;

public class randomizer {
    private String exePath = "n64-checksum.exe";
    private Path rom;
    private Path output;

    public randomizer(String inputROM, String outputPath) {
        this.rom = new File(inputROM).toPath();
        this.output = new File(outputPath + "/PKseed.z64").toPath();
    }

    public void Randomize() throws IOException {
        Files.copy(rom, output, StandardCopyOption.REPLACE_EXISTING);
        RandomAccessFile raf = new RandomAccessFile(output.toString(), "rw");
        constants pokemonDictionary = new util.constants();
        int[][] bstArray = new int[151][5];
        int[][] evs = new int[151][5];
        String[] ivs = new String[151];
        for (int i = 0; i < 151; i++) {
            evs[i] = util.util.randomSetOfInts(5, 0, 65535);
            ivs[i] = util.util.randomHexString(4);
        }

        int position = 59;
        byte[] version = new byte[5];
        String comparisonString = "";
        raf.seek(position);
        raf.read(version);
        for (byte b : version) {
            if (b >= 0)
                    comparisonString += String.format("%02X", b);
                else
                    comparisonString += String.format("%02X", (b & 0xFF));
        }
        String USA_V1_0 = "4E504F4500";
        boolean versionOffset = (comparisonString.equals(USA_V1_0));

        position = versionOffset ? 465825 : 466337;
        raf.seek(position);
        byte[] bstBytes = new byte[5];
        for (int bstIndex = 0; bstIndex < 151; bstIndex++) {
            raf.read(bstBytes);
            raf.seek(position);

            int[] intArray = new int[5];
            for (int i = 0; i < 5; i++) {
                if (bstBytes[i] >= 0)
                    intArray[i] = bstBytes[i];
                else
                    intArray[i] = bstBytes[i] & 0xFF;
            }

            intArray = baseStatsRandomizer.randomizeBaseStats(intArray);
            for (int i = 0; i < 5; i++) {
                bstArray[bstIndex][i] = intArray[i];
                //raf.write(HexFormat.of().parseHex(String.format("%02X", intArray[i])));
            }

            position += 23;
            raf.seek(position);
        }

        position = versionOffset ? 9057228 : 8917964;
        raf.seek(position);
        for (int i = 0; i < 10; i++) {
            int teamCount = i < 9 ? 4 : 7;
            for (int j = 0; j < teamCount; j++) {
                int[] newTeam = util.util.randomSetOfInts(6, 0, 149);
                for (int k = 0; k < 6; k++) {
                    int pokemonIndex = newTeam[k];
                    raf.write((pokemonIndex+1));
                    raf.seek(position + 6);
                    
                    String newType = pokemonDictionary.getPokemon(pokemonIndex).get("type");
                    raf.write(HexFormat.of().parseHex(newType));
                    raf.seek(position + 9);

                    int[] newAttacks = movesetGenerator.getRandomMoveset(bstArray[pokemonIndex]);
                    for (int l = 0; l < 4; l++) {
                        raf.write(HexFormat.of().parseHex(String.format("%02X", newAttacks[l])));
                    }
                    raf.seek(position + 17);

                    int exp = Integer.parseInt(pokemonDictionary.getPokemon(pokemonIndex).get("exp"));
                    raf.write(HexFormat.of().parseHex(String.format("%06X", exp)));
                    raf.seek(position + 20);
                    
                    for (int l = 0; l < 5; l++) {
                        raf.seek(position + 20 + l*2);
                        raf.write(evs[pokemonIndex][l]);
                    }
                    raf.seek(position + 30);
                    
                    raf.write(HexFormat.of().parseHex(ivs[pokemonIndex]));
                    raf.seek(position + 38);

                    raf.write(util.util.getDisplayStats(bstArray[pokemonIndex], evs[pokemonIndex], ivs[pokemonIndex]));
                    raf.seek(position + 48);

                    String pokemonName = pokemonDictionary.getPokemon(pokemonIndex).get("name");
                    raf.write(pokemonName.getBytes());
                    // check if a Nidoran is being written in to add their gender symbol
                    if (pokemonIndex == 28)
                        raf.write(HexFormat.of().parseHex("BE"));
                    else if (pokemonIndex == 31)
                        raf.write(HexFormat.of().parseHex("A9"));
                    pokemonName += " ";
                    if (pokemonName.length() < 10) {
                        int blanks = 10 - pokemonName.length();
                        for (int l = 0; l < blanks; l++) {
                            raf.write(HexFormat.of().parseHex("00"));
                        }
                    }
                    position += 84;
                    raf.seek(position);
                }
                position += 56;
                raf.seek(position);
            }
            position += 16;
            raf.seek(position);
        }

        // randomize gym castle rentals
        position = versionOffset ? 9119629 : 8980365;
        for (int j = 0; j < 149; j++) {
            raf.seek(position);
            int[] newAttacks = movesetGenerator.getRandomMoveset(bstArray[j]);
            for (int k = 0; k < 4; k++) {
                raf.write(HexFormat.of().parseHex(String.format("%02X", newAttacks[k])));
            }

            for (int k = 0; k < 5; k++) {
                raf.seek(position + 11 + k*2);
                raf.write(evs[j][k]);
            }
            raf.seek(position + 21);
            
            raf.write(HexFormat.of().parseHex(ivs[j]));
            raf.seek(position + 29);

            raf.write(util.util.getDisplayStats(bstArray[j], evs[j], ivs[j]));

            position += 84;
        }

        raf.close();
        ProcessBuilder checkSum = new ProcessBuilder().command(this.exePath, output.toString());
        checkSum.start();
    }
}
