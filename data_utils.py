import csv

def save_to_csv(data, filename):
    with open(filename,
                'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    print(f"Data saved to {filename}")


if __name__ == '__main__':
    save_to_csv([['a', 'b'], ['c', 'd']], 'test.csv')
