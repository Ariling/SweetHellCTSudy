from collections import defaultdict
def solution(genres, plays):
    answer = []
    music_dict = defaultdict(list)
    total_play = defaultdict(int)
    for i in range(len(genres)):
        music_dict[genres[i]].append((i, plays[i]))
        total_play[genres[i]] += plays[i]
    # 복잡한 리스트 dict 키 정렬하는 방법
    for key, items in music_dict.items():
        music_dict[key] = sorted(items, key=lambda item: (-item[1], item[0]))
    total_play = sorted(total_play.items(), key=lambda item: -item[1])
    for key, items in total_play:
        if key in music_dict:
            music_list = music_dict[key][:2]
            for song in music_list:
                answer.append(song[0])
    return answer