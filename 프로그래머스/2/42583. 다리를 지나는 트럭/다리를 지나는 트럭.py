def solution(length, w, kk):
    t = 0
    b = [0] * length
    c = 0
    
    while len(kk) > 0:
        t += 1
        c = c - b.pop(0)

        if c + kk[0] <= w:
            c += kk[0]
            b.append(kk.pop(0))
        else:
            b.append(0)

    t += length
    return t