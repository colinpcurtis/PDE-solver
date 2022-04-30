# Finite Differences to Solve PDEs

This repository implements the finite differences method to solve the heat and wave equation in 1D

GitHub doesn't currently support LaTeX in markdown files, so it's not possible to give a
really nice looking description of the numerical scheme, however I'll release a PDF paper
explaining this soon.

## Heat Equation Results


These two images are the output from the numerical scheme for the heat equation, where each row in the image is the temperature of the rod, and each row increments time by delta t.  

![heat equation dirichlet boundary conditions](images/heat_equation_fig1.png)

The first image is for a non-insulating boundary, so heat quickly dissipates on the rod with time.

![heat equation neumann boundary conditions](images/heat_equation_fig2.png)

The second image is for an insulating boundary on the left, which means that heat is not lost near the left boundary.


## Wave Equation Results

This animation displays the wave displacement vs time

![wave equation](images/wave_equation.gif)
