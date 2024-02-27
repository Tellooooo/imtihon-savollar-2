import random



N = int(input("N = "))
A = []
for i in range(1 , N + 1):
    z = random.randint(1 , N)
    A.append(z)
print(A)
print(max(A))