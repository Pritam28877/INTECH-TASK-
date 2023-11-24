# STL File Processing with VTK in C++

This project involves processing and visualizing 3D models stored in STL (Stereolithography) files using the Visualization Toolkit (VTK) library in C++. The main task is to identify and highlight all triangles in the 3D model that make an angle more than 45 degrees with the horizontal plane.

## Why C++?

C++ was chosen for this project due to its efficiency and the extensive support it provides for complex mathematical calculations and 3D graphics, which are crucial for this project. Moreover, VTK is natively written in C++, ensuring seamless integration and optimal performance.

## Project Overview

The project involves the following steps:

1. **Reading the STL file**: The STL file, which contains the 3D model data, is read using the `vtkSTLReader` class in VTK.

2. **Processing the triangles**: Each triangle in the 3D model is processed to calculate the angle it makes with the horizontal plane. This is done by calculating the angle between the normal vector of the triangle and the horizontal plane vector (0, 0, 1).

3. **Highlighting the triangles**: If a triangle makes an angle more than 45 degrees with the horizontal plane, it is highlighted in the 3D model visualization. This is achieved by creating a new actor for the triangle, setting its color to a different one (e.g., red), and adding it to the renderer.

## Running the Project

To run the project, you need to have the VTK library installed in your development environment. You can then compile and run the C++ code using your preferred C++ compiler.

### import vtk
