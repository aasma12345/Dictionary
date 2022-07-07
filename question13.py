from collections import Counter
from curses import keyname
my_dict = my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
k = Counter(my_dict)
high = k.most_common(3)
for i in high:
   print([i])
