import math
m_Ears = 5.97600 * math.pow(10, 24)
mAnotherrPlanet = float(input("Please, write the mass of another planet: "))
RAnotherrPlanet = float(input("Please,write down the distance to another planet: "))
G = 6.6743 * math.pow(10, 11)
F = G * m_Ears * mAnotherrPlanet / RAnotherrPlanet **2
print(F)