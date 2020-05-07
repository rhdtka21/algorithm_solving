# [파이썬 | 2019 카카오 인턴쉽] 불량 사용자

def solution(user_id, banned_id):
    ansSet = set()
    def solve(depth, banned_num):
        if depth == banned_num:
            temp = ''
            for k, v in check.items():
                if v == 1:
                    temp += k
            ansSet.add(temp)
            return

        each_banned = banned_id[depth]
        for each_candi in candi[each_banned]:
            if check[each_candi] == 0:
                check[each_candi] = 1
                solve(depth+1, banned_num)
                check[each_candi] = 0

    candi = {}
    check = {}
    for each_banned in banned_id:
        candi[each_banned] = []
        for each_user in user_id:
            flag = True
            if len(each_banned) == len(each_user):
                #print(each_banned, each_user)
                for i in range(len(each_banned)):
                    if each_banned[i] == each_user[i] or each_banned[i] == '*':
                        continue
                    else:
                        flag = False
                        break
            else:
                flag = False
            if flag:
                candi[each_banned].append(each_user)
                check[each_user] = 0
    
    #print(check)
    solve(0, len(banned_id))
    #print(ansSet)
    answer = len(ansSet)
    return answer

# 테스트용 input output 정의

# 5 4
# frodo
# fradi
# crodo
# abc123
# frodoc
# fr*d*
# *rodo
# ******
# ******

# 5 2
# frodo
# fradi
# crodo
# abc123
# frodoc
# fr*d*
# abc1**

N, M = map(int, input().split())
user_id = []
banned_id = []
for _ in range(N):
    user_id.append(input())
for _ in range(M):
    banned_id.append(input())
solution(user_id, banned_id)