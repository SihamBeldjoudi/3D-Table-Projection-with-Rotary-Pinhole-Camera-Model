import numpy as np
import matplotlib.pyplot as plt

# Constants
f = 5          # Arbitrary focal length factor
v = 6          # Distance for thin lens transformation
dx = 2         # Offset along x-axis for pinhole shift
dy = 3         # Offset along y-axis for pinhole shift
times = np.linspace(0, 10, 5)  # Time intervals for rotation
speeds = np.linspace(0.1, 1, 5)  # Rotation speeds

# Camera intrinsic parameters
f_x = f_y = 4  # Focal length
c_x, c_y = 0, 0  # Principal point (image center)
K = np.array([
    [f_x, 0, c_x],
    [0, f_y, c_y],
    [0, 0, 1]
])

# Function to define 3D points of an asymmetric table
def points_3D_table():
    table_points = []
    t_length = 6  # Table length
    t_width = 3   # Table width
    t_height = 3  # Table top height
    leg_height = 3  # Leg height
    leg_thickness = 0.5  # Leg thickness

    # Generate top surface points of the table
    for x in np.linspace(-t_length / 2, t_length / 2, 20):
        for y in np.linspace(-t_width / 2, t_width / 2, 20):
            table_points.append([x, y, t_height])

    leg_points = []
    # Generate points for each leg at corners, adjusted for thickness
    for dx in [-t_length / 2 + leg_thickness / 2, t_length / 2 - leg_thickness / 2]:
        for dy in [-t_width / 2 + leg_thickness / 2, t_width / 2 - leg_thickness / 2]:
            for z in np.linspace(0, leg_height, 7):
                leg_points.append([dx, dy, z])

    return np.array(table_points + leg_points)

# Thin lens transformation matrix for projection
L = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, -1 / v, 1]
])

# Translation matrix to shift the pinhole
T = np.array([
    [1, 0, 0, dx],
    [0, 1, 0, dy],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Generate 3D points of the table and convert them to homogeneous coordinates
points_3D = points_3D_table()
points_3D_homogeneous = np.hstack((points_3D, np.ones((points_3D.shape[0], 1))))

# Initialize figure for plotting
fig = plt.figure(figsize=(14, 6))

# 3D view of the table
fig1 = fig.add_subplot(121, projection='3d')
fig1.set_title('Table in 3D')
fig1.set_xlabel('X')
fig1.set_ylabel('Y')
fig1.set_zlabel('Z')
fig1.scatter(points_3D[:, 0], points_3D[:, 1], points_3D[:, 2], color='blue', marker='p', s=1)

# 2D projection view
fig2 = fig.add_subplot(122)
fig2.set_title('2D Projection')
fig2.set_xlabel('x')
fig2.set_ylabel('y')

# Colors for different time and speed combinations
colors = plt.cm.viridis(np.linspace(0, 1, len(times) * len(speeds)))

# Project 3D points for each time and speed
i = 0
for t in times:
    for w in speeds:
        # Calculate rotation angle based on speed and time
        theta = w * t

        # Z-axis rotation matrix
        R = np.array([
            [np.cos(theta), -np.sin(theta), 0, 0],
            [np.sin(theta), np.cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # Combined transformation and projection matrix
        M = np.dot(L, np.dot(R, T))
        points_2D_homogeneous = np.dot(points_3D_homogeneous, M.T)
        points_2D_homogeneous = np.dot(K, points_2D_homogeneous[:, :3].T).T

        # Convert homogeneous coordinates to 2D coordinates
        x_2D = points_2D_homogeneous[:, 0] / points_2D_homogeneous[:, 2]
        y_2D = points_2D_homogeneous[:, 1] / points_2D_homogeneous[:, 2]

        # Plot 2D projection for the current time and speed
        fig2.scatter(x_2D, y_2D, color=colors[i], marker='p', s=1, label=f't={t}, w={round(w,2)}')
        i += 1

# Set plot limits and add reference lines
fig2.set_xlim(-10, 15)
fig2.set_ylim(-10, 10)
fig2.grid(True)
fig2.axhline(c_y, color='black', linewidth=0.25)
fig2.axvline(c_x, color='black', linewidth=0.25)
fig2.axhline(dx, color='red', linewidth=0.25)
fig2.axvline(dy, color='red', linewidth=0.25)

# Adjust aspect ratio and add legend
fig2.set_aspect('equal', adjustable='box')
fig2.legend()

# Display the plot
plt.tight_layout()
plt.show()

