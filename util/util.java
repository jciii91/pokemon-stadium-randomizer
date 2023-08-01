package util;

import java.util.HexFormat;
import java.util.concurrent.ThreadLocalRandom;
import java.lang.Math;

public class util {
    public static int[] randomSetOfInts(int size, int min, int max) {
        int[] returnArray = new int[size];
        for (int i = 0; i < size; i++) {
            returnArray[i] = ThreadLocalRandom.current().nextInt(min, max + 1);
        }
        return returnArray;
    }

    public static String randomHexString(int length) {
        String hexString = "";
        int[] intValues = randomSetOfInts(length, 0, 15);
        for (int number : intValues) {
            hexString += Integer.toHexString(number);
        }
        return hexString;
    }

    public static byte[] getDisplayStats(int[] baseStats, int[] evs, String ivStr) {
        int[] ivs = new int[5];
        String binaryIVStr = "";
        int[] displayStats = new int[5];
        
        String binaryPiece;
        for (int i = 0; i < 4; i++) {
            binaryPiece = Integer.toBinaryString(Integer.parseInt(ivStr.substring(i, i+1), 16));
            binaryIVStr += String.format("%4s", binaryPiece).replace(' ', '0');
        }

        for (int i = 1; i < 4; i++) {
            int iv = Integer.parseInt(binaryIVStr.substring(i * 4, (i * 4 + 4)), 2);
            ivs[i] = iv;
            if (iv % 2 != 0)
                ivs[0] = (int)ivs[0] + (int)Math.pow(2, 3 - i);
        }

        displayStats[0] = ((((baseStats[0] + ivs[0]) * 2 + (int)Math.ceil(Math.sqrt(evs[0]) / 4)) * 50)/100) + 50 + 10;
        for (int i = 1; i < 5; i++)
            displayStats[i] = ((((baseStats[i] + ivs[i]) * 2 + (int)Math.ceil(Math.sqrt(evs[i]) / 4)) * 50)/100) + 5;

        String hexString = "";
        for (int number : displayStats) {
            String holder = Integer.toHexString(number);
            hexString += String.format("%4s", holder).replace(' ', '0');
        }

        return HexFormat.of().parseHex(hexString);
    }
}
