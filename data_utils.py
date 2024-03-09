import csv


def save_to_csv(data: list, filename: str, mode: str = 'w') -> None:
    with open(filename,
              mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"Data saved to {filename}")


def append_column_to_csv(data: list, filename: str) -> None:
    save_to_csv([data], filename, mode='a')
    print(f"Data appended to {filename}")


def save_headers_to_csv(filename: str) -> None:
    headers = ['timestamp', 'total_time', 'avg_time',
               'n_exercises', 'n_correct', 'n_incorrect']
    save_to_csv([headers], filename)
    print(f"Headers saved to {filename}")


if __name__ == '__main__':
    save_headers_to_csv('test.csv')
    append_column_to_csv([['a', 'b'], ['c', 'd']], 'test.csv')
