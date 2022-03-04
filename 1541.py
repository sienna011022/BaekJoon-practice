arr = input().split('-')
s = 0
for i in arr[0].split("+"):
    s += int(i)
for j in arr[1:]:
    for t in j.split("+"):
        s -= int(t)
print(s)



