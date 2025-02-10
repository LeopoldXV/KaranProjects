def calculate_cost(cost, width, height):
    # assuming that the cost is per meter squared, and that the width and height are in meters
    return (width * height) / cost

if __name__ == "__main__":
    COST = float(input("What is the cost of a single tile? "))
    WIDTH = float(input("What is the width of the floor? "))
    HEIGHT = float(input("What is the height of the floor? "))

    print(calculate_cost(COST, WIDTH, HEIGHT))
