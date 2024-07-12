num_rolls = 25
six_count = 0
one_count = 0
double_six_count = 0
last_rool = None
import random
for _ in range(num_rolls):
    roll= random.randint(1, 6)
    if roll == 6:
       six_count += 1
       if last_roll == 6:
           double_six_count += 1
    elif roll == 1:
        one_count += 1
    last_roll = roll

print(f"Rolled a 6: {six_count} times")
print(f"Rolled a 1: {one_count} times")
print(f"Rolled two 6s in a row: {double_six_count} times")

