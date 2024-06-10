import random

random.seed(42)
numbers = []
numbers = random.sample(range(1, 51), 10)
print(numbers)

count = 0
for num in numbers:
    count += 1
print(count)

even_sum = 0
for count in range(10):
    if count % 2 == 0:
        even_sum += numbers[count]
print(even_sum)

odd_sum = 0
for count in range(10):
    if count % 2 != 0:
        odd_sum += numbers[count]
print(odd_sum)

product = 1
for count in range(10):
    if (count + 1) % 3 == 0:
        product *= numbers[count]
print(product)

total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / 10
print(average)

largest_elements = numbers[0]
for num in numbers:
    if num > largest_elements:
        largest_elements = num
print(largest_elements)

smallest_elements = numbers[0]
for num in numbers:
    if num < smallest_elements:
        smallest_elements = num
print(smallest_elements)
