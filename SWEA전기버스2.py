# SWEA 전기버스2

def solve(num, charge, cnt):
    global ans
    if cnt > ans:
        return

    if num == N:
        if ans > cnt:
            ans = cnt
        return
    #print(num, charge, cnt)
    
    # 지금 충전량이 배터리[정류장번호]보다 작으면 바꿔도 되고 안바꿔도 된다.
    if charge < battery[num] and charge > 0:
        solve(num+1, battery[num]-1, cnt+1)
        solve(num+1, charge-1, cnt)

    # 충전량이 0이면 무조건 바꾼다
    elif charge == 0:
        solve(num+1, battery[num]-1, cnt+1)

    # 지금 충전량이 배터리[정류장번호]보다 크거나 같으면 바꿀 이유가없다.
    elif charge >= battery[num]:
        solve(num+1, charge-1, cnt)

T = int(input())

for t in range(1, T+1):
    ans = 999999
    battery = list(map(int, input().split()))
    N = battery[0]
    solve(2, battery[1]-1, 0)
    print("#%d %d" %(t, ans))
    
