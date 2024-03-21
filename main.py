from datetime import datetime as dt

from random_exercise import generate_exercise_with_solution
from data_utils import append_column_to_csv, save_headers_to_csv
from db_utils import create_connection, create_records_table, add_record
import os
import json

daily_routine_filename = 'daily_routine.csv'
MAX_SOLVING_TIME = 10
n = 3


def start_configuration(connection=None):
    if not connection:
        connection = create_connection('sem_app.sqlite')
    create_records_table(connection)
    global MAX_SOLVING_TIME, n
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data' + os.sep + daily_routine_filename):
        save_headers_to_csv(daily_routine_filename)
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            MAX_SOLVING_TIME = config['max_solving_time']
            n = config['n']
    except FileNotFoundError:
        if not os.path.exists('config.json'):
            with open('config.json', 'w') as f:
                json.dump({'max_solving_time': MAX_SOLVING_TIME, 'n': n}, f)
    except Exception as e:
        print('An error occurred while reading the configuration file', e, sep='\n')


def measure_exercise() -> float:
    start = dt.now()
    exercise, solution = generate_exercise_with_solution()
    print('Solve the following exercise:')
    print(exercise)
    answer = None
    incorrect = -1
    correct = 0
    delta_time = 0
    while answer != int(solution):
        incorrect += 1
        try:
            answer = int(input('Your answer here: '))
        except KeyboardInterrupt:
            break
        except:
            print('Please, write a valid number')
        delta_time = (dt.now()-start).seconds
        if delta_time >= MAX_SOLVING_TIME:
            correct -= 1
            break
    correct += 1
    print('Congrats! That\'s the correct answer' if correct else
          'You didn\'t solve the exercise. Time is up!')
    print(f'Your solving time: {delta_time} seconds')
    return delta_time, incorrect, correct


def generate_daily_routine(connection, n: int = 3) -> list:
    times = []
    incorrects = []
    corrects = []
    for i in range(n):
        print(f'Exercise {i+1}')
        time, incorrect, correct = measure_exercise()
        # print(f'Exercise {i+1} solved in {time} seconds. Correct: {correct}, Incorrect: {incorrect}')
        times.append(time)
        incorrects.append(incorrect)
        corrects.append(correct)
        print()
    notes = input('Enter any notes: ')
    avg_time = sum(times)/len(times)
    add_record(connection, (sum(times), avg_time, ', '.join(
        map(str, times)), n, sum(corrects), sum(incorrects), notes))
    append_column_to_csv([dt.now(), sum(times), avg_time, n, sum(corrects), sum(incorrects), notes],
                         daily_routine_filename)
    print(f'Your average solving time is: {avg_time} seconds')
    return times


def settings():
    print('Settings')
    print('1. Change the maximum solving time')
    print('2. Change the number of exercises in the daily routine')
    print('3. Back')
    option = input('Write the number of the option you want to execute: ')
    config = {}
    with open('config.json', 'r') as f:
        config = json.load(f)
    if option == '1':
        MAX_SOLVING_TIME = int(input('Write the new maximum solving time: '))
        config['max_solving_time'] = MAX_SOLVING_TIME
        with open('config.json', 'w') as f:
            json.dump(config, f)

    elif option == '2':
        n = int(input('Write the new number of exercises in the daily routine: '))
        config['n'] = n
        with open('config.json', 'w') as f:
            json.dump(config, f)
    elif option == '3':
        return
    else:
        print('Please, write a valid option')


def print_menu():
    print('Welcome to the exercise generator')
    print('1. Generate exercise')
    print('2. Measure exercise')
    print('3. Daily routine')
    print('4. Settings')
    print('5. Exit')


if __name__ == '__main__':
    connection = create_connection('sem_app.sqlite')
    start_configuration(connection)
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
                generate_daily_routine(connection, n=n)
            elif option == '4':
                settings()
            elif option == '5':
                print('Goodbye!')
                break
            else:
                print('Please, write a valid option')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        except:
            print('An error occurred, please try again')
