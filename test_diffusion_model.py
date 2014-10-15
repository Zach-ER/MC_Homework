from diffusion_model import energy
def test_energy():
    density = range(1,6)
    assert energy(density) == 20
    
def test_energy_empty():
    density = []
    assert energy(density) == 0

def test_large_array_of_zeros():
    density = [0] * 1000000 
    assert energy(density) == 0
