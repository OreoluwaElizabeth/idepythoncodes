def even_numbers(lst):
    even_num = []
    for number in lst:
        if number % 2 == 0:
            even_num.append(number)
    return even_num

numbers = []
for count in range(1,51):
    numbers.append(count)
even = even_numbers(numbers)
print(even)
