
public class Individual {
			private Map map; // the map
			private int fitness; // fitness is cached and only updated on request whenever necessary
            // TODO some representation of the genom of the individual
            private int[] color={0,1,2,3};
            private int[] statescolor;

			/**
			 * Updates the fitness value based on the genom and the map.
			 */
			public void updateFitness() {
				// TODO implement fitness function
                int sumfitness=0;
                for(int i=0;i<map.states.size();i++){
                    for (int j=0;j<map.borders.size();j++){
                        if(map.borders.get(j).index1==i){
                            if(statescolor[i]!=statescolor[map.borders.get(j).index2]){
                                sumfitness+=1;
                            }
                        }
                    }
                }
                fitness=sumfitness;
//                System.out.println(fitness);
			}

			/**
			 * Default ctor. Creates a (valid) random individual.
			 * @param map The US states map.
			 */
			public Individual(Map map) {
			    this.map = map;
			    statescolor=new int[map.states.size()];
			    for(int i=0;i<map.states.size();i++){
                    double r=Math.random();
                    if(r>=0&&r<0.25){
                        statescolor[i]=color[0];
                    }
                    if(r>=0.25&&r<0.5){
                        statescolor[i]=color[1];
                    }
                    if(r>=0.5&&r<0.75){
                        statescolor[i]=color[2];
                    }
                    if(r>=0.75&&r<1){
                        statescolor[i]=color[3];
                    }
                }
			// TODO implement random generation of an individual

			    updateFitness();
		    }
		    Individual(){}

			/**
			 * Reproduces a child randomly from two individuals (see textbook).
			 * @param x The first parent.
			 * @param y The second parent.
			 * @return The child created from the two individuals.
			 */
			public static Individual reproduce(Individual x, Individual y) {
				Individual child = new Individual();
				child.map=x.map;
				child.statescolor=new int[x.map.states.size()];
				// TODO reproduce child from individuals x and y
                int r=(int)(Math.random())*(x.statescolor.length-1);
                for(int i=0;i<x.statescolor.length;i++){
                    if(i<r){
                        child.statescolor[i]=x.statescolor[i];
                    }
                    else {
                        child.statescolor[i]=y.statescolor[i];
                    }
                }
				child.updateFitness();
				return child;
			}

			/**
			 * Returns the current fitness value of the individual.
			 * @return The current fitness value.
			 */
			public int getFitness() {
				return fitness;
			}

			/**
			 * Randomly mutates the individual.
			 */
			public void mutate() {
				// TODO implement random mutation of the individual
				int r=(int)(Math.random())*(statescolor.length-1);
				int c=(int)(Math.random())*3;
				statescolor[r]=c;
				updateFitness();
			}

			/**
			 * Checks whether the individual represents a valid goal state.
			 * @return Whether the individual represents a valid goal state.
			 */
			public boolean isGoal() {
			    System.out.println("fitness: "+fitness+" goalfitness: "+map.borders.size());
				return fitness == map.borders.size();
			}
			
			/**
			 * Prints out the individual to the console.
			 */
			void print() {
				// TODO implement printing the individual in the following format:
				// fitness: 15
				// North Carolina: 0
				// South Carolina: 2
				// ...
                System.out.println("fitness: "+fitness);
                for (int i=0;i<statescolor.length;i++){
                    System.out.println(map.states.get(i)+": "+statescolor[i]);
                }
				System.out.println("0, 1, 2, and 3 represent 4 colors respectively.");
	        }
}
