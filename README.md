# Neutron Scattering Energy Calculator

This Python program calculates the final energy of a neutron after an elastic collision with a target nucleus. 
The program uses a simplified classical model for two-body elastic scattering.

## How It Works
- The user inputs:
  - Target mass number (A)
  - Scattering angle (theta) in degrees
- The program calculates the final neutron energy using the formula:
  
  E2 = E1 * (A^2 + 1 + 2*A*cos(theta)) / (A + 1)^2

- Initial neutron energy is assumed to be 1 MeV.
- Output is displayed in MeV.

## How to Run
1. Make sure Python 3 is installed on your system.
2. Run the script `neutron_scattering.py`.
3. Enter the target mass number and scattering angle when prompted.
4. The program prints the final neutron energy in MeV.

## Notes
- This is a simplified model assuming an ideal two-body elastic collision.
- Angles must be entered in degrees.
