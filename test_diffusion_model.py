from diffusion_model import energy
import monte_carlo as MC

def test_energy():
    density = range(1,6)
    assert energy(density) == 20
    
def test_energy_empty():
    density = []
    assert energy(density) == 0

def test_large_array_of_zeros():
    density = [0] * 1000000 
    assert energy(density) == 0

#tests for move_particle_one
#check that it hasn't changed the number
def test_same_number_at_end():
    density = [1,0,2] * 100
    assert sum(density) == sum(MC.move_particle_one(density,3))