def generate_list():
    my_list = []
    for count in range(1, 16):
        my_list.append(count)
    return my_list

def duplicate_generate_list(my_list):
    duplicated_list = []
    for item in my_list:
        for count in range(2):
            duplicated_list.append(item)
    return duplicated_list

def remove_duplicates(duplicated_list):
    transformed_list = list(set(duplicated_list))
    return transformed_list

def add_third_element(lst):
    total = 0
    for count, num in enumerate(lst):
        if (count + 1) % 3 == 0:
            total += num
    return total

def unique_numbers(numbers):
    numbers_set = set()
    for number in numbers:
        numbers_set.add(number)
    return numbers_set

def sum_collection(collection):
    total = 0
    for item in collection:
        total += item
    return total

def remove_item(set, number):
    if number in set:
        set.remove(number)
        return number
    else:
        return None

def find_intersection(set1, set2):
    return set(set1) & set(set2)

def find_union(set1, set2):
    return set1 | set2

def subset(set1, set2):
    return set1.issubset(set2)

def remove_first_element(set1, set2):
    set1.clear()
    return set1, set2

def maximum_and_minimum(set1, set2):
    max_value = max(set2)
    min_value = min(set2)
    return set1, set2, max_value, min_value

def set_length(set1):
    count = 0
    for element in set1:
        count += 1
    return count




#numbers = unique_numbers()
#print("unique numbers are: ",  numbers)


#print(generate_list())
#print(duplicate_generate_list(generate_list()))
#print(remove_duplicates(duplicate_generate_list(generate_list())))
