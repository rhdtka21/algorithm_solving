# [파이썬 | 2020 KAKAO BLIND RECRUITMENT | 문제 2] 괄호 변환

def rightOrBalance(string): #right True / Balance False
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif not stack:
                stack.append(')')
            elif stack and stack[-1] == ')':
                stack.append(')')
    if not stack:
        return True
    else:
        return False

def solve(p):
    l, r = 0, 0
    u = ''
    v = ''
    
    if p == '':
        return ''
    else:
        for i in range(len(p)):
            if p[i] == '(':
                l += 1
                u += '('
            elif p[i] == ')':
                r += 1
                u += ')'
            if l == r:
                break
        v = p[i+1:]
        if rightOrBalance(u):
            return u + solve(v)
        else:
            tail = ''
            for char in u[1:-1]:
                if char == '(':
                    tail += ')'
                else:
                    tail += '('
            return '(' + solve(v) + ')' + tail

def solution(p):
    answer = solve(p)
    #print(answer)
    return answer