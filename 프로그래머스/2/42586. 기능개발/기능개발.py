def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    # 첫번째가 100이 될때까지 loop 를 돌며 time 을 늘린다.
    # 100이 안되면 loop를 돌며 time 을 늘린다.
    
    # 반복하면서 그전에 완성된 item의 count 값이 있다면 이 item들을 출시한다.
    # 따라서 answer 리스트에 append하고 count 초기화한다.
    # 그후에 loop를 돌며 time 을 늘리면서 결과값을 제출한다.
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)
    return answer