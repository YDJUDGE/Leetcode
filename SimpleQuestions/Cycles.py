#1
# def add_underscores(word:
#     my_string = "_"
#     for k in range(len(word)):
#         my_string += word[k] + "_"
#     return my_string
# print(add_underscores("Python")))

#2
# a = int(input())
# b = int(input())
# for i in range(a+1,b):
#     print(i)

#3
# a = int(input())
# b = int(input())
# for i in range(a+1, b):
#     if i % 5 == 0:
#         print(i)

#4
# a = int(input())
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list:
#     print(a * i)

#5
# score = []
# for i in range(4):
#     score.append(int(input("score: ")))
#     print(sum(score))

#6
# while True:
#     a = input()
#     if a == "end":
#         break

#7 Дано натуральное число. Определить сумму цифр в нем.
# a = int(input())
# count = 0
# my_list=[]
# for i in range(count, a):
#     count+=1
#     my_list.append(int(i))
#     print(sum(my_list))

#8(неверно) Пользователь вводит число n и цифру a. Определить, сколько раз цифра встречается в числе. (не использовать метод count)
# n = int(input())
# a = int(input())
# my_list = []
# count = 0
# for i in range(n):
#     my_list.append(i)
#     if i == a:
#         count += 1
# print(my_list)
# print(count)

#2nd Variant ?
# n = int(input())
# a = int(input())
# my_list = []
# count = 0
# for i in range(n):
#     my_list.append(str(i))
#     x = "".join(my_list)
#     if str(a) == x:
#         count+=1
# print(x)
# print(x.count(str(a)))

#9
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <= 5:
#         print(i)

#10
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# new_list = []
# for i in a:
#     for g in b:
#         if i == g:
#             new_list.append(i)
#             print(new_list)

#11
# dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(sorted(dict))
# print(sorted(dict, reverse=True))

#12 Задача - обЪеденить 3 словаря
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# combined_intermediate = dict_a.copy()
# combined_intermediate.update(dict_b)
# combined_finite = combined_intermediate.copy()
# combined_finite.update(dict_c)
# print(combined_finite)

