from time import time
start = time()

word = "Artificial Intelligence is a monster"
letter = word.split()
a = " "

for i in letter:
    a += str(i[0]).upper()
print(a)

end = time()

result = end - start
print("The exicution time is ", result)