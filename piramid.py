print("Size:")
n = int(input())
a = [0] * n
for i in range(1, n+1):
    for k in range(1, i+1):
        print(k, end="")
    while (i-1):
        print(i-1, end="")
        i -= 1
    print(end='\n')

