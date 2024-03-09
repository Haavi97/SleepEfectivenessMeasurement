from datetime import datetime as dt

from random_exercise import generate_exercise_with_solution
from data_utils import save_to_csv, append_column_to_csv, save_headers_to_csv
import os

daily_routine_filename = 'daily_routine.csv'

def start_configuration():
    if not os.path.exists(daily_routine_filename):
        save_headers_to_csv(daily_routine_filename)


def measure_exercise() -> float:
    start = dt.now()
    exercise, solution = generate_exercise_with_solution()
    print('Solve the following exercise:')
    print(exercise)
    answer = None
    incorrect = -1
    while answer != int(solution):
        incorrect += 1
        try:
            answer = int(input('Your answer here: '))
        except KeyboardInterrupt:
            break
        except:
            print('Please, write a valid number')
    print('Congrats! That\'s the correct answer')
    finish = dt.now()
    delta_time = (finish-start).seconds
    print(f'Your solving time: {delta_time} seconds')
    return delta_time, incorrect


def generate_daily_routine(n: int = 3) -> list:
    times = []
    incorrects = []
    for i in range(n):
        print(f'Exercise {i+1}')
        time, incorrect = measure_exercise()
        times.append(time)
        incorrects.append(incorrect)
        print()
    avg_time = sum(times)/len(times)
    append_column_to_csv([dt.now(), sum(times), avg_time, n, n, sum(incorrects)],
                  daily_routine_filename)
    print(f'Your average solving time is: {avg_time} seconds')
    return times


def print_menu():
    print('Welcome to the exercise generator')
    print('1. Generate exercise')
    print('2. Measure exercise')
    print('3. Daily routine')
    print('4. Exit')


if __name__ == '__main__':
    start_configuration()
    while True:
        try:
            print_menu()
            option = input(
                'Write the number of the option you want to execute: ')
            if option == '1':
                exercise, solution = generate_exercise_with_solution()
                print('Exercise:')
                print(exercise)
                print('Solution:')
                print(solution)
            elif option == '2':
                measure_exercise()
            elif option == '3':
                generate_daily_routine()
            elif option == '4':
                print('Goodbye!')
                break
            else:
                print('Please, write a valid option')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        except:
            print('An error occurred, please try again')
