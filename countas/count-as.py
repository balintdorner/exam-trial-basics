# Create a function that takes a filename as string parameter,
# counts the occurances of the letter "a", and returns it as a number.
# If the file does not exist, the function should return 0 and not break.

def count_as(file_name):
    try:
        my_file = open(file_name, 'r')
        text = my_file.read()
        occurances_A = text.count('A')
        occurances_a = text.count('a')
        all_occurances = occurances_a + occurances_A
        return all_occurances
    except FileNotFoundError:
        return 0






print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
