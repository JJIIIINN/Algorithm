def solution(n, m, section):
    answer = 0
    while section:
        e = section[0] + m
        while section and section[0] < e:
            section.pop(0)
        answer += 1
    return answer