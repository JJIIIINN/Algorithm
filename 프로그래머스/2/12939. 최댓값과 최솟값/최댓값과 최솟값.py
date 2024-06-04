def solution(s):
    b = list(map(int, s.split(' ')))
    answer = f'{min(b)} {max(b)}'
    return answer