N, K = map(int, input().split())
coin_list = list()
for i in range(N):
    coin_list.append(int(input()))

sum = 0
for i in reversed(range(N)):
            #K보다 값이 크다면 어차피 몫이 0이라서 제외됨
            count = K // coin_list[i]
            K -= coin_list[i] * count
            sum += count

print(sum)








