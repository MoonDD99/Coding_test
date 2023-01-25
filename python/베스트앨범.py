from collections import defaultdict, deque
def solution(genres, plays):
    answer = []
    genreSong = defaultdict(list) #{genre : [plays]}
    genreTotalPlay = defaultdict(int) #{genre : totalPlay} {totalPlay : genre}

    for index in range(len(genres)):
        genre = genres[index]
        play = plays[index]

        genreSong[genre].append((index, play))
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