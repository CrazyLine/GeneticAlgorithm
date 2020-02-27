import java.util.Vector;

/**
 * Class representing a population of individuals
 */
public class Population extends Vector<Individual> {
	private Map map;
		
	/**
	 * Actual standard ctor.
	 * @param map The map.
	 * @param initialSize The initial size of the population.
	 */
	Population(Map map, int initialSize) {
		for(int i = 0; i < initialSize; ++i)
		{
			add(new Individual(map));
		}
	}
	
	/**
	 * Standard ctor.
	 * @param map The map.
	 */
	public Population(Map map) {
		this(map, 0);
	}
	
	/**
	 * Randomly selects an individual out of the population
	 * proportionally to its fitness.
	 * @return The selected individual.
	 */
	Individual randomSelection() {
		// TODO implement random selection
		// an individual should be selected with a probability
		// proportional to its fitness
		int sumfitness=0;
		for(int i=0;i<size();i++){
			sumfitness+=get(i).getFitness();
		}
		double r=Math.random()*(sumfitness-1);
		int sumprevious=0;
		for (int i=0;i<size();i++){
			if(r>=sumprevious&&r<(sumprevious+get(i).getFitness())){
				//System.out.println("class Population 46");
				return get(i);
			}
			sumprevious+=get(i).getFitness();
		}
		return null;
	}
	
}
