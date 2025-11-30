import math as mt 

E1 = 1

A = float(input("Enter target mass number (A): "))
B = float(input("Enter scattering angle theta (degrees): "))

c = mt.cos(mt.radians(B))
K1 = (A**2)+1+(2*A*c)
K2 = (A+1)**2
E2 = (K1/K2)*E1

print(f"Final neutron energy: {E2:.4f} MeV")

