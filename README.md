# 3D Table Projection with Rotary Pinhole Camera Model

This project simulates the projection of a 3D asymmetrical table onto a 2D plane using a rotary pinhole camera model with an off-centered aperture. It leverages a combination of intrinsic camera parameters, a thin lens model, and time-varying rotation to showcase the effects of rotary motion and aperture offsets on 2D projections of a 3D object. This setup is ideal for exploring camera modeling concepts, 3D transformations, and dynamic projection techniques.

## Key Features

### 1. 3D Table Model
A simple 3D model of an asymmetrical table is created with a tabletop and four legs:
- **Top Surface**: Defined with customizable length, width, and height values, represented by a grid of points.
- **Legs**: Four legs are positioned at the corners of the tabletop, with adjustable thickness and height, allowing for realistic proportions.
- **Representation**: Points are stored in a 3D array format, making transformations straightforward.

### 2. Rotary Camera Model and Transformations
The rotary camera model simulates a pinhole camera with an aperture that is offset from the origin, combining intrinsic parameters, translation, and a thin lens transformation.

- **Intrinsic Camera Parameters (K)**:
  - Defines focal lengths (`f_x`, `f_y`) and the principal point (`c_x`, `c_y`), assuming a centered image plane.
  - Provides an initial setup of camera parameters before any transformations.

- **Pinhole Shift Matrix (T)**:
  - Applies an x-axis (`dx`) and y-axis (`dy`) offset to simulate a non-centered aperture, creating a shifted perspective.
  - This translation matrix models the shift of the pinhole itself rather than the object or camera position.

- **Thin Lens Transformation (L)**:
  - Simulates the thin lens effect, mapping 3D points onto a 2D plane at a distance (`v`) from the lens.
  - This matrix emphasizes the effect of the focal length on perspective distortion, creating depth in the projection.

### 3. Dynamic Rotary Motion
The code allows for rotary motion based on time intervals and rotation speeds, generating different projection angles for each configuration.

- **Time and Speed Parameters**:
  - `times` (a list of time intervals) and `speeds` (a range of angular speeds) enable dynamic changes in the camera’s angle.
  - These variables control the rotation angle as \(\theta = w \times t\), where `w` is the rotation speed and `t` is the time interval, simulating the table’s rotation over time.

- **Rotation Matrix (R)**:
  - A Z-axis rotation matrix calculates the angle of rotation, affecting the position and orientation of the 3D object in each projection.
  - This matrix allows the camera to create multiple perspectives of the table as it "rotates" around the Z-axis over time.

- **Combined Transformation (M)**:
  - The matrices `T` (translation), `R` (rotation), and `L` (thin lens) are combined into a single transformation matrix `M`, which is applied to the 3D points to yield a final 2D projection.
  - The intrinsic matrix `K` is then applied to scale and translate the projection into pixel coordinates.

### 4. Visualization
Two plots are generated for easy visualization and comparison:

- **3D Plot**:
  - Displays the 3D table model, providing a reference for the original structure and dimensions.
  - Includes labeled axes (X, Y, Z) and plots the tabletop and legs in blue.

- **2D Projection Plot**:
  - Shows the projected points of the 3D table from the camera's perspective at each time-speed configuration.
  - Each rotation angle’s projection is represented in a unique color, and labels indicate the time and speed for each configuration.
  - Reference lines (black and red) mark the x and y shifts of the aperture for context.
  - Adjustable x and y limits and an equal aspect ratio ensure accurate scaling and perspective in the plot.

## Code Structure and Customization
- **Parameters**: Easily adjust focal lengths (`f_x`, `f_y`), time intervals, rotation speeds, and pinhole offsets (`dx`, `dy`) to explore various projection effects.
- **Modular Functions**: The 3D point generation, transformation, and projection calculations are modular, making the code extensible for additional objects or transformations.

## Dependencies
- **`numpy`**: Used for efficient matrix operations, 3D point generation, and transformations.
- **`matplotlib`**: Handles 3D and 2D plotting, allowing for clear visualization of projections.

## Usage
Run the script to generate dynamic 2D projections of the rotating 3D table. Experiment with different parameters to observe changes in perspective due to variations in rotation, focal length, and pinhole offset.

## Potential Applications
This project serves as a foundation for learning and testing:
- **Camera Modeling and Calibration**: Simulate intrinsic and extrinsic camera parameters, offering a realistic approximation of perspective transformations.
- **3D Graphics and Rendering**: Understand how 3D objects are projected onto a 2D screen, an essential concept in computer graphics.
- **Computer Vision and Robotics**: Gain insight into how rotary camera models and perspective transformations can be applied in object recognition, SLAM, and other vision-based applications.

