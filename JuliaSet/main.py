import matplotlib.pyplot as plt

width = 1000
height = 1000

x_min, x_max = -1.75, 1.75
y_min, y_max = -1.75, 1.75

x_width = x_max - x_min
y_height = y_max - y_min

c = complex(-0.835, -0.2321)
# c = complex(0, -0.8)

n_iter = 25

x_dots, y_dots = [], []


def main():
    for x in range(width):
        for y in range(height):
            a = x / width * x_width + x_min
            b = y / height * y_height + y_min
            z = complex(a, b)
            
            for i in range(n_iter):
                z = z**2 + c
                if abs(z) > 1.75:
                    break
            else:
                x_dots.append(x)
                y_dots.append(y)

    plt.scatter(x_dots, y_dots, s=0.5,  c='#000000')
    #plt.axis('off')

    plt.show()


if __name__ == "__main__":
    main()
