# Create a function that takes a filename as string parameter,
# counts the occurances of the letter "a", and returns it as a number.
# If the file does not exist, the function should return 0 and not break.

my_file = open('afile.txt', 'r')

def count_as(file_name):
    try:
        my_file = open(file_name, 'r')
        text = my_file.read()
        occcurances = text.count('a')
        return text
    except FileNotFoundError:
        return 0






print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
