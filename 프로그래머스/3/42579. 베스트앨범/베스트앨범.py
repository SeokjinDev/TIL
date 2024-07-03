from collections import defaultdict
def solution(genres, plays):
    playCounter, genreCounter, music = defaultdict(int), defaultdict(int), []
    answer = []
    for idx, play, genre in zip(range(len(genres)), plays, genres):
        playCounter[genre] += play
        music.append([idx, play, genre])
    
    # 정렬을 여러 번 할 경우 후순위 조건부터 정렬하기
    music = sorted(music, reverse = True) # 추후 pop으로 추출하므로 반대로 정렬 / 0번을 기준으로 정렬
    music = sorted(music, key=lambda x: x[1]) # 플레이 순으로 오름차순
    music = sorted(music, key=lambda x: playCounter[x[2]]) # 장르별 플레이 순으로 오름차순
    
    while music:
        data = music.pop()
        if genreCounter[data[2]] < 2:
            genreCounter[data[2]] += 1
        else:
            continue
        answer.append(data[0])

    return answer