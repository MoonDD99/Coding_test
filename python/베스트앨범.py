from collections import defaultdict, deque
def solution(genres, plays):
    answer = []
    genreSong = defaultdict(list) #{genre : [(index,play)]}
    genreTotalPlay = defaultdict(int) #{genre : totalPlay} {totalPlay : genre}

    for index in range(len(genres)):
        genre = genres[index]
        play = plays[index]
        
        genreSong[genre].append((index, play))
        genreTotalPlay[genre] += play

    
    sortTotalPlay = sorted(genreTotalPlay.items(), key=lambda x:x[1], reverse=True)
    
    for key, value in sortTotalPlay:
        sortSong = sorted(genreSong[key],key=lambda x:x[1], reverse=True)
        for index, play in sortSong[:2]:
            answer.append(index)
    

    print(genreTotalPlay)
    print(genreSong)
    return answer


genres = ["a", "b", "b", "c", "c"] #["classic", "pop", "classic", "pop", "classic", "classic"]#["classic", "pop", "classic", "classic", "pop"] #["classic", "pop", "classic", "classic"]
plays = [5, 5, 40, 5, 5]#[1950, 600, 500, 2500, 500, 150] #[500, 600, 150, 800, 2500]	#[800, 600, 150, 800]
answer = solution(genres, plays)
print(answer)