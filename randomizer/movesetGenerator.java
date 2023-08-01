package randomizer;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.IntStream;

import util.constants;

public class movesetGenerator {
    private static int getRandomMove(String atkType, double[] distribution) {
        String keyStr = "";
        int roll = ThreadLocalRandom.current().nextInt(1, 101);
        constants pokemonDictionary = new util.constants();

        if (roll <= distribution[0])
            keyStr = atkType + "1";
        else if (roll <= distribution[1])
            keyStr = atkType + "2";
        else if (roll <= distribution[2])
            keyStr = atkType + "3";
        else if (roll <= distribution[3])
            keyStr = atkType + "4";
        else if (roll > distribution[4])
            keyStr = atkType + "5";
        else if (roll <= distribution[5])
            keyStr = atkType + "6";
        else if (roll <= distribution[6])
            keyStr = atkType + "7";

        int[] atkPool = pokemonDictionary.getAtkPool(keyStr);
        roll = ThreadLocalRandom.current().nextInt(0, atkPool.length);
        return atkPool[roll];
    }

    public static int[] getRandomMoveset(int[] bstArray) {
        int bst = IntStream.of(bstArray).sum();
        String firstType, secondType, thirdType, fourthType;
        int coinFlip = ThreadLocalRandom.current().nextInt(1, 101);
        int oneInThree = ThreadLocalRandom.current().nextInt(1, 100);
        double[] distribution = new double[7];
        constants pokemonDictionary = new util.constants();

        firstType = bstArray[1] > bstArray[4] ? "PHY" : "SPE";
        
        if (coinFlip <= 50)
            secondType = "PHY";
        else
            secondType = "SPE";
        
        thirdType = "STA";
        
        if (oneInThree <= 33)
            fourthType = "PHY";
        else if (oneInThree <= 66)
            fourthType = "SPE";
        else
            fourthType = "STA";

        String[] attackTypes = {firstType, secondType, thirdType, fourthType};

        if (bst <= 225)
            distribution = pokemonDictionary.getStatDistribution(0);
        else if (bst <= 300)
            distribution = pokemonDictionary.getStatDistribution(1);
        else if (bst <= 375)
            distribution = pokemonDictionary.getStatDistribution(2);
        else if (bst <= 450)
            distribution = pokemonDictionary.getStatDistribution(3);
        else
            distribution = pokemonDictionary.getStatDistribution(4);

        int[] moveset = new int[4];
        int randomMove;
        for (int i = 0; i < 4; i++) {
            randomMove = movesetGenerator.getRandomMove(attackTypes[i], distribution);
            
            for (int j = 0; j < 4; j++) {
                if (moveset[j] == randomMove) {
                    randomMove = movesetGenerator.getRandomMove(attackTypes[i], distribution);
                    j = 0;
                }
            }
            
            moveset[i] = randomMove;
        }

        return moveset;
    }
}
