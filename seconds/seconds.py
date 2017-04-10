def seconds(num_list):
    number_list = num_list
    new_list = []

    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)

    return new_list
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
