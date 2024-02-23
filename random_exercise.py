import random


def generate_random_int_places(n: int) -> int:
    # Generates a random integer with maximum n places
    return random.randint(0, 10**n)


if __name__ == '__main__':
    print(generate_random_int_places(3))
