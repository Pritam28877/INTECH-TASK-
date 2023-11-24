import vtk

# Step 1: Read the .stl file
reader = vtk.vtkSTLReader()
reader.SetFileName("./Step 1.stl")
reader.Update()

# Step 2: Get the data from the .stl file
data = reader.GetOutput()

# Create a mapper and actor for the original data
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(data)

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a new polydata to store the highlighted triangles
highligtdata = vtk.vtkPolyData()
highlightpoints = vtk.vtkPoints()
highlightpolys = vtk.vtkCellArray()

# Step 3: Iterate over each triangle in the data
for i in range(data.GetNumberOfCells()):
    triangle = data.GetCell(i)
    normal = [0.0, 0.0, 0.0]
    vtk.vtkTriangle.ComputeNormal(triangle.GetPoints().GetPoint(0), 
    triangle.GetPoints().GetPoint(1), triangle.GetPoints().GetPoint(2), normal)
    # The horizontal plane can be represented as the vector (0, 0, 1)
    horizontal_plane = [0, 0, 1]

    # Calculate the angle between the triangle normal and the horizontal plane
    angle = vtk.vtkMath.AngleBetweenVectors(normal, horizontal_plane)

    # Check if the angle is more than 45 degrees
    if angle > vtk.vtkMath.RadiansFromDegrees(45):
        # This triangle makes an angle more than 45 degrees with the horizontal plane
        # Add this triangle to the highlighted_data
        highlightpoints.InsertNextPoint(triangle.GetPoints().GetPoint(0))
        highlightpoints.InsertNextPoint(triangle.GetPoints().GetPoint(1))
        highlightpoints.InsertNextPoint(triangle.GetPoints().GetPoint(2))
        highlightpolys.InsertNextCell(3, [i*3, i*3+1, i*3+2])

# Set the points and polys of the highlighted_data
highligtdata.SetPoints(highlightpoints)
highligtdata.SetPolys(highlightpolys)

# Create a mapper and actor for the highlighted_data
highlighted_mapper = vtk.vtkPolyDataMapper()
highlighted_mapper.SetInputData(highligtdata)

highlighted_actor = vtk.vtkActor()
highlighted_actor.SetMapper(highlighted_mapper)
# Set color to red
highlighted_actor.GetProperty().SetColor(1.0, 0.0, 0.0)  

# Create a renderer and add the actors to it
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.AddActor(highlighted_actor)

# Create a render window and add the renderer to it
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a render window interactor and set the render window to it
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the interaction
interactor.Initialize()
interactor.Start()
