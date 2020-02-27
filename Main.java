
public class Main {
	static void initMap(Map map)
	{// 10 states
//		map.states.add("North Carolina");
//		map.states.add("South Carolina");
//		map.states.add("Virginia");
//		map.states.add("Tennessee");
//		map.states.add("Kentucky");
//		map.states.add("West Virginia");
//		map.states.add("Georgia");
//		map.states.add("Alabama");
//		map.states.add("Mississippi");
//		map.states.add("Florida");
//
//		map.borders.add(new Border(0, 1));
//		map.borders.add(new Border(0, 2));
//		map.borders.add(new Border(0, 3));
//		map.borders.add(new Border(0, 6));
//		map.borders.add(new Border(1, 6));
//		map.borders.add(new Border(2, 3));
//		map.borders.add(new Border(2, 4));
//		map.borders.add(new Border(2, 5));
//		map.borders.add(new Border(3, 4));
//		map.borders.add(new Border(3, 6));
//		map.borders.add(new Border(3, 7));
//		map.borders.add(new Border(3, 8));
//		map.borders.add(new Border(4, 5));
//		map.borders.add(new Border(6, 7));
//		map.borders.add(new Border(6, 9));
//		map.borders.add(new Border(7, 8));
//		map.borders.add(new Border(7, 9));
//*******************************51 states***************************************************
        map.states.add("AK");//0
        map.borders.add(new Border(0, 1));
        map.states.add("WA");//1
        map.borders.add(new Border(1, 2));
        map.borders.add(new Border(1, 3));
        map.states.add("ID");//2
        map.borders.add(new Border(2, 4));
        map.borders.add(new Border(2, 5));
        map.borders.add(new Border(2, 6));
        map.borders.add(new Border(2, 7));
        map.borders.add(new Border(2, 3));
        map.states.add("OR");//3
        map.borders.add(new Border(3, 7));
        map.borders.add(new Border(3, 8));
        map.states.add("MT");//4
        map.borders.add(new Border(4, 9));
        map.borders.add(new Border(4, 10));
        map.borders.add(new Border(4, 5));
        map.states.add("WY");//5
        map.borders.add(new Border(5, 10));
        map.borders.add(new Border(5, 11));
        map.borders.add(new Border(5, 12));
        map.borders.add(new Border(5, 6));
        map.states.add("UT");//6
        map.borders.add(new Border(6, 12));
        map.borders.add(new Border(6, 13));
        map.borders.add(new Border(6, 14));
        map.borders.add(new Border(6, 7));
        map.states.add("NV");//7
        map.borders.add(new Border(7, 14));
        map.borders.add(new Border(7, 8));
        map.states.add("CA");//8
        map.borders.add(new Border(8, 14));
        map.borders.add(new Border(8, 15));
        map.states.add("ND");//9
        map.borders.add(new Border(9, 16));
        map.borders.add(new Border(9, 10));
        map.states.add("SD");//10
        map.borders.add(new Border(10, 16));
        map.borders.add(new Border(10, 17));
        map.borders.add(new Border(10, 11));
        map.states.add("NE");//11
        map.borders.add(new Border(11, 17));
        map.borders.add(new Border(11, 19));
        map.borders.add(new Border(11, 18));
        map.borders.add(new Border(11, 12));
        map.states.add("CO");//12
        map.borders.add(new Border(12, 19));
        map.borders.add(new Border(12, 20));
        map.borders.add(new Border(12, 13));
        map.borders.add(new Border(12, 14));
        map.states.add("NM");//13
        map.borders.add(new Border(13, 20));
        map.borders.add(new Border(13, 21));
        map.borders.add(new Border(13, 14));
        map.states.add("AZ");//14

        map.states.add("HI");//15

        map.states.add("MN");//16
        map.borders.add(new Border(16, 22));
        map.borders.add(new Border(16, 17));
        map.states.add("IA");//17
        map.borders.add(new Border(17, 22));
        map.borders.add(new Border(17, 23));
        map.borders.add(new Border(17, 18));
        map.states.add("MO");//18
        map.borders.add(new Border(18, 23));
        map.borders.add(new Border(18, 24));
        map.borders.add(new Border(18, 25));
        map.borders.add(new Border(18, 20));
        map.borders.add(new Border(18, 19));
        map.states.add("KS");//19
        map.borders.add(new Border(19, 20));
        map.states.add("OK");//20
        map.borders.add(new Border(20, 26));
        map.borders.add(new Border(20, 21));
        map.states.add("TX");//21
        map.borders.add(new Border(21, 26));
        map.borders.add(new Border(21, 27));
        map.states.add("WI");//22
        map.borders.add(new Border(22, 28));
        map.borders.add(new Border(22, 23));
        map.states.add("IL");//23
        map.borders.add(new Border(23, 29));
        map.borders.add(new Border(23, 24));
        map.states.add("KY");//24
        map.borders.add(new Border(24, 30));
        map.borders.add(new Border(24, 31));
        map.borders.add(new Border(24, 32));
        map.borders.add(new Border(24, 25));
        map.borders.add(new Border(24, 29));
        map.states.add("TN");//25
        map.borders.add(new Border(25, 32));
        map.borders.add(new Border(25, 33));
        map.borders.add(new Border(25, 33));
        map.borders.add(new Border(25, 34));
        map.borders.add(new Border(25, 35));
        map.borders.add(new Border(25, 36));
        map.borders.add(new Border(25, 26));
        map.states.add("AR");//26
        map.borders.add(new Border(26, 36));
        map.borders.add(new Border(26, 27));
        map.states.add("LA");//27
        map.borders.add(new Border(27, 36));
        map.states.add("MI");//28
        map.borders.add(new Border(28, 30));
        map.borders.add(new Border(28, 29));
        map.states.add("IN");//29
        map.borders.add(new Border(29, 30));
        map.states.add("OH");//30
        map.borders.add(new Border(30, 37));
        map.borders.add(new Border(30, 31));
        map.states.add("WV");//31
        map.borders.add(new Border(31, 37));
        map.borders.add(new Border(31, 38));
        map.borders.add(new Border(31, 32));
        map.states.add("VA");//32
        map.borders.add(new Border(32, 38));
        map.borders.add(new Border(32, 39));
        map.borders.add(new Border(32, 33));
        map.states.add("NC");//33
        map.borders.add(new Border(33, 40));
        map.borders.add(new Border(33, 34));
        map.states.add("GA");//34
        map.borders.add(new Border(34, 40));
        map.borders.add(new Border(34, 41));
        map.borders.add(new Border(34, 35));
        map.states.add("AL");//35
        map.borders.add(new Border(35, 41));
        map.borders.add(new Border(35, 36));
        map.states.add("MS");//36

        map.states.add("PA");//37
        map.borders.add(new Border(37, 42));
        map.borders.add(new Border(37, 44));
        map.borders.add(new Border(37, 43));
        map.borders.add(new Border(37, 38));
        map.states.add("MD");//38
        map.borders.add(new Border(38, 44));
        map.borders.add(new Border(38, 39));
        map.states.add("DC");//39

        map.states.add("SC");//40

        map.states.add("FL");//41

        map.states.add("NY");//42
        map.borders.add(new Border(42, 45));
        map.borders.add(new Border(42, 46));
        map.borders.add(new Border(42, 47));
        map.borders.add(new Border(42, 43));
        map.states.add("NJ");//43
        map.borders.add(new Border(43, 47));
        map.borders.add(new Border(43, 44));
        map.states.add("DE");//44

        map.states.add("VT");//45
        map.borders.add(new Border(45, 48));
        map.borders.add(new Border(45, 46));
        map.states.add("MA");//46
        map.borders.add(new Border(46, 48));
        map.borders.add(new Border(46, 47));
        map.borders.add(new Border(46, 49));
        map.states.add("CT");//47
        map.borders.add(new Border(47, 49));
        map.states.add("NH");//48
        map.borders.add(new Border(48, 50));
        map.states.add("RI");//49
        map.states.add("ME");//50

	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
			Map map = new Map();
			initMap(map);
			
			final int populationSize = 2000; // TODO find reasonable value
			Population population = new Population(map, populationSize);

			final int maxIterations = 300; // TODO find reasonable value
			int currentIteration = 0;
			boolean goalFound = false;
			Individual bestIndividual = new Individual(map); // to hold the individual representing the goal, if any
            int mark=0;
			while(currentIteration < maxIterations && !goalFound)
			{
				Population newPopulation = new Population(map);
				for(int i = 0; i < populationSize; ++i)
				{
					Individual x = population.randomSelection();
					Individual y = population.randomSelection();
					Individual child = Individual.reproduce(x, y);
					double pmutate=Math.random();
					if(pmutate<0.01) // TODO use small probability instead
					{
						child.mutate();
					}
					if(child.isGoal())
					{
						goalFound = true;
						bestIndividual = child;
						mark=1;
						break;
					}
					newPopulation.add(child);
				}

				population = newPopulation;
				++currentIteration;
                if(mark==1){
                    break;
                }
			}

			if(goalFound)
			{
				System.out.printf("Found a solution after %d iterations\n", currentIteration);
				bestIndividual.print();
			}
			else
			{
				System.out.printf("Did not find a solution after %d iterations\n", currentIteration);
				System.out.print("Please run it again...");
			}
	}

}
