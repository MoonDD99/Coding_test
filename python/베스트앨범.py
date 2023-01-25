from collections import defaultdict, deque
def solution(genres, plays):
    answer = []
    genreSong = {} #{genre : [(index,play)]}
    genreTotalPlay = {} #{genre : totalPlay} {totalPlay : genre}

    for index in range(len(genres)):
        genre = genres[index]
        play = plays[index]
        
        if genre not in genreSong:
            genreSong[genre] = [(index, play)]
        else:    
            genreSong[genre].append((index, play))
            
        if genre not in genreTotalPlay:
            genreTotalPlay[genre] = play    
        else:
            genreTotalPlay[genre] += play

    
    sortTotalPlay = sorted(genreTotalPlay.items(), key=lambda x:x[1], reverse=True)
    
    for key, value in sortTotalPlay[:2]:
        sortSong = sorted(genreSong[key],key=lambda x:x[1], reverse=True)
        for index, play in sortSong[:2]:
            answer.append(index)
    

    print(genreTotalPlay)
    print(genreSong)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
answer = solution(genres, plays)
print(answer)