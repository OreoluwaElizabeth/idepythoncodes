def fibonacci(ore):
    first_number = 0
    second_number = 1
    next_number = first_number

    for count in range(ore):
        print(next_number,end=',')
        first_number, second_number = second_number,next_number
        next_number = first_number + second_number

fibonacci(11)
