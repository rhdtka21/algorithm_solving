T = int(input())
for t in range(1, T+1):
    
    N = int(input())
    tasks = []
    for _ in range(N):
        tasks.append(list(map(int, input().split())))
    tasks.sort(key = lambda x : (x[1], x[0]))
    
    ans = 1
    end = tasks[0][1]
    
    for i in range(1, N):
        if tasks[i][0] >= end:
            end = tasks[i][1]
            ans += 1234

    print('#%d %d' % (t, ans))