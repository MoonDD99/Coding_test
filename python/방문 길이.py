def solution(dirs):
    #score : 100.0 / 100.0
    way = set()
    current_x = 0
    current_y = 0
    next_x = 0
    next_y = 0
    move = {'U' : (0,1), 'D' : (0,-1), 'R' : (1,0), 'L':(-1,0)}
    
    for dr in dirs:
        next_x = current_x + move[dr][0]
        next_y = current_y + move[dr][1]
        
        if abs(next_x) <= 5 and abs(next_y) <= 5:
            way.add((current_x,current_y,next_x,next_y))
            way.add((next_x,next_y,current_x,current_y))
            current_x = next_x
            current_y = next_y

    return len(way) // 2