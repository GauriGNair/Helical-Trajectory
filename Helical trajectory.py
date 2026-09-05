from matplotlib.pyplot import *
from numpy import *

# Step 1: Define system parameters separately
r = 2  # Radius of the helical wire (distance from z-axis)
omega = 3.5  # Angular velocity (speed of rotation around z-axis)
b = 3.5  # Vertical speed constant (rate of vertical speed along z-axis)

# Step 2: Create a smooth time array from 0 to 10 seconds
t = linspace(0, 10, 1000)

# Step 3: Calculate parametric positions (Cylindrical to Cartesian coordinates)
x = r * cos(omega * t)  # X-coordinate over time
y = r * sin(omega * t)  # Y-coordinate over time
z = b * t  # Z-coordinate over time

# Step 4: Set up 3D plot directly
p = axes(projection="3d")

# Step 5: Plot the continuous helical wire path
p.plot(x, y, z, color="purple", linewidth=3)
p.plot([x[0]], [y[0]], [z[0]], marker="o", color="pink")
p.plot([x[-1]], [y[-1]], [z[-1]], marker="o", color="pink")
p.set_xlabel("x")
p.set_ylabel("y")
p.set_zlabel("z")
p.set_title("Trajectory of Bead on Helical Wire")

show()
