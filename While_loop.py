# # print number from 10 to 15
# a = 10
# while a <= 15:
#     print(a,end=' ')
#     a = a + 1
#output: 10 11 12 13 14 15

# print cubes of numbers from 1 to 5
# a = 1
# while a <= 5:
#     # print(a**3,end=' ')
#     print(a*a*a,end=' ')
#     a = a + 1

# output: 1 8 27 64 125

# print odd numbers from 1 to 10
# a = 1
# while a <= 10:
#     if a % 2 != 0:
#         print(a,end=' ')
#     a = a + 1

# output: 1 3 5 7 9

# calculate the product of number from 1 to 5

# a = 1
# product = 1
# while a <=5:
#     product*=a
#     a += 1
# print(product)

# output: 120


# Reverse Each word in a sentence

# sentence = "I Love Python Programming"
# words = sentence.split()

# while words:
#     word = words.pop()
#     # print(word)
#     print(word[::-1],end=' ')

# output: I evoL nohtyP gnimmargorP

# # count consonants and vowels in a string

# count = 0 
# vowels = 'aeiou'
# word = 'learning'
# index = 0

# while index < len(word):
#     if word[index] in vowels:
#         count += 1
#     index += 1
# print(count)


# print the first 5 multiplies of 3
# a = 1
# while a <= 10:
#     # print(a*3,end=' ')
#     if a % 3 == 0:
#         print(a,end=' ')
#     a += 1

# write a program to calculate 3 to the power of 4
# a = 1
# b = 1
# while a <= 4:
#     b*=3
#     a += 1

# print(b)

#check if number is perfect is square or not

# number  = 9

# while number > 0:
#     if number ** 0.5 == int(number ** 0.5):
#         print(number ** 0.5 == int(number ** 0.5))
#         print("Perfect Square")
#         break
#     else:
#         print("Not a perfect square")
#         break

#count occurence of a character in a string
# a = "hello"
# b = {}
# index = 0

# while index < len(a):
#     if a[index] in b:
#         b[a[index]] += 1
#     else:
#         b[a[index]] = 1
#     index += 1
# print(b)
