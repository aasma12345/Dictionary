# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
dict_values = sorted(dict.values())
my_dict = {}
for i in dict_values:
    for k in dict.keys():
        if dict[k] == i:
            my_dict[k] = dict[k]
            break
print(my_dict)