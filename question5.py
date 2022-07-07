






# from itertools import zip_longest
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d1=zip_longest(list1,list2)
# print (d1)
# print (dict(d1))


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
dict={}
i=0
while i<len(list1):
    dict[list1[i]]=list2[i]
    i=i+1
print(dict)


