import random


def generate_random_int_places(n: int = 3) -> int:
    # Generates a random integer with maximum n places.
    # n=3 by default. On failure 3 is used.
    try:
        return random.randint(1, 10**n)
    except:
        print(
            'Error in generate_random_int_places.\n'
            f'Returning with n=3.\nGiven n: {n}\n'
            f'n type: {type(n)}')
        return random.randint(1, 10**3)


def generate_random_multiple_int_places(multiple: int, n: int = 3) -> int:
    # Generates a random integer with maximum n places.
    # n=3 by default. On failure 3 is used.
    try:
        generated = random.randrange(0, 10**n, multiple)
        return generated if generated else generate_random_multiple_int_places(multiple, n)
    except:
        print(
            'Error in generate_random_multiple_int_places.\n'
            f'Returning with multiple=1.\nGiven multiple: {multiple}\n'
            f'multiple type: {type(multiple)}\n'
            f'Returning with n=3.\nGiven n: {n}\n'
            f'n type: {type(n)}')
        generated = random.randrange(0, 10**3, multiple)
        return generated if generated else generate_random_multiple_int_places(multiple, n)

def get_random_operation(exclude: str = None) -> str:
    OPERATIONS = ['+', '-', '*', '/']
    try:
        if exclude:
            OPERATIONS.remove(exclude)
    except:
        print('Invalid exclude value in get_random_operation')
        pass
    return random.choice(OPERATIONS)

def generate_exercise(difficulty: int = 2, multiples: bool = True) -> str:
    # Generates an exercise with the given difficulty.
    # Difficulty means number of operations.
    # 1: 1 operation, 2: 2 operations, etc.
    # 2 by default.
    # Multiples means if the division should be a multiple of the divisor.
    OPERATIONS = ['+', '-', '*', '/']
    operations = [random.choice(OPERATIONS)]
    for _ in range(difficulty-1):
        operations.append(get_random_operation(operations[-1]))
    numbers = [generate_random_int_places(difficulty)]
    exercise = ''
    for operation in operations:
        exercise = f'{operation} {numbers[-1]} {exercise}'
        if operation == '/' and multiples:
            numbers.append(generate_random_multiple_int_places(
                numbers[-1], difficulty+1))
        elif operation == '*':
            numbers[-1] = generate_random_int_places(difficulty - 1)
            numbers.append(generate_random_int_places(difficulty))
        else:
            numbers.append(generate_random_int_places(difficulty))
    return f'{numbers[-1]} {exercise}'


def generate_exercise_with_solution(difficulty: int = 2, multiples: bool = True) -> str:
    exercise = generate_exercise(difficulty, multiples)
    return exercise, eval(exercise)


if __name__ == '__main__':
    # print(generate_random_int_places('2'))
    # print(generate_random_multiple_int_places(135))
    # print(generate_exercise(2))
    print(generate_exercise_with_solution(2))
