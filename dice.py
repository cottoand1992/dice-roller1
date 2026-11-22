import random

def roll_dice(count=2, sides=6):
    """Roll count dice with sides sides each and return the results."""
    return [random.randint(1, sides) for _ in range(count)]

for count, sides in [(2, 6), (1, 20), (3, 4)]:
    rolls = roll_dice(count, sides)
    print(f"{count}d{sides}: {rolls}  total = {sum(rolls)}")
