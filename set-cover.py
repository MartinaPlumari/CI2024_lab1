from random import random, seed
from itertools import product
from itertools import accumulate
import numpy as np
import sys
from matplotlib import pyplot as plt

from icecream import ic

UNIVERSE_SIZE = 100000
NUM_SETS = 10000
DENSITY = 0.2

MAX_STEPS = 1000

rng = np.random.Generator(np.random.PCG64([UNIVERSE_SIZE, NUM_SETS, int(10_000 * DENSITY)]))



SETS = np.random.random((NUM_SETS, UNIVERSE_SIZE)) < DENSITY
for s in range(UNIVERSE_SIZE):
    if not np.any(SETS[:, s]):
        SETS[np.random.randint(NUM_SETS), s] = True
COSTS = np.pow(SETS.sum(axis=1), 1.1)


def valid(solution):
    """Checks wether solution is valid (ie. covers all universe)"""
    return np.all(np.logical_or.reduce(SETS[solution]))

def cost(solution):
    """Returns the cost of a solution (to be minimized)"""
    return COSTS[solution].sum()

def coverage(solution):
    """Returns how many elements of the universe are covered by the union of sets""" 
    return np.sum(np.any(SETS[solution], axis=0))


#multiple mutation tweak
def multiple_mutation(solution: np.ndarray, strength: float = 0.1) -> np.ndarray:
    """Tweak function. It inverts a random number of elements in the solution""" 
    mask = rng.random(NUM_SETS) < strength
    new_sol = np.logical_xor(solution, mask)
    return new_sol

#fitness function: it returns a tuple with the coverage and the cost of the solution
def fitness(solution: np.ndarray):
    return (coverage(solution), -cost(solution))



STEEPEST_STEP_CANDIDATES = 10
BUFFER_SIZE = NUM_SETS//30 

#solution initialization
solution = rng.random(NUM_SETS) < .2

strength = 0.1
buffer = list()
max_value= (-1,-sys.maxsize)
num_steps = 0
steady= 0

solution_fitness = fitness(solution)
ic(solution_fitness)
print("Initial solution taken sets percentage:", np.sum(solution)/NUM_SETS*100, '%\n')

last_improvement = 0
new_solution = solution
cost_history = [solution_fitness[1]]

tweak = multiple_mutation

for step in range(MAX_STEPS):
    
    candidates = [tweak(solution, strength) for i in range(0, STEEPEST_STEP_CANDIDATES)]
    candidates_fitness = list()
    for c in candidates:
        f = fitness(c)
        cost_history.append(f[1])
        candidates_fitness.append(f)    
    idx = candidates_fitness.index(max(candidates_fitness))
    
    new_solution = candidates[idx]
    new_fitness = candidates_fitness[idx]
    num_steps += STEEPEST_STEP_CANDIDATES
    
    buffer.append(new_fitness>solution_fitness)    
    buffer = buffer[-BUFFER_SIZE:]
    if sum(buffer) > BUFFER_SIZE/5 :
         strength *= 1.1
    if sum(buffer) < BUFFER_SIZE/5 :
         strength /= 1.1
    
    if new_fitness > solution_fitness:
        last_improvement  = step
        solution = new_solution
        solution_fitness = new_fitness
    elif new_fitness == solution_fitness:
        steady += 1
    
    if steady > 200:
         break   

ic(fitness(solution))
ic(valid(solution))
print("Num steps:", num_steps)
print("Taken sets percentage: ", np.sum(solution)/NUM_SETS*100, '%')
 
 
#plotting the results
plt.figure(figsize=(14, 8))

plt.plot(
    range(len(cost_history)),
    list(accumulate(cost_history, max)),
    color="red",
)
x = plt.scatter(range(len(cost_history)), cost_history, marker=".")

plt.show()