# [파이썬 | BOJ | 17140] 이차원 배열과 연산
import sys
read = sys.stdin.readline

def sync():
    # row에서 column으로
    if len(rows) >= len(columns):
        columns.clear()
        rangeC = len(rows[0])
        rangeR = len(rows)

        for c in range(rangeC):
            temp = []
            for r in range(rangeR):
                temp.append(rows[r][c])
            columns.append(temp)
    # column에서 row로
    else:
        rows.clear()
        rangeR = len(columns[0])
        rangeC = len(columns)

        for i in range(rangeR):
            temp = []
            for j in range(rangeC):
                temp.append(columns[j][i])
            rows.append(temp)

def cal():
    rangeR = len(rows)
    rangeC = len(rows[0])
    #print(rangeR, rangeC)
    # 행의개수 >= 열의 개수
    if len(rows) >= len(rows[0]):
        temps = []
        temp_maxC = -1
        for row in rows:
            row.sort()
            ttemp = []
            i = 0
            while i < rangeC:
                if row[i] == 0:
                    i += row.count(row[i])
                    continue
                ttemp.append([row[i], row.count(row[i])])
                i += row.count(row[i])
            ttemp.sort(key = lambda x: (x[1], x[0]))
            temp = []
            for t in ttemp:
                temp.append(t[0])
                temp.append(t[1])

            if temp_maxC < len(temp):
                temp_maxC = len(temp)
            temps.append(temp)
        
        # 남는 길이를 0으로 맞춘다.
        for temp in temps:
            temp.extend([0 for _ in range(temp_maxC-len(temp))])
        
        #rows를 새로 바꾼다.
        rows.clear()
        for temp in temps:
            rows.append(temp)        

        sync()

    # column에서 row로
    else:
        temps = []
        temp_maxR = -1
        for column in columns:
            column.sort()
            ttemp = []
            i = 0
            while i < rangeR:
                if column[i] == 0:
                    i += column.count(column[i])
                    continue
                ttemp.append([column[i], column.count(column[i])])
                i += column.count(column[i])
            ttemp.sort(key = lambda x: (x[1], x[0]))
            temp = []
            for t in ttemp:
                temp.append(t[0])
                temp.append(t[1])
            #print(temp)

            if temp_maxR < len(temp):
                temp_maxR = len(temp)
            temps.append(temp)
        
        # 남는 길이를 0으로 맞춘다.
        for temp in temps:
            temp.extend([0 for _ in range(temp_maxR-len(temp))])
        
        #rows를 새로 바꾼다.
        columns.clear()
        for temp in temps:
            columns.append(temp)        

        sync()

R, C, K = map(int, read().split())
rows = []
columns = []
t = 0
for _ in range(3):
    rows.append(list(map(int, read().split())))
#초기 column 복사
sync()

while t <= 110: #넉넉하게 잡아줌
    #print(rows)
    try:        #TC에 초기 index를 벗어나는게 존재함.
                #따라서 그냥 indexing error 무시하고 넘어감
        if rows[R-1][C-1] == K:
            break
    except IndexError:
        pass
    cal()
    t += 1

print(t if t <= 100 else -1)