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


def print_menu():
    print('Welcome to the exercise generator')
    print('1. Generate exercise')
    print('2. Measure exercise')
    print('3. Exit')


if __name__ == '__main__':
    while True:
        try:
            print_menu()
            option = input('Write the number of the option you want to execute: ')
            if option == '1':
                exercise, solution = generate_exercise_with_solution()
                print('Exercise:')
                print(exercise)
                print('Solution:')
                print(solution)
            elif option == '2':
                measure_exercise()
            elif option == '3':
                print('Goodbye!')
                break
            else:
                print('Please, write a valid option')
        except:
            print('An error occurred, please try again')
