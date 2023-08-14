import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)

    numbers.sort()
    return numbers

print(generate_lotto_numbers())