def solution(name, yearning, photo):
    a = 0
    answer = []
    for item in photo:
        for v in item:
            if v in name:
                a += yearning[name.index(v)]
        answer.append(a)
        a = 0
    return answer