list=[
    {"first":"1"},
    {"third": "1"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}
    ]
i=0
j=0
list1=[]
while i<len(list):
    for j in list[i]:
        if list[i][j] not in list1:
            list1.append(list[i][j])
        i=i+1
print(list1)









# print("Original List: ",list)
# u_value = set( val for dict in list for val in dict.values())
# print("Unique Values: ",u_value)
# list=[]
# list.append(u_value)

