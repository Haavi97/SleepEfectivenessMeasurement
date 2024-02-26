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


def generate_random_multiple_int_places(multiple: int, n: int = 3) -> int:
    # Generates a random integer with maximum n places.
    # n=3 by default. On failure 3 is used.
    try:
        return random.randrange(0, 10**n, multiple)
    except:
        print(
            'Error in generate_random_multiple_int_places.\n'
            f'Returning with multiple=1.\nGiven multiple: {multiple}\n'
            f'multiple type: {type(multiple)}\n'
            f'Returning with n=3.\nGiven n: {n}\n'
            f'n type: {type(n)}')
        return random.randrange(0, 10**3, 1)


def generate_exercise(difficulty: int = 2, multiples: bool = True) -> str:
    # Generates an exercise with the given difficulty.
    # Difficulty means number of operations.
    # 1: 1 operation, 2: 2 operations, etc.
    # 2 by default.
    OPERTIONS = ['+', '-', '*', '/']
    operations = [random.choice(OPERTIONS) for _ in range(difficulty)]
    numbers = [generate_random_int_places() for _ in range(difficulty+1)]
    exercise = ''
    for i in range(difficulty):
        exercise += f'{numbers[i]} {random.choice(operations)} '
    exercise += f'{numbers[-1]}'
    return exercise


def generate_exercise_with_solution(difficulty: int = 2) -> str:
    # Generates an exercise with the given difficulty.
    # Difficulty means number of operations.
    # 1: 1 operation, 2: 2 operations, etc.
    # 2 by default.
    numbers = [generate_random_int_places() for _ in range(difficulty+1)]
    operations = ['+', '-', '*', '/']
    exercise = ''
    for i in range(difficulty):
        exercise += f'{numbers[i]} {random.choice(operations)} '
    exercise += f'{numbers[-1]}'
    return exercise, eval(exercise)


if __name__ == '__main__':
    print(generate_random_int_places('2'))
    print(generate_random_multiple_int_places(135))
    print(generate_exercise(2))
    print(generate_exercise_with_solution(2))
