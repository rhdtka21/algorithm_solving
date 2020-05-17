# [파이썬 | BOJ | 6549] 히스토그램에서 가장 큰 직사각형
 
import sys
read = sys.stdin.readline

def solve(left, right):
    mid = (left + right) // 2
    if left == right:
        return height[left]
    maxwidth = right-left+1

    #접점을 포함하는 사각형의 최대 넓이 계산

    #mid와 mid+1 두개만 포함하는 경우
    tempHeight = min(height[mid:mid+2])
    tempArea = 2 * tempHeight
    
    #그외의 길이 경우
    ll, rr = mid, mid+1

    #ll과 rr이 모두 범위밖에 나가면 종료
    while left < ll or rr < right:
        #ll과 rr이 가리키는 높이를 비교해서, 큰쪽으로 커진다.
        print(ll, rr)
        if rr < right and (ll == left or height[ll-1] < height[rr+1]):
            rr += 1
            tempHeight = min(tempHeight, height[rr])
        else:
            ll -= 1
            tempHeight = min(tempHeight, height[ll])
        tempArea = max(tempArea, tempHeight * (rr-ll+1))

    #왼쪽 분할, 오른쪽 분할, 그리고 접점을 포함하는 area중에서 제일 큰 값을 return
    return max(solve(left, mid), solve(mid+1, right), tempArea)

while True:
    height = list(map(int, read().split()))
    ans = -1
    if height[0] == 0:
        break
    N = height[0]
    print(solve(1, N))