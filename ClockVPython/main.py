from vpython import *
import datetime


def clock_init():
    ring_radius = 2
    ring_color = color.cyan

    sphere_radius = 0.2
    sphere_color = color.black

    box(pos=vector(0, 0, 0.9), size=vector(5, 5, 0.3), color=color.orange)
    ring(pos=vector(0, 0, 1), axis=vector(0, 0, 1), radius=ring_radius, thickness=0.1, color=ring_color)

    sphere(pos=vector(0, 0, 1.1), radius=sphere_radius / 2, color=color.red)

    sphere(pos=vector(ring_radius * sin(0), ring_radius * cos(0), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(ring_radius * sin(pi / 6), ring_radius * cos(pi / 6), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(pi / 3), ring_radius * cos(pi / 3), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(pi / 2), ring_radius * cos(pi / 2), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(2 * pi / 3), ring_radius * cos(2 * pi / 3), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(5 * pi / 6), ring_radius * cos(5 * pi / 6), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(pi), ring_radius * cos(pi), 1), radius=sphere_radius, color=sphere_color)
    sphere(pos=vector(ring_radius * sin(7 * pi / 6), ring_radius * cos(7 * pi / 6), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(4 * pi / 3), ring_radius * cos(4 * pi / 3), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(3 * pi / 2), ring_radius * cos(3 * pi / 2), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(5 * pi / 3), ring_radius * cos(5 * pi / 3), 1), radius=sphere_radius,
           color=sphere_color)
    sphere(pos=vector(ring_radius * sin(11 * pi / 6), ring_radius * cos(11 * pi / 6), 1), radius=sphere_radius,
           color=sphere_color)


def main():
    # scene.camera.pos = vector(0, 0, 4)
    # scene.camera.axis = vector(5, -7, -5)

    clock_init()

    now = datetime.datetime.now()

    current_seconds = now.second
    current_minutes = now.minute
    current_hours = now.hour

    t_seconds = (current_seconds * 2 * pi) / 60
    dt_seconds = pi / 30

    t_minutes = (current_minutes * 2 * pi) / 60
    dt_minutes = pi / 30

    t_hours = (current_hours * 2 * pi) / 60
    dt_hours = pi / 360

    arrow_seconds = arrow(pos=vector(0, 0, 1.1), axis=vector((2 - 0.2) * sin(t_seconds), (2 - 0.2) * cos(t_seconds), 0),
                          color=color.white, shaftwidth=0.04)

    arrow_minutes = arrow(pos=vector(0, 0, 1.1), axis=vector(1.8 * sin(t_minutes), 1.8 * cos(t_minutes), 0),
                          color=color.white, shaftwidth=0.07)

    arrow_hours = arrow(pos=vector(0, 0, 1.1), axis=vector(1.3 * sin(t_hours), 1.3 * cos(t_hours), 0),
                        color=color.white, shaftwidth=0.1)

    while True:
        if fabs(t_seconds - 2 * pi) < 0.0000000001:
            t_seconds = 0
            t_minutes += dt_minutes
            t_hours += dt_hours
            arrow_minutes.axis = vector(1.8 * sin(t_minutes), 1.8 * cos(t_minutes), 0)
            arrow_hours.axis = vector(1.3 * sin(t_hours), 1.3 * cos(t_hours), 0)

        arrow_seconds.axis = vector(1.8 * sin(t_seconds), 1.8 * cos(t_seconds), 0)

        t_seconds += dt_seconds

        sleep(1)


if __name__ == "__main__":
    main()
