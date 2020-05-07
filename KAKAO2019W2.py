# [파이썬 | 2019 카카오 인턴쉽] 튜플

def solution(s):
    answer = []
    S = list(s[2:-2].split('},{'))
    arr = list()
    
    for s in S:
        temp = list(map(int, s.split(',')))
        arr.append(temp)

    for i in range(1, len(arr)+1):
        for ar in arr:
            if len(ar) == i:
                for a in ar:
                    if answer.count(a) == 0:
                        answer.append(a)
    #print(answer)
    return answer
# 테스트용 input output 정의

# {{2},{2,1},{2,1,3},{2,1,3,4}}

s = input()
solution(s)
