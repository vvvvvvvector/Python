import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

width = 1000
height = 1000

x_min, x_max = -1.8, 1.8
y_min, y_max = -1.8, 1.8

x_width = x_max - x_min
y_height = y_max - y_min

n_iter_max = 0

dots_list = np.zeros([height, width])


def main():
    re, im = 0.0, 0.0

    # c = complex(-0.2, 0.75)
    # c = complex(0, -0.8)

    re = float(
        input("please enter real part of complex number([-2.0, 2.0]): "))
    im = float(
        input("please enter complex part of complex number([-2.0, 2.0]): "))

    print("please choose your resolution:")

    print("1. low")
    print("2. medium")
    print("3. high")
    print("4. ultra")

    n = int(input("please enter chosen resolution number: "))

    if n == 1:
        n_iter_max = 15
    elif n == 2:
        n_iter_max = 55
    elif n == 3:
        n_iter_max = 120
    elif n == 4:
        n_iter_max = 1000
    else:
        n_iter_max = 120

    if re >= -2 and re <= 2 and im >= -2 and im <= 2:
        c = complex(re, im)

        for x in range(width):
            for y in range(height):
                n_iter_count = 0

                a = x / width * x_width + x_min
                b = y / height * y_height + y_min
                z = complex(a, b)

                for i in range(n_iter_max):
                    z = z**2 + c
                    n_iter_count += 1
                    if abs(z) > 2:
                        break

                if n_iter_count != n_iter_max:
                    dots_list[y, x] = n_iter_count / n_iter_max

        fig = plt.figure(figsize=[5.5, 5.5])
        plt.figimage(dots_list, origin='lower', cmap=cm.jet)
        # plt.imshow(dots_list, origin='lower', cmap=cm.jet)
        plt.axis('off')

        plt.show()


if __name__ == "__main__":
    main()
