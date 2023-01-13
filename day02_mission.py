import random

green = random.randint(0, 1)
small = random.randint(0, 1)


if green:
    if small:
        print("pea")
    else:
        print("watermelon")

else:
    if small:
        print("cherry")
    else:
        print("pumpkin")
