

#Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.

def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2

tuple1 = (1,2,3)
tuple2 = (4,5,6)

results = concat_tuples(tuple1, tuple2)
print(results)