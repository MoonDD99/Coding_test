from collections import defaultdict, deque
def solution(genres, plays):
    answer = []
    genreSong = defaultdict(list) #{genre : [plays]}
    genreTotalPlay = defaultdict(int) #{genre : totalPlay}
    firstGenre = "pop"
    secondGenre = "classic"

    for index in range(len(genres)-1,-1,-1):
        genre = genres[index]
        play = plays[index]

        if len(genreSong[genre]) == 0 :
            genreSong[genre] = [index,0]
        elif plays[(genreSong[genre])[0]] <= play:
                (genreSong[genre])[1] = (genreSong[genre])[0]
                (genreSong[genre])[0] = index
        elif plays[(genreSong[genre])[1]] <= play:
            (genreSong[genre])[1] = index

        genreTotalPlay[genre] += play


    answer.append((genreSong[firstGenre])[:2])
    answer.append((genreSong[secondGenre])[:2])

    print(genreSong)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
answer = solution(genres, plays)
print(answer)