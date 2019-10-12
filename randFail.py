from random import randint

numerator = randint(0, 100)
denominator = randint(0,10)

while True:
    if denominator == 0:
        print("I fail now")
    print(numerator / denominator)
    numerator = randint(0, 100)
    denominator = randint(0, 100)