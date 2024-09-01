import random

def is_point_inside_circle(x, y):

    return x**2 + y**2 < 1

def approximate_pi(num_points):
    points_inside_circle = 0


    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if is_point_inside_circle(x, y):
            points_inside_circle += 1


    pi_approximation = 4 * (points_inside_circle / num_points)
    return pi_approximation

def main():

    num_points = int(input("Enter the number of random points to generate: "))

    pi_value = approximate_pi(num_points)

    print(f"The approximation of pi with {num_points} random points is: {pi_value}")

if __name__ == "__main__":
    main()
