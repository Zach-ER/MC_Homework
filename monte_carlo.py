import diffusion_model as dm
from random import random
from math import exp

def monte_carlo(energy,density,temperature,iterations):
    """inputs of some energy function, a given density, a temperature and a number of iterations """
    for ii in range(iterations):
        #keep value of input density
        first_density = density[:]
        #compute the energy of the system.
        energy_val = energy(density)
        #perturb the density by moving a particle
        box_no = which_box_loses_a_particle(density)
        second_density = move_particle_one(density,box_no)
        E0 = float(energy(first_density))
        E1 = float(energy(second_density))
        temperature = float(temperature)
        
        #if new energy is less, keep that.
        if E0 > E1:
            density = second_density
        #or if the boltzmann exceeds a random number in [0,1]
        elif boltzmann(E0,E1,temperature) > random():
            density = second_density
        else:
            density = first_density
    return density

def which_box_loses_a_particle(density):
    #will pick a random particle in the density and return the box number
    num_particles = sum(density)
    particle_we_move =  random() * num_particles
    #here, we see which box the particle lived in - when we tick past the counter, then it was that box
    i = 0
    ctr = 0
    while ctr < particle_we_move:
        ctr += density[i]
        box_no = i
        i += 1
    return box_no

#moves particle in box box_no one to left or right, at random.
#circular boundary conditions
def move_particle_one(density,box_no):
    density[box_no] -= 1
    if random() > .5:
        density[(box_no + 1) %len(density)] += 1
    else:
        density[(box_no - 1 )%len(density)] += 1
    return density

#calculates the boltzmann distribution
def boltzmann(E0,E1,T):
    return exp(-(E1-E0)/T)
