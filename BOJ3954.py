#[파이썬 | BOJ | 3954] BrainFuck

import sys
read = sys.stdin.readline
INFNUM = 50000000
class bit8:
    num = 0
    def __inint__(self, num):
        self.num = num % 256
    def plus(self):
        self.num += 1
        if self.num == 256:
            self.num = 0
    def minus(self):
        self.num -= 1
        if self.num == -1:
            self.num = 255
    def ret(self):
        return self.num
    def go(self, val):
        self.num = ord(val)

class pointer:
    mem = 0
    def __inint__(self, mem):
        self.mem = mem % sm
    def plus(self):
        self.mem += 1
        if self.mem == sm:
            self.mem = 0
    def minus(self):
        self.mem -= 1
        if self.mem == -1:
            self.mem = sm-1
    def ret(self):
        return self.mem
    def go(self, val):
        self.mem = val % sm

# 현재 포인터가 가리키는 메모리에 쓰여진 값. arr[ptr.ret()].ret()

T = int(read())
for t in range(T):
    sm, sc, si = map(int, read().split())
    operation = read().replace('\n', '')
    inputstr = read().replace('\n', '')
    inputidx = 0
    check = [0 for _ in range(sc)]
    arr = [bit8() for _ in range(sm)]
    ptr = pointer()
    
    twins = [-1 for _ in range(sc)]
    
    twin = []       #스택역할
    for i in range(sc):
        if operation[i] == '[':
            twin.append(i)
        elif operation[i] == ']':
            twin.append(i)
            a = twin.pop()
            b = twin.pop()
            twins[a] = b
            twins[b] = a
    
    index = 0
    cnt = -1
    max_index = 0
    while index < sc:
        cnt += 1
        op = operation[index]
        if op == '-':
            arr[ptr.ret()].minus()
        elif op == '+':
            arr[ptr.ret()].plus()
        elif op == '<':
            ptr.minus()
        elif op == '>':
            ptr.plus()
        elif op == '[':
            if arr[ptr.ret()].ret() == 0:
                index = twins[index]
                continue
        elif op == ']':
            if arr[ptr.ret()].ret() != 0:
                check[index] = 0
                index = twins[index]
                continue
            else:
                check[index] = 1
                index += 1
                continue
        elif op == '.':
            pass
        elif op == ',':
            if inputidx < si:
                arr[ptr.ret()].go(inputstr[inputidx])
                inputidx += 1
            else:
                arr[ptr.ret()].go(chr(255))
        index += 1
        
        if cnt >= INFNUM:
            left, right = -1, -1
            minright = sys.maxsize
            for i in range(sc):
                if check[i] == 0 and operation[i] == ']':
                    if minright > i:
                        minright = i
            right = minright
            left = twins[right]

            print("Loops " + str(left) + " " +  str(right))
            break
    else:
        print("Terminates")