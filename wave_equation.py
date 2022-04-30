import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


WAVE_SPEED = 10
delta_x = .1
delta_t = delta_x / (2 * np.sqrt(WAVE_SPEED))

boundary = 1
length = np.pi * 2
max_time = 5

assert np.sqrt(WAVE_SPEED) * delta_t / delta_x <= 1


def initial_condition(x):
    return np.sin(x)


def initial_condition_t(x):
    return 0


def create_mesh():
    # need to switch so the time indicies are the rows
    num_points_x = int(length / delta_x)
    num_points_t = int(max_time / delta_t)
    grid = np.zeros((num_points_t, num_points_x))
    grid[0, :] = np.linspace(0, length, num_points_x)
    return grid


def apply_conditions(u):
    u[0, :] = np.vectorize(initial_condition)(u[0, :])

    scale = (WAVE_SPEED * (delta_t ** 2)) / (delta_x ** 2)

    num_points_x = int(length / delta_x)
    points_x = np.linspace(0, length, num_points_x)

    cols = u.shape[1]

    for n in range(cols - 1):
        update = u[0, n + 1] - (2 * u[0, n]) + u[0, n - 1]
        u[1, n + 1] = u[0, n] + (.5 * scale * update) + (delta_t * initial_condition_t(points_x[n]))


def finite_differences(points):
    apply_conditions(points)
    rows, cols =  points.shape
    scale = (WAVE_SPEED * (delta_t ** 2)) / (delta_x ** 2)

    for k in range(1, rows - 1):
        for n in range(1, cols - 1):
            update = points[k, n + 1] - (2 * points[k, n]) + points[k, n - 1]
            next_time = (2 * points[k, n]) - points[k - 1, n] + (scale * update)
            points[k + 1, n] = next_time
    return points


def init():
    line.set_data([], [])
    return line


def animate(i):
    num_points_x = int(length / delta_x)
    x = np.linspace(0, length, num_points_x)
    y = u[i, :]
    line.set_data(x, y)
    return line


if __name__ == "__main__":
    points = create_mesh()

    u = finite_differences(points)
    print(u.shape)

    fig = plt.figure()
    ax = plt.axes(xlim=(0, np.pi * 2), ylim=(-5, 5))
    line, = ax.plot([], [], lw=3)

    frames = int(max_time / delta_t)

    anim = FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=1, blit=False)
    plt.title("Wave Displacement vs Time")
    plt.xlabel(r"Distance Along String")
    plt.ylabel(r"Displacement $u(x, t)$")
    anim.save('images/wave_equation.gif')
    # plt.show()
