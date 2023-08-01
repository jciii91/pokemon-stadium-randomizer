package randomizer;

import java.util.Random;
import java.util.stream.IntStream;
import java.lang.Math;

public final class baseStatsRandomizer {
    private baseStatsRandomizer() {}

    private final static int[] MIN_BASE_PERCENT = {15, 15, 15, 15, 15};
    private final static int[] MAX_BASE_PERCENT = {43, 43, 43, 43, 43};

    public static int[] randomizeBaseStats(int[] baseStats) {
        int bst = IntStream.of(baseStats).sum();
        int[] newBaseStats;
        int remainingPercentage;
        Random r = new Random();

        while (true) {
            newBaseStats = new int[5];
            remainingPercentage = 100;
            for (int i = 0; i < 4; i++) {
                int bstPercentage;
                if (remainingPercentage > MIN_BASE_PERCENT[i]) {
                    if (remainingPercentage < MAX_BASE_PERCENT[i]) {
                        bstPercentage = r.nextInt(remainingPercentage-MIN_BASE_PERCENT[i]) + MIN_BASE_PERCENT[i];
                    }
                    else {
                        bstPercentage = r.nextInt(MAX_BASE_PERCENT[i]-MIN_BASE_PERCENT[i]) + MIN_BASE_PERCENT[i];
                    }
                }
                else {
                    bstPercentage = MIN_BASE_PERCENT[i];
                }
                newBaseStats[i] = (int)Math.floor(bst * ((double)bstPercentage/100));
                remainingPercentage = remainingPercentage - bstPercentage;
            }
            if (MAX_BASE_PERCENT[4] >= remainingPercentage && remainingPercentage >= MIN_BASE_PERCENT[4]) {
                newBaseStats[4] = bst - IntStream.of(newBaseStats).sum();
                break;
            }
        }

        for (int j = newBaseStats.length - 1; j > 0; j--) {
            int index = r.nextInt(j + 1);
            int temp = newBaseStats[index];
            newBaseStats[index] = newBaseStats[j];
            newBaseStats[j] = temp;
        }

        return newBaseStats;
    }
}
