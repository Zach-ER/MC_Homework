import diffusion_model as dm
from random import random

def monte_carlo(energy,density,temperature):
    """inputs of some energy function, a given density and a temperature"""
    #keep value of input density 
    first_density = density[:]
    #compute the energy of the system. 
    energy_val = energy(density)
    #perturb the density by moving a particle 
    second_density = perturb(density)
    
    print first_density, second_density

def perturb(density):
    #will pick a random particle in the density and move it either left or right 
    num_particles = sum(density)
    particle_we_move =  random() * num_particles
    #here, we see which box the particle lived in - when we tick past the counter, then it was that box
    i = 0 
    ctr = 0
    while ctr < particle_we_move:
        ctr += density[i]
        box_no = i
        i += 1
    return move_particle_one(density,box_no)
    
#moves particle in box box_no one to left or right, at random. 
#circular boundary conditions 
def move_particle_one(density,box_no):
    density[box_no] -= 1 
    if random() > .5:
        density[(box_no + 1) %len(density)] += 1
    else: 
        density[(box_no - 1 )%len(density)] += 1
    return density
        
monte_carlo(dm.energy,[1000] * 5 ,1)


