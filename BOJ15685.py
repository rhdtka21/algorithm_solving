# [파이썬 | BOJ | 15685] 드래곤 커브
import sys
read = sys.stdin.readline

def lineOperation(line):
    x1, y1, x2, y2 = line

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    if y1 > y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    return [x1, y1, x2, y2]

        
def rotateDragon(eachDragon):
    originX, originY = 0, 0
    for i in range(len(eachDragon)):
        x1, y1, x2, y2 = eachDragon[i]
        x1, y1 = matrixOperation(x1, y1, originX, originY)
        x2, y2 = matrixOperation(x2, y2, originX, originY)
        eachDragon[i] = [x1, y1, x2, y2]
    return eachDragon



def matrixOperation(inputX, inputY, originX, originY):
    #회전행렬, 
    # [ 0 1]    [a b]
    # [-1 0]    [c d]

    x = inputX - originX
    y = inputY - originY
 
    a, b, c, d = 0, -1, 1, 0

    outputX = a * x + b * y + originX
    outputY = c * x + d * y + originY

    return outputX, outputY

def originDistance(x1, y1, x2, y2):
    #x2, y2가 더 크면 true 아니면 false
    return True if x1 ** 2 + y1 ** 2 < x2 ** 2 + y2 ** 2 else False

#dragonShapes : 가장큰 리스트, 각각의 드래곤을 포함한다.
#dragonXYs / eachDragon : 각각의 드래곤, 드래곤의 선분을 포함한다.


N = int(read())
dragonInfo = []
dragonShapes = []   
allPoints = set()

for _ in range(N):
    x, y, d, g = map(int, read().split())
    
    if d == 1:
        d = 3
    elif d == 3:
        d = 1
    
    dragonInfo.append([x,y,d,g])

for i in range(N):
    gen = dragonInfo[i][3]
    dragonXYs = [[0, 0, 1, 0]]
    for i in range(gen):
        if i == 0:
            standardX, standardY = 1, 0
        else:
            x1, y1, x2, y2 = dragonXYs[-1]
            x1, y1, x2, y2 = lineOperation([x1, y1, x2, y2])
            standardX, standardY = x1, y1
        
        temp = []
        for dragonXY in reversed(dragonXYs):
            x1, y1, x2, y2 = dragonXY
            nx1, ny1 = matrixOperation(x1, y1, standardX, standardY)
            nx2, ny2 = matrixOperation(x2, y2, standardX, standardY)
            temp.append([nx1, ny1, nx2, ny2])
        dragonXYs += temp
    dragonShapes.append(dragonXYs)

#이제 방향 및 위치에 맞게 이동해준다.
for i in range(N):
    direction =  dragonInfo[i][2]
    startX, startY = dragonInfo[i][0:2]
    for _ in range(direction):
        dragonShapes[i] = rotateDragon(dragonShapes[i])
    for j in range(len(dragonShapes[i])):
        for k in range(4):
            dragonShapes[i][j][k] += (startX if k % 2 == 0 else startY)


for eachDragon in dragonShapes:
    for line in eachDragon:
        x1, y1, x2, y2 = line
        allPoints.add((x1, y1))
        allPoints.add((x2, y2))

ans = 0
for x in range(100):
    for y in range(100):
        p1 = (x, y)
        p2 = (x, y+1)
        p3 = (x+1, y)
        p4 = (x+1, y+1)
        if p1 in allPoints and p2 in allPoints and p3 in allPoints and p4 in allPoints:
            ans += 1

print(ans)