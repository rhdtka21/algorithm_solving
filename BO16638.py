# [파이썬 | BOJ | 16638] 괄호 추가하기 2
 
import sys
from copy import deepcopy
read = sys.stdin.readline
maxAns = sys.maxsize * -1

val = {'(' : 0, ')' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2}

def case(check, depth):
    if depth == opNum:
        solve(check)
        return

    if depth > 0 and check[depth-1] == 1:
        check[depth] = 0
        case(check, depth+1)
    else:
        check[depth] = 0
        case(check, depth+1)
        check[depth] = 1
        case(check, depth+1)

def stackCal(string):
    def infixToPostfix(string):
        stack = []
        ret = ''
        for s in string:
            if s in '0123456789':
                ret += s
            elif s == '(':
                stack.append(s)
            elif s == ')':
                while True:
                    x = stack.pop()
                    if x == '(':
                        break
                    ret += x
            else:
                while stack:
                    top = stack[-1]
                    if val[top] < val[s]:
                        break
                    ret += stack.pop()
                stack.append(s)
        while stack:
            ret += stack.pop()
        ret = ret.replace('(', '').replace(')', '')
        #print(ret)
        return ret

    def postfixCal(string):
        stack = []
        for s in string: 
            if s == '+': 
                op2 = stack.pop() 
                op1 = stack.pop() 
                stack.append(op1 + op2)
            elif s == '-': 
                op2 = stack.pop()
                op1 = stack.pop() 
                stack.append(op1 - op2)
            elif s == '*': 
                op2 = stack.pop() 
                op1 = stack.pop() 
                stack.append(op1 * op2) 
            elif s == '/':
                op2 = stack.pop() 
                op1 = stack.pop()
                stack.append(op1 / op2) 
            else: 
                stack.append(int(s))
        #print(stack[0])
        return stack[0]
        
    return postfixCal(infixToPostfix(string))


def solve(check):
    global maxAns
    string = deepcopy(calstr)
    #print(check)
    cnt = 0
    for i in range(opNum):
        if check[i]:
            idx = 2*i+1 + cnt
            string = string[:idx-1] + '(' + string[idx-1:idx+2] + ')' + string[idx+2:]
            cnt += 2
    #print(string)
    ans = stackCal(string)
    #print(ans)
    if ans > maxAns:
        maxAns = ans
'''
print(stackCal('1-(9-1)-9-1-9-1-9-1-9'))

'''
N = int(read())
calstr = read().replace('\n', '')

originNums = [] 
originOps = []
for i in range(N):
    if i%2 == 0:
        originNums.append(int(calstr[i]))
    else:
        originOps.append(calstr[i])

opNum = len(originOps)
case([0 for _ in range(opNum)], 0)
print(maxAns)
