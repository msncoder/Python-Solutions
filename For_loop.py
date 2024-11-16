#print number 1 to 5
# for i in range(1,6):
#     print(i,end="")

#output 1 2 3 4 5

#print square number 1 to 5

# for i in range(1,6):
#     print(i*i,end=" ")

# output 1 4 9 16 25

#print even number 1 to 10

# for i in range(1,11,2):
#     print(i,end=" ")

#output 1 3 5 7 9

#print sum of number 1 to 10
# sum = 0
# for i in range(1,11+1):
#     sum = sum + i
# print(sum)

# output 55

# reverse a word python
# word = "python"
# reversed_word = ""
# for i in range(len(word),0,-1):
#     print(i,end=" ")
#     print(word[i-1])
#     reversed_word += word[i-1]
# print(reversed_word)

# output = nohtyp

#count a vowel in a word
# word = "python"
# vowels = "aeiou"
# for i in word:
#     if i in vowels:
#         print(i+" is a vowel")
# output = o is a vowel

# print a fabonnaci series upto 10 times

# a = 0
# b = 1
# # print(a,end=" ")
# # print(b,end=" ")
# for i in range(10):
#     c = a+b
#     print(a,end=" ")
#     a = b
#     b = c
# output = 0 1 1 2 3 5 8 13 21 34

#calculate a factorial of a number 5
# fact = 1
# for i in range(1,6):
#     print(i)
#     fact *= i
# print(fact)
# output = 120

# count accurances in each character in a word
# word = "python programming"
# d = {}
# for i in word:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# write a program to check a number is prime or not
# num = 7
# for i in range(2,int(num ** 0.5)+1):
#     if num % i == 0:
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break