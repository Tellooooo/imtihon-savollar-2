A = []
N = int(input("N = "))
if (N >= 100000000) and (N < 1000000000):
    A.append(N)
    print(A)
    if A[0] == 0:
        print("parol xato")
    else:
        print("parol togri = " , A)
else:
    print("parol xato")