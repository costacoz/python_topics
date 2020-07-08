import math, random, statistics

print(f'{math.pi:,.3}')

animal = random.choice(['dog', 'cat', 'hamster']) # Random choice from list
print(animal)

numbers = random.sample(range(10), 5) # Samples from some range
print(numbers)

some_float = random.random() # Random float
print(some_float)

some_integer = random.randrange(5) # Random number from 0 to 4
print(some_integer)

stats_data = [1, 2, 3, 4, 5, 6]
print(f'Mean: {statistics.mean(stats_data)}')
print(f'Median: {statistics.median(stats_data)}')
print(f'Variance: {statistics.variance(stats_data)}')