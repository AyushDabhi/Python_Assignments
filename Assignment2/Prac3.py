user_input = int(input())
b = list(map(int, input().split(' ')))
for i in b:
    d = b.count(i)
    if d == 1:
        print(i)