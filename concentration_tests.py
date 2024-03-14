import time
from random_word import RandomWords
r = RandomWords()


def typing_test(length: int = 10):
    text = " ".join([r.get_random_word() for _ in range(length)])
    print("Type the following text:")
    print(text)

    input("Press Enter when you're ready to start...")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    accuracy = calculate_accuracy(text, user_input)
    speed = calculate_speed(user_input, end_time - start_time)

    print("Accuracy: {:.2f}%".format(accuracy))
    print("Speed: {:.2f} characters per minute".format(speed))


def calculate_accuracy(original_text, user_text):
    correct_chars = sum(1 for i in range(
        min(len(original_text), len(user_text))) if original_text[i] == user_text[i])
    accuracy = (correct_chars / len(original_text)) * 100
    return accuracy


def calculate_speed(user_text, time_taken):
    words_typed = len(user_text.split())
    speed = (words_typed / time_taken) * 60
    return speed


if __name__ == "__main__":
    typing_test()
