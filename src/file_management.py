# create and open

my_file = open('text.txt', 'a') # file will be created if it doesn't exist

# write

my_file.write('''Hello!
this is a
text test''')

# read

with open('text.txt', 'r') as reader:
    print(reader.read()) # use .readline to read a single line

# close

my_file.close()