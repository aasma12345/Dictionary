# Q11.Write a Python script to merge two Python dictionaries


dic1={1:10, 2:20}
dic2={3:30, 4:40}

dict={}
for d in dic1,dic2:
    dict.update(d)
print(dict)