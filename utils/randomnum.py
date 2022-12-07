import random


def random_numbers(start =1,stop = 82):
    return(random.randrange(1, stop = 82)for item in range(1, 16))

obj = random_numbers()

for i in range(1, 15):
    print(next(obj))


print(__name__)
