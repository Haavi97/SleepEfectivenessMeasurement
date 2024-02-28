from datetime import datetime as dt
from random_exercise import generate_exercise_with_solution


def measure_exercise() -> float:
    start = dt.now()
    exercise, solution = generate_exercise_with_solution()
    print('Solve the following exercise:')
    print(exercise)
    answer = None
    while answer != int(solution):
        try:
            answer = int(input('Your answer here: '))
        except:
            print('Please, write a valid number')
    print('Congrats! That\'s the correct answer')
    finish = dt.now()
    delta_time = (finish-start).seconds
    print(f'Your solving time: {delta_time} seconds')
    return delta_time


if __name__ == '__main__':
    measure_exercise()
