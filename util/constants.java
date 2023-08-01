package util;

import java.util.HashMap;
import java.util.ArrayList;

public class constants {
    private ArrayList<HashMap<String, String>> kantoDex = new ArrayList<HashMap<String, String>>(151);
    private HashMap<String, int[]> kantoAttackDex = new HashMap<String, int[]>();
    private double[][] statDistributionArray = {
        {16.5, 38, 54.5, 68, 79.5, 90, 100},
        {13.5, 29, 48, 63.5, 77, 89, 100},
        {12, 25, 40.5, 59.5, 75, 88, 100},
        {11, 23, 36.5, 52, 71, 86.5, 100},
        {10, 20.5, 32, 45.5, 62, 83.5, 100}
    };

    public HashMap<String, String> getPokemon(int index) {
        return this.kantoDex.get(index);
    }

    public double[] getStatDistribution(int index) {
        return this.statDistributionArray[index];
    }

    public int[] getAtkPool(String keyString) {
        return this.kantoAttackDex.get(keyString);
    }

    public constants() {
        for (int i = 0; i < 151; i++) {
            HashMap<String, String> element = new HashMap<String, String>();
            this.kantoDex.add(i, element);
        }

        this.kantoDex.get(0).put("name", "BULBASAUR");
        this.kantoDex.get(0).put("type", "1603");
        this.kantoDex.get(0).put("exp", "117360");
        
        this.kantoDex.get(1).put("name", "IVYSAUR");
        this.kantoDex.get(1).put("type", "1603");
        this.kantoDex.get(1).put("exp", "117360");
        
        this.kantoDex.get(2).put("name", "VENUSAUR");
        this.kantoDex.get(2).put("type", "1603");
        this.kantoDex.get(2).put("exp", "117360");
        
        this.kantoDex.get(3).put("name", "CHARMANDER");
        this.kantoDex.get(3).put("type", "1414");
        this.kantoDex.get(3).put("exp", "117360");

        this.kantoDex.get(4).put("name", "CHARMELEON");
        this.kantoDex.get(4).put("type", "1414");
        this.kantoDex.get(4).put("exp", "117360");

        this.kantoDex.get(5).put("name", "CHARIZARD");
        this.kantoDex.get(5).put("type", "1402");
        this.kantoDex.get(5).put("exp", "117360");
        
        this.kantoDex.get(6).put("name", "SQUIRTLE");
        this.kantoDex.get(6).put("type", "1402");
        this.kantoDex.get(6).put("exp", "117360");
        
        this.kantoDex.get(7).put("name", "WARTORTLE");
        this.kantoDex.get(7).put("type", "1402");
        this.kantoDex.get(7).put("exp", "117360");
        
        this.kantoDex.get(8).put("name", "BLASTOISE");
        this.kantoDex.get(8).put("type", "1402");
        this.kantoDex.get(8).put("exp", "117360");
        
        this.kantoDex.get(9).put("name", "CATERPIE");
        this.kantoDex.get(9).put("type", "0707");
        this.kantoDex.get(9).put("exp", "125000");
        
        this.kantoDex.get(10).put("name", "METAPOD");
        this.kantoDex.get(10).put("type", "0707");
        this.kantoDex.get(10).put("exp", "125000");
        
        this.kantoDex.get(11).put("name", "BUTTERFREE");
        this.kantoDex.get(11).put("type", "0707");
        this.kantoDex.get(11).put("exp", "125000");
        
        this.kantoDex.get(12).put("name", "WEEDLE");
        this.kantoDex.get(12).put("type", "0703");
        this.kantoDex.get(12).put("exp", "125000");
        
        this.kantoDex.get(13).put("name", "KAKUNA");
        this.kantoDex.get(13).put("type", "0703");
        this.kantoDex.get(13).put("exp", "125000");
        
        this.kantoDex.get(14).put("name", "BEEDRILL");
        this.kantoDex.get(14).put("type", "0703");
        this.kantoDex.get(14).put("exp", "125000");
        
        this.kantoDex.get(15).put("name", "PIDGEY");
        this.kantoDex.get(15).put("type", "0002");
        this.kantoDex.get(15).put("exp", "117360");
        
        this.kantoDex.get(16).put("name", "PIDGEOTTO");
        this.kantoDex.get(16).put("type", "0002");
        this.kantoDex.get(16).put("exp", "117360");
        
        this.kantoDex.get(17).put("name", "PIDGEOT");
        this.kantoDex.get(17).put("type", "0002");
        this.kantoDex.get(17).put("exp", "117360");
        
        this.kantoDex.get(18).put("name", "RATTATA");
        this.kantoDex.get(18).put("type", "0000");
        this.kantoDex.get(18).put("exp", "125000");
        
        this.kantoDex.get(19).put("name", "RATICATE");
        this.kantoDex.get(19).put("type", "0000");
        this.kantoDex.get(19).put("exp", "125000");
        
        this.kantoDex.get(20).put("name", "SPEAROW");
        this.kantoDex.get(20).put("type", "0002");
        this.kantoDex.get(20).put("exp", "125000");
        
        this.kantoDex.get(21).put("name", "FEAROW");
        this.kantoDex.get(21).put("type", "0002");
        this.kantoDex.get(21).put("exp", "125000");
        
        this.kantoDex.get(22).put("name", "EKANS");
        this.kantoDex.get(22).put("type", "0303");
        this.kantoDex.get(22).put("exp", "125000");
        
        this.kantoDex.get(23).put("name", "ARBOK");
        this.kantoDex.get(23).put("type", "0303");
        this.kantoDex.get(23).put("exp", "125000");
        
        this.kantoDex.get(24).put("name", "PIKACHU");
        this.kantoDex.get(24).put("type", "1717");
        this.kantoDex.get(24).put("exp", "125000");
        
        this.kantoDex.get(25).put("name", "RAICHU");
        this.kantoDex.get(25).put("type", "1717");
        this.kantoDex.get(25).put("exp", "125000");
        
        this.kantoDex.get(26).put("name", "SANDSHREW");
        this.kantoDex.get(26).put("type", "0404");
        this.kantoDex.get(26).put("exp", "125000");
        
        this.kantoDex.get(27).put("name", "SANDSLASH");
        this.kantoDex.get(27).put("type", "0404");
        this.kantoDex.get(27).put("exp", "125000");
        
        this.kantoDex.get(28).put("name", "NIDORAN");
        this.kantoDex.get(28).put("type", "0303");
        this.kantoDex.get(28).put("exp", "117360");
        
        this.kantoDex.get(29).put("name", "NIDORANA");
        this.kantoDex.get(29).put("type", "0303");
        this.kantoDex.get(29).put("exp", "117360");
        
        this.kantoDex.get(30).put("name", "NIDOQUEEN");
        this.kantoDex.get(30).put("type", "0304");
        this.kantoDex.get(30).put("exp", "117360");
        
        this.kantoDex.get(31).put("name", "NIDORAN");
        this.kantoDex.get(31).put("type", "0303");
        this.kantoDex.get(31).put("exp", "117360");
        
        this.kantoDex.get(32).put("name", "NIDORANO");
        this.kantoDex.get(32).put("type", "0303");
        this.kantoDex.get(32).put("exp", "117360");
        
        this.kantoDex.get(33).put("name", "NIDOKING");
        this.kantoDex.get(33).put("type", "0304");
        this.kantoDex.get(33).put("exp", "117360");
        
        this.kantoDex.get(34).put("name", "CLEFAIRY");
        this.kantoDex.get(34).put("type", "0000");
        this.kantoDex.get(34).put("exp", "100000");
        
        this.kantoDex.get(35).put("name", "CLEFABLE");
        this.kantoDex.get(35).put("type", "0000");
        this.kantoDex.get(35).put("exp", "100000");
        
        this.kantoDex.get(36).put("name", "VULPIX");
        this.kantoDex.get(36).put("type", "1414");
        this.kantoDex.get(36).put("exp", "125000");
        
        this.kantoDex.get(37).put("name", "NINETAILS");
        this.kantoDex.get(37).put("type", "1414");
        this.kantoDex.get(37).put("exp", "125000");
        
        this.kantoDex.get(38).put("name", "JIGGLYPUFF");
        this.kantoDex.get(38).put("type", "0000");
        this.kantoDex.get(38).put("exp", "100000");
        
        this.kantoDex.get(39).put("name", "WIGGLYTUFF");
        this.kantoDex.get(39).put("type", "0000");
        this.kantoDex.get(39).put("exp", "100000");
        
        this.kantoDex.get(40).put("name", "ZUBAT");
        this.kantoDex.get(40).put("type", "0302");
        this.kantoDex.get(40).put("exp", "125000");
        
        this.kantoDex.get(41).put("name", "GOLBAT");
        this.kantoDex.get(41).put("type", "0302");
        this.kantoDex.get(41).put("exp", "125000");
        
        this.kantoDex.get(42).put("name", "ODDISH");
        this.kantoDex.get(42).put("type", "1603");
        this.kantoDex.get(42).put("exp", "117360");
        
        this.kantoDex.get(43).put("name", "GLOOM");
        this.kantoDex.get(43).put("type", "1603");
        this.kantoDex.get(43).put("exp", "117360");
        
        this.kantoDex.get(44).put("name", "VILEPLUME");
        this.kantoDex.get(44).put("type", "1603");
        this.kantoDex.get(44).put("exp", "117360");
        
        this.kantoDex.get(45).put("name", "PARAS");
        this.kantoDex.get(45).put("type", "0716");
        this.kantoDex.get(45).put("exp", "125000");
        
        this.kantoDex.get(46).put("name", "PARASECT");
        this.kantoDex.get(46).put("type", "0716");
        this.kantoDex.get(46).put("exp", "125000");
        
        this.kantoDex.get(47).put("name", "VENONAT");
        this.kantoDex.get(47).put("type", "0703");
        this.kantoDex.get(47).put("exp", "125000");
        
        this.kantoDex.get(48).put("name", "VENOMOTH");
        this.kantoDex.get(48).put("type", "0703");
        this.kantoDex.get(48).put("exp", "125000");
        
        this.kantoDex.get(49).put("name", "DIGLETT");
        this.kantoDex.get(49).put("type", "0404");
        this.kantoDex.get(49).put("exp", "125000");
        
        this.kantoDex.get(50).put("name", "DUGTRIO");
        this.kantoDex.get(50).put("type", "0404");
        this.kantoDex.get(50).put("exp", "125000");
        
        this.kantoDex.get(51).put("name", "MEOWTH");
        this.kantoDex.get(51).put("type", "0000");
        this.kantoDex.get(51).put("exp", "125000");
        
        this.kantoDex.get(52).put("name", "PERSIAN");
        this.kantoDex.get(52).put("type", "0000");
        this.kantoDex.get(52).put("exp", "125000");
        
        this.kantoDex.get(53).put("name", "PSYDUCK");
        this.kantoDex.get(53).put("type", "1515");
        this.kantoDex.get(53).put("exp", "125000");
        
        this.kantoDex.get(54).put("name", "GOLDUCK");
        this.kantoDex.get(54).put("type", "1515");
        this.kantoDex.get(54).put("exp", "125000");
        
        this.kantoDex.get(55).put("name", "MANKEY");
        this.kantoDex.get(55).put("type", "0101");
        this.kantoDex.get(55).put("exp", "125000");
        
        this.kantoDex.get(56).put("name", "PRIMEAPE");
        this.kantoDex.get(56).put("type", "0101");
        this.kantoDex.get(56).put("exp", "125000");
        
        this.kantoDex.get(57).put("name", "GROWLITHE");
        this.kantoDex.get(57).put("type", "1414");
        this.kantoDex.get(57).put("exp", "156250");
        
        this.kantoDex.get(58).put("name", "ARCANINE");
        this.kantoDex.get(58).put("type", "1414");
        this.kantoDex.get(58).put("exp", "156250");
        
        this.kantoDex.get(59).put("name", "POLIWAG");
        this.kantoDex.get(59).put("type", "1515");
        this.kantoDex.get(59).put("exp", "117360");
        
        this.kantoDex.get(60).put("name", "POLIWHIRL");
        this.kantoDex.get(60).put("type", "1515");
        this.kantoDex.get(60).put("exp", "117360");
        
        this.kantoDex.get(61).put("name", "POLIWRATH");
        this.kantoDex.get(61).put("type", "1501");
        this.kantoDex.get(61).put("exp", "117360");
        
        this.kantoDex.get(62).put("name", "ABRA");
        this.kantoDex.get(62).put("type", "1818");
        this.kantoDex.get(62).put("exp", "117360");
        
        this.kantoDex.get(63).put("name", "KADABRA");
        this.kantoDex.get(63).put("type", "1818");
        this.kantoDex.get(63).put("exp", "117360");
        
        this.kantoDex.get(64).put("name", "ALAKAZAM");
        this.kantoDex.get(64).put("type", "1818");
        this.kantoDex.get(64).put("exp", "117360");
        
        this.kantoDex.get(65).put("name", "MACHOP");
        this.kantoDex.get(65).put("type", "0101");
        this.kantoDex.get(65).put("exp", "117360");
        
        this.kantoDex.get(66).put("name", "MACHOKE");
        this.kantoDex.get(66).put("type", "0101");
        this.kantoDex.get(66).put("exp", "117360");
        
        this.kantoDex.get(67).put("name", "MACHAMP");
        this.kantoDex.get(67).put("type", "0101");
        this.kantoDex.get(67).put("exp", "117360");
        
        this.kantoDex.get(68).put("name", "BELLSPROUT");
        this.kantoDex.get(68).put("type", "1603");
        this.kantoDex.get(68).put("exp", "117360");
        
        this.kantoDex.get(69).put("name", "WEEPINBELL");
        this.kantoDex.get(69).put("type", "1603");
        this.kantoDex.get(69).put("exp", "117360");
        
        this.kantoDex.get(70).put("name", "VICTREEBEL");
        this.kantoDex.get(70).put("type", "1603");
        this.kantoDex.get(70).put("exp", "117360");
        
        this.kantoDex.get(71).put("name", "TENTACOOL");
        this.kantoDex.get(71).put("type", "1503");
        this.kantoDex.get(71).put("exp", "156250");
        
        this.kantoDex.get(72).put("name", "TENTACRUEL");
        this.kantoDex.get(72).put("type", "1503");
        this.kantoDex.get(72).put("exp", "156250");
        
        this.kantoDex.get(73).put("name", "GEODUDE");
        this.kantoDex.get(73).put("type", "0504");
        this.kantoDex.get(73).put("exp", "117360");
        
        this.kantoDex.get(74).put("name", "GRAVELER");
        this.kantoDex.get(74).put("type", "0504");
        this.kantoDex.get(74).put("exp", "117360");
        
        this.kantoDex.get(75).put("name", "GOLEM");
        this.kantoDex.get(75).put("type", "0504");
        this.kantoDex.get(75).put("exp", "117360");
        
        this.kantoDex.get(76).put("name", "PONYTA");
        this.kantoDex.get(76).put("type", "1414");
        this.kantoDex.get(76).put("exp", "125000");
        
        this.kantoDex.get(77).put("name", "RAPIDASH");
        this.kantoDex.get(77).put("type", "1414");
        this.kantoDex.get(77).put("exp", "125000");
        
        this.kantoDex.get(78).put("name", "SLOWPOKE");
        this.kantoDex.get(78).put("type", "1518");
        this.kantoDex.get(78).put("exp", "125000");
        
        this.kantoDex.get(79).put("name", "SLOWBRO");
        this.kantoDex.get(79).put("type", "1518");
        this.kantoDex.get(79).put("exp", "125000");
        
        this.kantoDex.get(80).put("name", "MAGNEMITE");
        this.kantoDex.get(80).put("type", "1717");
        this.kantoDex.get(80).put("exp", "125000");
        
        this.kantoDex.get(81).put("name", "MAGNETON");
        this.kantoDex.get(81).put("type", "1717");
        this.kantoDex.get(81).put("exp", "125000");
        
        this.kantoDex.get(82).put("name", "FARFETCH'D");
        this.kantoDex.get(82).put("type", "0002");
        this.kantoDex.get(82).put("exp", "125000");
        
        this.kantoDex.get(83).put("name", "DODUO");
        this.kantoDex.get(83).put("type", "0002");
        this.kantoDex.get(83).put("exp", "125000");
        
        this.kantoDex.get(84).put("name", "DODRIO");
        this.kantoDex.get(84).put("type", "0002");
        this.kantoDex.get(84).put("exp", "125000");
        
        this.kantoDex.get(85).put("name", "SEEL");
        this.kantoDex.get(85).put("type", "1515");
        this.kantoDex.get(85).put("exp", "125000");
        
        this.kantoDex.get(86).put("name", "DEWGONG");
        this.kantoDex.get(86).put("type", "1519");
        this.kantoDex.get(86).put("exp", "125000");
        
        this.kantoDex.get(87).put("name", "GRIMER");
        this.kantoDex.get(87).put("type", "0303");
        this.kantoDex.get(87).put("exp", "125000");
        
        this.kantoDex.get(88).put("name", "MUK");
        this.kantoDex.get(88).put("type", "0303");
        this.kantoDex.get(88).put("exp", "125000");
        
        this.kantoDex.get(89).put("name", "SHELLDER");
        this.kantoDex.get(89).put("type", "1515");
        this.kantoDex.get(89).put("exp", "156250");
        
        this.kantoDex.get(90).put("name", "CLOYSTER");
        this.kantoDex.get(90).put("type", "1519");
        this.kantoDex.get(90).put("exp", "156250");
        
        this.kantoDex.get(91).put("name", "GASTLY");
        this.kantoDex.get(91).put("type", "0803");
        this.kantoDex.get(91).put("exp", "117360");
        
        this.kantoDex.get(92).put("name", "HAUNTER");
        this.kantoDex.get(92).put("type", "0803");
        this.kantoDex.get(92).put("exp", "117360");
        
        this.kantoDex.get(93).put("name", "GENGAR");
        this.kantoDex.get(93).put("type", "0803");
        this.kantoDex.get(93).put("exp", "117360");
        
        this.kantoDex.get(94).put("name", "ONIX");
        this.kantoDex.get(94).put("type", "0504");
        this.kantoDex.get(94).put("exp", "125000");
        
        this.kantoDex.get(95).put("name", "DROWZEE");
        this.kantoDex.get(95).put("type", "1818");
        this.kantoDex.get(95).put("exp", "125000");
        
        this.kantoDex.get(96).put("name", "HYPNO");
        this.kantoDex.get(96).put("type", "1818");
        this.kantoDex.get(96).put("exp", "125000");
        
        this.kantoDex.get(97).put("name", "KRABBY");
        this.kantoDex.get(97).put("type", "1515");
        this.kantoDex.get(97).put("exp", "125000");
        
        this.kantoDex.get(98).put("name", "KINGLER");
        this.kantoDex.get(98).put("type", "1515");
        this.kantoDex.get(98).put("exp", "125000");
        
        this.kantoDex.get(99).put("name", "VOLTROB");
        this.kantoDex.get(99).put("type", "1717");
        this.kantoDex.get(99).put("exp", "125000");
        
        this.kantoDex.get(100).put("name", "ELECTRODE");
        this.kantoDex.get(100).put("type", "1717");
        this.kantoDex.get(100).put("exp", "125000");
        
        this.kantoDex.get(101).put("name", "EXEGGCUTE");
        this.kantoDex.get(101).put("type", "1618");
        this.kantoDex.get(101).put("exp", "156250");
        
        this.kantoDex.get(102).put("name", "EXEGGUTOR");
        this.kantoDex.get(102).put("type", "1618");
        this.kantoDex.get(102).put("exp", "156250");
        
        this.kantoDex.get(103).put("name", "CUBONE");
        this.kantoDex.get(103).put("type", "0404");
        this.kantoDex.get(103).put("exp", "125000");
        
        this.kantoDex.get(104).put("name", "MAROWAK");
        this.kantoDex.get(104).put("type", "0404");
        this.kantoDex.get(104).put("exp", "125000");
        
        this.kantoDex.get(105).put("name", "HITMONLEE");
        this.kantoDex.get(105).put("type", "0101");
        this.kantoDex.get(105).put("exp", "125000");
        
        this.kantoDex.get(106).put("name", "HITMONCHAN");
        this.kantoDex.get(106).put("type", "0101");
        this.kantoDex.get(106).put("exp", "125000");
        
        this.kantoDex.get(107).put("name", "LICKITUNG");
        this.kantoDex.get(107).put("type", "0000");
        this.kantoDex.get(107).put("exp", "125000");
        
        this.kantoDex.get(108).put("name", "KOFFING");
        this.kantoDex.get(108).put("type", "0303");
        this.kantoDex.get(108).put("exp", "125000");
        
        this.kantoDex.get(109).put("name", "WEEZING");
        this.kantoDex.get(109).put("type", "0303");
        this.kantoDex.get(109).put("exp", "125000");
        
        this.kantoDex.get(110).put("name", "RHYHORN");
        this.kantoDex.get(110).put("type", "0405");
        this.kantoDex.get(110).put("exp", "156250");
        
        this.kantoDex.get(111).put("name", "RHYDON");
        this.kantoDex.get(111).put("type", "0405");
        this.kantoDex.get(111).put("exp", "156250");
        
        this.kantoDex.get(112).put("name", "CHANSEY");
        this.kantoDex.get(112).put("type", "0000");
        this.kantoDex.get(112).put("exp", "100000");
        
        this.kantoDex.get(113).put("name", "TANGELA");
        this.kantoDex.get(113).put("type", "1616");
        this.kantoDex.get(113).put("exp", "125000");
        
        this.kantoDex.get(114).put("name", "KANGASKHAN");
        this.kantoDex.get(114).put("type", "0000");
        this.kantoDex.get(114).put("exp", "125000");
        
        this.kantoDex.get(115).put("name", "HORSEA");
        this.kantoDex.get(115).put("type", "1515");
        this.kantoDex.get(115).put("exp", "125000");
        
        this.kantoDex.get(116).put("name", "SEADRA");
        this.kantoDex.get(116).put("type", "1515");
        this.kantoDex.get(116).put("exp", "125000");
        
        this.kantoDex.get(117).put("name", "GOLDEEN");
        this.kantoDex.get(117).put("type", "1515");
        this.kantoDex.get(117).put("exp", "125000");
        
        this.kantoDex.get(118).put("name", "SEAKING");
        this.kantoDex.get(118).put("type", "1515");
        this.kantoDex.get(118).put("exp", "125000");
        
        this.kantoDex.get(119).put("name", "STARYU");
        this.kantoDex.get(119).put("type", "1515");
        this.kantoDex.get(119).put("exp", "156250");
        
        this.kantoDex.get(120).put("name", "STARMIE");
        this.kantoDex.get(120).put("type", "1518");
        this.kantoDex.get(120).put("exp", "156250");
        
        this.kantoDex.get(121).put("name", "MR. MIME");
        this.kantoDex.get(121).put("type", "1818");
        this.kantoDex.get(121).put("exp", "125000");
        
        this.kantoDex.get(122).put("name", "SCYTHER");
        this.kantoDex.get(122).put("type", "0702");
        this.kantoDex.get(122).put("exp", "125000");
        
        this.kantoDex.get(123).put("name", "JYNX");
        this.kantoDex.get(123).put("type", "1918");
        this.kantoDex.get(123).put("exp", "125000");
        
        this.kantoDex.get(124).put("name", "ELECTABUZZ");
        this.kantoDex.get(124).put("type", "1717");
        this.kantoDex.get(124).put("exp", "125000");
        
        this.kantoDex.get(125).put("name", "MAGMAR");
        this.kantoDex.get(125).put("type", "1414");
        this.kantoDex.get(125).put("exp", "125000");
        
        this.kantoDex.get(126).put("name", "PINSIR");
        this.kantoDex.get(126).put("type", "0707");
        this.kantoDex.get(126).put("exp", "156250");
        
        this.kantoDex.get(127).put("name", "TAUROS");
        this.kantoDex.get(127).put("type", "0000");
        this.kantoDex.get(127).put("exp", "156250");
        
        this.kantoDex.get(128).put("name", "MAGIKARP");
        this.kantoDex.get(128).put("type", "1515");
        this.kantoDex.get(128).put("exp", "156250");
        
        this.kantoDex.get(129).put("name", "GYARADOS");
        this.kantoDex.get(129).put("type", "1502");
        this.kantoDex.get(129).put("exp", "156250");
        
        this.kantoDex.get(130).put("name", "LAPRAS");
        this.kantoDex.get(130).put("type", "1519");
        this.kantoDex.get(130).put("exp", "156250");
        
        this.kantoDex.get(131).put("name", "DITTO");
        this.kantoDex.get(131).put("type", "0000");
        this.kantoDex.get(131).put("exp", "125000");
        
        this.kantoDex.get(132).put("name", "EEVEE");
        this.kantoDex.get(132).put("type", "0000");
        this.kantoDex.get(132).put("exp", "125000");
        
        this.kantoDex.get(133).put("name", "VAPOREON");
        this.kantoDex.get(133).put("type", "1515");
        this.kantoDex.get(133).put("exp", "125000");
        
        this.kantoDex.get(134).put("name", "JOLTEON");
        this.kantoDex.get(134).put("type", "1717");
        this.kantoDex.get(134).put("exp", "125000");
        
        this.kantoDex.get(135).put("name", "FLAREON");
        this.kantoDex.get(135).put("type", "1414");
        this.kantoDex.get(135).put("exp", "125000");
        
        this.kantoDex.get(136).put("name", "PORYGON");
        this.kantoDex.get(136).put("type", "0000");
        this.kantoDex.get(136).put("exp", "125000");
        
        this.kantoDex.get(137).put("name", "OMANYTE");
        this.kantoDex.get(137).put("type", "0515");
        this.kantoDex.get(137).put("exp", "125000");
        
        this.kantoDex.get(138).put("name", "OMASTAR");
        this.kantoDex.get(138).put("type", "0515");
        this.kantoDex.get(138).put("exp", "125000");
        
        this.kantoDex.get(139).put("name", "KABUTO");
        this.kantoDex.get(139).put("type", "0515");
        this.kantoDex.get(139).put("exp", "125000");
        
        this.kantoDex.get(140).put("name", "KABUTOPS");
        this.kantoDex.get(140).put("type", "0515");
        this.kantoDex.get(140).put("exp", "125000");
        
        this.kantoDex.get(141).put("name", "AERODACTYL");
        this.kantoDex.get(141).put("type", "0502");
        this.kantoDex.get(141).put("exp", "156250");
        
        this.kantoDex.get(142).put("name", "SNORLAX");
        this.kantoDex.get(142).put("type", "0000");
        this.kantoDex.get(142).put("exp", "156250");
        
        this.kantoDex.get(143).put("name", "ARTICUNO");
        this.kantoDex.get(143).put("type", "1902");
        this.kantoDex.get(143).put("exp", "156250");
        
        this.kantoDex.get(144).put("name", "ZAPDOS");
        this.kantoDex.get(144).put("type", "1702");
        this.kantoDex.get(144).put("exp", "156250");
        
        this.kantoDex.get(145).put("name", "MOLTRES");
        this.kantoDex.get(145).put("type", "1402");
        this.kantoDex.get(145).put("exp", "156250");
        
        this.kantoDex.get(146).put("name", "DRATINI");
        this.kantoDex.get(146).put("type", "1A1A");
        this.kantoDex.get(146).put("exp", "156250");
        
        this.kantoDex.get(147).put("name", "DRAGONAIR");
        this.kantoDex.get(147).put("type", "1A1A");
        this.kantoDex.get(147).put("exp", "156250");
        
        this.kantoDex.get(148).put("name", "DRAGONITE");
        this.kantoDex.get(148).put("type", "1A1A");
        this.kantoDex.get(148).put("exp", "156250");
        
        this.kantoDex.get(149).put("name", "MEWTWO");
        this.kantoDex.get(149).put("type", "1818");
        this.kantoDex.get(149).put("exp", "156250");
        
        this.kantoDex.get(150).put("name", "MEW");
        this.kantoDex.get(150).put("type", "1818");
        this.kantoDex.get(150).put("exp", "117360");

        this.kantoAttackDex.put("PHY1", new int[]{34, 89, 163});
        this.kantoAttackDex.put("PHY2", new int[]{38, 63, 65, 70, 136, 155, 161});
        this.kantoAttackDex.put("PHY3", new int[]{23, 24, 25, 26, 29, 30, 36, 37, 44, 66, 120, 124, 146, 153, 157, 158});
        this.kantoAttackDex.put("PHY4", new int[]{2, 4, 5, 11, 15, 21, 27, 41, 67, 69, 91, 101, 121, 125, 129, 131, 143, 154, 162});
        this.kantoAttackDex.put("PHY5", new int[]{1, 3, 6, 10, 16, 17, 20, 31, 33, 35, 42, 51, 64, 88, 98, 117, 130, 140});
        this.kantoAttackDex.put("PHY6", new int[]{13, 19, 40, 49, 99, 122, 123, 132, 141, 68});
        this.kantoAttackDex.put("PHY7", new int[]{68});
        this.kantoAttackDex.put("SPE1", new int[]{53, 57, 58, 85, 94, 59});
        this.kantoAttackDex.put("SPE2", new int[]{87, 126, 7, 8, 9});
        this.kantoAttackDex.put("SPE3", new int[]{56, 127, 128, 152});
        this.kantoAttackDex.put("SPE4", new int[]{60, 61, 62, 75, 76, 80, 93});
        this.kantoAttackDex.put("SPE5", new int[]{138, 149, 55, 72, 83, 84});
        this.kantoAttackDex.put("SPE6", new int[]{52, 145});
        this.kantoAttackDex.put("SPE7", new int[]{22, 71, 82});
        this.kantoAttackDex.put("STA1", new int[]{86, 147});
        this.kantoAttackDex.put("STA2", new int[]{79, 142});
        this.kantoAttackDex.put("STA3", new int[]{47, 78, 95, 97, 109, 133, 137, 156});
        this.kantoAttackDex.put("STA4", new int[]{14, 28, 48, 74, 77, 92, 103, 104, 105, 107, 108, 112, 113, 114, 115, 116, 134, 135, 139, 151, 164});
        this.kantoAttackDex.put("STA5", new int[]{12, 32, 39, 43, 45, 50, 54, 81, 90, 96, 106, 110, 111, 148, 159});
        this.kantoAttackDex.put("STA6", new int[]{73, 102, 118, 119, 144, 160});
        this.kantoAttackDex.put("STA7", new int[]{18, 46, 100, 150});
    }
}
