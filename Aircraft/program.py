#!/usr/bin/env python3
import matplotlib.pyplot as plt

def generate_plot(filename):
    x, y = [], []
    try:
        with open(filename, 'r') as f:
            # Skip the first line (header)
            lines = f.readlines()[1:]
            for line in lines:
                coords = line.split()
                if len(coords) == 2:
                    x.append(float(coords[0]))
                    y.append(float(coords[1]))
        
        plt.figure(figsize=(12, 4))
        plt.plot(x, y, 'b-o', markersize=2, label='NACA 4412')
        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.title('Airfoil Blueprint Visualization')
        plt.xlabel('Chord Position (0 to 1)')
        plt.ylabel('Thickness')
        plt.show()
        
    except FileNotFoundError:
        print(f"Error: {filename} not found. Save your .dat file first!")

if __name__ == "__main__":
    generate_plot('NACA-4412.dat')
