# Given a list of numbers, print the largest of the numbers.

numbers = [7, 21, 4, 33, -456, 8, 99, 1, 12340, 2, 79, 88, 124, 90]

maximum = 0
for number in numbers:
    if number > maximum:
        maximum = number
print(f'The maximum number in the list is {maximum}')