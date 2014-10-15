def energy(density, coeff=1.0):
    big_sigma = 0
    for piece in density:
        big_sigma += piece * (piece-1)
    return big_sigma * coeff / 2
