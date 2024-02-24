import random


def generate_random_int_places(n: int = 3) -> int:
    # Generates a random integer with maximum n places. 
    # n=3 by default. On failure 3 is used.
    try:
        return random.randint(0, 10**n)
    except:
        print(
            'Error in generate_random_int_places.\n'
            f'Returning with n=3.\nGiven n: {n}\n'
            f'n type: {type(n)}')
        return random.randint(0, 10**3)


if __name__ == '__main__':
    print(generate_random_int_places('2'))
