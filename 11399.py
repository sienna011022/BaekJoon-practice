N = int(input())
status =0
sum = 0
#일렬로 받고 이걸 리스트화 시키고 싶으면 다음과 같이 작성하면 된다.
line = list( map(int,input().split()))
line.sort()
for i in range(N):
    status += line[i]
    sum += status
print(sum)








