# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# ----------------------------------


# n = int(input("Enter a number: "))
# result = []
# fact = 1

# for i in range(1, n + 1):
#     fact *= i
#     result.append(fact)

# print(",".join(map(str, result)))


# ----------------------------------


# n = int(input("Enter a number "))
# result = []
# fact = 1

# for i in range (1, n+1):
#     fact *= i
#     result.append(fact)

# print(",".join(map(str, result)))


# ----------------------------------


# n = int(input("Enter a number "))
# fact = 1

# for i in range (1, n+1):
#     fact *= i
# print(fact)


# ----------------------------------

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print(fact(x))


def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)
x = int(input("Enter a number "))
print(fact(x))