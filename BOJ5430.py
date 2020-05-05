# [파이썬 | BOJ | 5430] AC

T = int(input())
for t in range(T):
    p = input()
    N = int(input())
    if N > 0:
        lst = list(map(int, input()[1:-1].split(',')))
    else:
        _ = input()
        lst = []

    left, right = 0, N-1
    rcnt = 0
    dcnt = 0
    for func in p:
        if func == 'R':
            rcnt += 1
        elif func == 'D':
            if rcnt % 2:                             #지금까지 R이 홀수개 나왔으면
                right -= 1                           #뒤에서 하나 지움
            else:
                left += 1                            #앞에서 하나 지움
            dcnt += 1

    isReverse = True if rcnt % 2 else False         #R이 홀수개 있으면 역순
    if left < right+1:
        lst = lst[left:right+1]
    else:
        lst = []
    if not lst:                                     #lst가 비어있을때
        if dcnt <= N:                               #숫자 개수보다 더 많이 지웠으면 에러
            print('[]')
        else:
            print('error')
        continue

    ans = '['
    if isReverse:
        for l in reversed(lst):
            ans += str(l) + ','
    else:
        for l in lst:
            ans += str(l) + ','
    ans = ans[:-1] + ']'
    print(ans)