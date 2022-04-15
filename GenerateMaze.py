import random

CONFIG_FILE_NAME = 'testGrid.txt'

density = 500
maxRange = 30

def main():

    points = []

    for _ in range(density):
        x = random.randint(0, maxRange)
        y = random.randint(0, maxRange)

        point = (x, y)
        points.append(point)

    with open(CONFIG_FILE_NAME, 'w') as cf:
        for point in points:
            x, y = point[0], point[1]
            cf.write(str(x) + " " + str(y) + "\n")

if __name__ == "__main__":
    main()