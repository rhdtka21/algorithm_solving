# [파이썬 | 2020 KAKAO BLIND RECRUITMENT | 문제 1] 문자열 압축

def solution(s):
    size = len(s)
    answer = size + 1
    if size == 1:
        return 1

    for window in range(1, size //2  + 1):
        tempList = []
        tempStr = ''
        cnt = 1
        for i in range(0, size, window):
            if s[i:i+window] == s[i+window:i+2*window]:
                cnt += 1
            else:
                tempList.append([s[i:i+window], cnt])
                cnt = 1
        for char, cnt in tempList:
            if cnt > 1:
                tempStr += str(cnt) + char
            else:
                tempStr += char
        #print(tempStr)
        answer = min(answer, len(tempStr))
                
    #print(answer)
    return answer

S = input()
solution(S)