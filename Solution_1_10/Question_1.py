ans = []

for num in range(2000, 3201):
    if (num % 7 ==0) and (num % 5 != 0):
        ans.append(str(num))

print(','.join(ans))