# dict1 ={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# dict_values = sorted(dict1.values())
# dict_dict = {}

# for i in dict_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             dict_dict[k] = dict1[k]
#             break

# print(dict_dict)


dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dict_values = sorted(dict.values())
my_dict = {}
for i in dict_values:
    for k in dict.keys():
        if dict[k] == i:
            my_dict[k] = dict[k]
            break
print(my_dict)


 


# dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# l=list(dict.items())   
# l.sort()           
# l=list(dict.items())
# l.sort(reverse=True)
# print('Descending order is',l)
# dict=dict(l)  
# print("Dictionary",dict)


# a={"key":"newyear",
# "year":2022,
# "univercity":"ignou"
# }
# for i in (a):
#     a["year"]=2021
# print(a)
