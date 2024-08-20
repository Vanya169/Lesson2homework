number = int(input("Enter number: "))
n1 = number // 1000 #1"
n11 = number % 100 #34
n12 = number // 100 #12
n2 = n12 % 10
n3 = n11 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)


nnumber = int(input("Enter nnumber: "))
# nnumber 54321
nn1 = nnumber // 10000 #5
nn11 = nnumber // 1000 #54
nn12 = nnumber % 1000 #321
nn2 = nn11 % 10 #4
nn13 = nn12 % 100 #21
nn3 = nn12 // 100 #3
nn4 = nn13 // 10 #2
nn5 = nn13 % 10 #1
nnn5 = nn5 * 10000
nnn4 = nn4 * 1000
nnn3 = nn3 * 100
nnn2 = nn2 * 10
nnn1 = nn1 * 1
result = nnn5 + nnn4 + nnn3 + nnn2 + nnn1
print(result)
