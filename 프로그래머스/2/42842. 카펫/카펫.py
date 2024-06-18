import math

def solution(brown, yellow):
    # 갈색이 한줄 둘러져있고 그 중앙이 노란색인 카펫이기 때문에 근의 공식으로 풀었다.
    w = ((brown + 4) / 2 + math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    h = ((brown + 4) / 2 - math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    return [w,h]