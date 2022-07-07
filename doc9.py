# Q9.Write a Python program to iterate over dictionaries using for loops.






# dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
# # for key in dt:
# #     print(key, dt[key])



# for key, value in dt.items():
#     print(key, value)



num=int(input("enter the number: "))
num1=int(input("enter the number: "))
num2=int(input("enter the number: "))
if num<num1 and num>num2:
    print(num)
elif num1<num and num1>num2:
    print(num1)
else:
    print(num2)
