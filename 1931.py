N = int(input())
schedule_list = list()

for i in range(N):
        a,b = map(int,input().split())
        schedule_list.append([a,b])
#오름 차순으로 비교해서 sort해줌
schedule_list = sorted(schedule_list,key = lambda x : (x[0],x[1]))

count = list()
count.append(schedule_list[0])

for i in (range(1,N)):
   if count[-1][-1] <= schedule_list[i][0]:
     count.append(schedule_list[i])

print(len(count))









