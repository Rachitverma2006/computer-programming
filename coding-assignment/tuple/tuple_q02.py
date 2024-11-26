#Create a function that returns the intersection of two tuples.

def tuple_intersection(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


print(tuple_intersection((1, 2, 3), (2, 3, 4)))
