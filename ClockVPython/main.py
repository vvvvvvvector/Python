from vpython import *


def clock_init():
    ring_radius = 2
    ring_color = color.cyan

    sphere_radius = 0.2
    sphere_color = color.black

    box(pos=vector(0, 0, 0.9), size=vector(5, 5, 0.3), color=color.orange)
    ring(pos=vector(0, 0, 1), axis=vector(0, 0, 1), radius=ring_radius, thickness=0.1, color=ring_color)

    sphere(pos=vector(2 * sin(0), 2 * cos(0), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(pi / 6), 2 * cos(pi / 6), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(pi / 3), 2 * cos(pi / 3), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(pi / 2), 2 * cos(pi / 2), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(2 * pi / 3), 2 * cos(2 * pi / 3), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(5 * pi / 6), 2 * cos(5 * pi / 6), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(pi), 2 * cos(pi), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(7 * pi / 6), 2 * cos(7 * pi / 6), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(4 * pi / 3), 2 * cos(4 * pi / 3), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(3 * pi / 2), 2 * cos(3 * pi / 2), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(5 * pi / 3), 2 * cos(5 * pi / 3), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(2 * sin(11 * pi / 6), 2 * cos(11 * pi / 6), 1), radius=sphere_radius, color=sphere_color)


def main():
    clock_init()
    # scene.camera.pos = vector(0, 0, 4)
    # scene.camera.axis = vector(5, -7, -5)


if __name__ == "__main__":
    main()
