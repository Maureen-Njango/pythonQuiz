#Write a function create_tuple that takes any number of arguments and returns them as a tuple.
def create_turple(*args):
    return args

#Given a tuple t, write a function access_elements that returns the first and last elements of the tuple.
def access_elements(*args):
    print(args[1])
    print(args[-1])

  #Write a function tuple_length that returns the length of a given tuple.
def find_length(*args):
    print(len(args))

#Write a function concat_tuples that concatenates two tuples.
def add_two_tuples(tuple1, tupple2):
    return tuple1+tupple2
    
#Write a function count_elements that counts the number of times a specific element appears in a tuple.
def count_occurrence(tuple,element):
    count = 0
    for i in tuple:
        if i == element:
            count +=i
            return count
        
#Write a function find_index that finds the index of the first occurrence of a specific element in a tuple. If the element is not found, return -1.

#Write a function dict_from_tuples that takes a list of tuples, where each tuple contains a key-value pair, and returns a dictionary.
def dic_from_tuples(tuple):
    b= dict(tuple)
    return b
  