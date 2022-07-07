from tkinter import N


def solution(rooms, target):
    answer = []
    room_name = {}
    name_room = {}
    for room in rooms:
        roomNum = room[1:4]
        names = room[5:].split(',')
        names.sort()
        room_name[roomNum] = names
        for name in names:
            if name in name_room :
                name_room[name].add(roomNum)
            else : 
                name_room[name] = {roomNum}
    
            

    print(room_name)
    print(name_room)
    return answer

rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403

result = solution(rooms, target)
