# print('string manipulation excersise\nstring concatination is done with + sign\ne.g print("hello"+"jenny")\nnew line can be write with backslash and n.')

# name = int(input("what is your name?"))
# # print('how are you? '+name)
# print(type(name))

# val = int(input())
# print(type(val))
# x = 0
# while(x<5):
#     print("not yet x =" + str(x))
#     x = x + 1
# # print(x)

# num = input()
# res = int(num[0]) + int(num[1])
# print(res)

# height = float(input("Enter your height: "))
# weight = float(input("Enter your weight: "))

# bmi = weight/height**2
# print(f"your height: {height},weight: {weight} and BMI: {bmi}")

# num = int(input())

# if num % 2 == 0 and num > 0:
#     print(num, 'is even number')
# else:
#     print(num, 'is odd number')

# height = int(input("enter your height: "))
# if height>3:
#     age = int(input("enter your age: "))
#     if age<5:
#         print("you can play hide and sike")
#     elif age>10:
#         print("you can play cricket")
# else:
#     print("you height is less than 3 cm")

# for i in range(1,10,2):
#     print(i)

# names = ['mamun','shidul','mizan','tutul','sobuj''rahim','kamal']
# for name in names:
#     print([name])

# name = 'mamun'
# age = 13
# print(f"my name is {name}\nmy age is :{age}")
# print("name: {1} age: {0}".format(name,age))

# num1,num2,num3 = list(input().split())
# print(num1,num2,num3)
# print(type(nums))

# names = ['mamun','shidul','mizan','tutul','sobuj','rahim','kamal']
# # print(names[0:5:3])
# # print(names[0::3])
# names.sort()
# del names([])
# print(names)

# tuple1 = (1,'mamun')
# print(tuple1)
# list1 = [1,2,3]
# list2 = [66,77]
# # list1.append(4)
# # print(list1.pop(2))
# set1 = {1,4,6}
# print(set1.union(list1))

# for i in range(5):
#     print(i)
# 22 33 12 44 66
# heightes = input("Enter heightes: ").split()
# count = 0
# total = 0
# for i in range(len(heightes)):
#     count += 1
#     heightes[i] = int(heightes[i])
#     total += heightes[i]
#     avg = total/count
# print(round(avg))

# from pstats import SortKey

# s = "anagram"
# t = "nagaram"

# sorted_s = sorted(t)
# sorted_t = sorted(s)
# length = len(sorted(s))
# print(length)
# for i in range(length):
#     if(sorted_s[i]!=sorted_t[i]):
#         print(sorted_s[i])
#     else:
#         print("ok")

# nums = [1, 1, 1, 2, 2, 2, 3, 6, 6]
# count = {}
# freq = [[] for i in range(len(nums)+1)]
# for n in nums:
#     count[n] = 1 + count.get(n, 0)
# for n, c in count.items():
#     freq[c].append(n)
# res = []
# for i in range(len(freq)-1, 0, -1):
#     for n in freq[i]:
#         print("i=",i,"n=", n)
#         res.append(n)
#         if(len(res) == 2):
#             break
""" 
"""
# d1 = {'name':'mamun','age':23}
# d2 = d1
# d2['name']='ghum'
# print(d2['name'])
# print(d1['name'])

# l1 = [1,4,5,6,35]
# for i in enumerate(l1):
#     if(i == 2):
#         l1[i] = 66
# print(l1)
# s = "pwwkew"
# x = set()
# for char in s:
#     x.add(char)
# print(x)

# x = 'mamun'
# x[0] = 'v'
# print (x)
person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)