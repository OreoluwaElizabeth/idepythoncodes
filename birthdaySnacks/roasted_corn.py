import random

def generate_numbers():
    random.seed(42)
    numbers = []
    for count in range(10):
        numbers.append(random.randint(1, 50))
    return numbers

def count_numbers(numbers):
    count = 0
    for num in numbers:
        count += 1
    return count

def sum_even_numbers(numbers):
    even_sum = 0
    for count in range(10):
        if count % 2 == 0:
            even_sum += numbers[count]
    return even_sum

def odd_even_numbers(numbers):
    odd_sum = 0
    for count in range(10):
        if count % 2 != 0:
            odd_sum += numbers[count]
    return odd_sum

def product(numbers):
    product = 1
    for count in range(10):
        if (count + 1) % 3 == 0:
            product *= numbers[count]
    return product

def average(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    average = total_sum / 10
    return average

def largest_elements(numbers):
    largest_elements = numbers[0]
    for num in numbers:
        if num > largest_elements:
            largest_elements = num
    return largest_elements

def smallest_elements(numbers):
    smallest_elements = numbers[0]
    for num in numbers:
        if num < smallest_elements:
            smallest_elements = num
    return smallest_elements


