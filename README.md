# About

This algorithm is named Solo Leveling as a reference to one literary work. The idea of that algorithm is to simulate some behaviour of a character from this writing but modified into an algorithm. Is more like an RPG game strategy for a King during a fight. Here are presented it's features:

* First 5 steps have a structure that looks like 01110. This is the idea how to control such algorithms as Eye for an Eye for example. 
* Then the algorithm get 4 different situations to proceed. 
  1. First one named ATTACK: gets the next 5 steps as enemies reverse history (1->0;0->1)
  2. Second is DEFENCE: gets the next 5 steps as enemies history (copy)
  3. Third variant is ARISE: gets the enemies 4 steps history as copy, but the 5th will always be 1 
  4. The last situation is MONARCH TERRITORY: next 5 steps are close to random

* The oponent choosing algorithm works next way: it determines according to enemy's history either the case is best/good/normal/bad/worst. It depends on the points we can potentially get:
  1. Best - we get maximum points
  2. Good - we get equal points
  3. Normal - we get a bit less points
  4. Bad - we get less points
  5. Worst - we get only 1 point, while oponont get a lot

To cut to the chase this is the algorithm that combines Eye for an Eye and Random algorithms, but uses more interesting pattern
