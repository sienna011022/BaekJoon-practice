N = int(input())
line = list(map(int, input().split()))
price = list(map(int, input().split()))
line_sum = 0
sum = 0
max = 0

for i in range(len(line)):
    line_sum += line[i]

sort_price = list()

for i in range(N-1):
    sort_price.append(price[i])
    sort_price.sort()

max = sort_price[0]
max = price.index(max)

for i in range(max):
    sum += price[i] * line[i]
    line_sum -= line[i]

sum += price[max] * line_sum

print(sum)




