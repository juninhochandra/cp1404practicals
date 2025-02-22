from random import randint

NUMBERS_PER_LINE = 6
ALIGNMENT = 2
MIN_RANGE = 1
MAX_RANGE = 45

total_quick_picks = int(input("How many quick picks? "))

for i in range(total_quick_picks):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        ran_num = randint(MIN_RANGE, MAX_RANGE)
        while ran_num in numbers:
            ran_num = randint(MIN_RANGE, MAX_RANGE)
        numbers.append(ran_num)
    numbers.sort()
    print(" ".join(f"{number:{ALIGNMENT}}" for number in numbers))