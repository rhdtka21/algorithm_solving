# [파이썬 | 2019 카카오 인턴쉽] 호텔 방 배정

import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    def findAvailRoom(each_room):
        temp = []
        while check.get(each_room) is not None:
            temp.append(each_room)
            each_room = check[each_room]
        #print(temp)
        for t in temp:
            check[t] = each_room + 1
        check[each_room] = each_room + 1
        return each_room

    answer = []
    check = {}
    for each_room in room_number:
        answer.append(findAvailRoom(each_room))
    #print(answer)
    return answer
    
k = int(input())
room_number = list(map(int, input().split()))
solution(k, room_number)