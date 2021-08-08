inf = 10000
movieDB_sz, horrorDB_sz, pairDB_sz = map(int, input().split())
horror_list = list(map(int, input().split()))
horror_list.sort()
pairs_list = [[] for m in range(movieDB_sz)]
for p in range(pairDB_sz):
    movie_A, movie_B = map(int, input().split())
    pairs_list[movie_A] += [movie_B]
    pairs_list[movie_B] += [movie_A]

movies_scores = [[inf, m] for m in range(movieDB_sz)]
for h in horror_list:
    movies_scores[h][0] = 0

for h in horror_list:
    p = pairs_list[h]
    for pp in p:
        movies_scores[pp][0] = min(1, movies_scores[pp][0])
    for pp in p:
        ppp = pairs_list[pp]
        for pppp in ppp:
            movies_scores[pppp][0] = min(2, movies_scores[pppp][0])

print(movies_scores)

# research about graphs maybe?


