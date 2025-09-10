# def findMissingNumbers(n):
#     numbers = set(n)
#     length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output
    
# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
# print(findMissingNumbers(listOfNumbers))


# def findMissingNumbers (n):
#     numbers = set(n)
#     output = []
#     for i in range (1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output

# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 14, 16]
# print(findMissingNumbers(listOfNumbers))



# def missingNumber(n):
#     numbers = set(n)
#     output = []
#     for i in range (1, n[-1]):
#         if i not in n:
#             output.append(i)
#     return output

# realNumbers = [1,2,3,4,6,9,10,11,14]
# print(missingNumber(realNumbers))




def missingNumbers(a):
    output = []
    for i in range (1, a[-1]):
        if i not in a:
            output.append(i)
    return output


listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(missingNumbers(listOfNumbers))