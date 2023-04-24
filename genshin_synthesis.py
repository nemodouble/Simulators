import random

const_start = 3000000

start_amount = const_start
end_amount = 0

while start_amount > 2:
    start_amount -= 3
    end_amount += 1
    if random.random() < 0.25:
        start_amount += 1
end_amount -= const_start / 3
print(end_amount)

start_amount = const_start
end_amount = 0

while start_amount > 2:
    start_amount -= 3
    end_amount += 1
    if random.random() < 0.1:
        end_amount += 1
end_amount -= const_start / 3
print(end_amount)
