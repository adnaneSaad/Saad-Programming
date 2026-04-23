import matplotlib.pyplot as plt

def create_blueprint(dat_file, chord_mm):
    x, y = [], []
    with open(dat_file, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            coords = line.split()
            if len(coords) == 2:
                # Scale the 0-1 coordinates to real millimeters
                x.append(float(coords[0]) * chord_mm)
                y.append(float(coords[1]) * chord_mm)

    # Export to a simple DXF-style text file for CAD
    with open('wing_rib.dxf', 'w') as dxf:
        dxf.write("0\nSECTION\n2\nENTITIES\n")
        for i in range(len(x)-1):
            dxf.write(f"0\nLINE\n8\n0\n10\n{x[i]}\n20\n{y[i]}\n11\n{x[i+1]}\n21\n{y[i+1]}\n")
        dxf.write("0\nENDSEC\n0\nEOF\n")
    
    print(f"Success! wing_rib.dxf created at {chord_mm}mm scale.")

if __name__ == "__main__":
    # Change 200 to whatever size (in mm) you want your wing to be!
    create_blueprint('NACA-4412.dat', 200)
