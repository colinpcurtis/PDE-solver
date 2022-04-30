import numpy as np
import matplotlib.pyplot as plt


K = 10
delta_x = .1
delta_t = (delta_x ** 2)/(4 * K)

boundary = 1
length = 10
max_time = 2
u_start = 10
u_left = 0
u_right = 0

neumann = True 
"""
applies neumann boundary condition at left endpoint
with du/dx(0, t) = u_left
"""

assert ((K * delta_t) / (delta_x ** 2)) < (1 / 2) # stability condition

def initial_condition(x):
    return u_start


def apply_conditions(u):
    n = u.shape[1]
    u[0, :] = np.vectorize(initial_condition)(u[0, :])
    if not neumann:
        u[:, 0] = u_left
    u[:, n - 1] = u_right


def create_mesh():
    # need to switch so the time indicies are the rows
    num_points_x = int(length / delta_x)
    num_points_t = int(max_time / delta_t)
    grid = np.zeros((num_points_t, num_points_x))
    grid[0, :] = np.linspace(0, length, num_points_x)
    return grid


def finite_differences(points):
    apply_conditions(points)
    rows, cols =  points.shape
    scale = (K * delta_t) / (delta_x ** 2)

    for k in range(rows - 1):
        if neumann:
            neumann_update = 2 * (points[k, 1] - points[k, 0] - (delta_x * u_left))
            points[k+1, 0] = points[k, 0] + (scale * neumann_update)
        for n in range(1, cols - 1):
            update = points[k, n + 1] - (2 * points[k, n]) + points[k, n - 1]
            next_time = points[k, n] + (scale * update)
            points[k + 1, n] = next_time
    return points


def plot_1d(u):
    rows, cols = u.shape
    plt.imshow(u, cmap="hot", aspect=(cols/rows))
    plt.title("Temperature on Rod with Time")
    plt.xlabel("Position on Rod")
    plt.ylabel(r"Time $\Delta t$")
    plt.colorbar(label="temperature")
    plt.show()
    # plt.savefig("images/heat_equation_fig2.png")


if __name__ == "__main__":
    points = create_mesh()

    u = finite_differences(points)

    plot_1d(u)

