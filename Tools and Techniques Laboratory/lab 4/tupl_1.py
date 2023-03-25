# Create a tuple with different data types
#Create a tuple with different data types
my_tuple = (1, "hello", 3.14, ['a', 'b', 'c'])
print(my_tuple)


# modify

def create_tuple(*args):
    return tuple(args)

my_tuple = create_tuple(1, "hello", 3.14, ['a', 'b', 'c'])
print(my_tuple)
