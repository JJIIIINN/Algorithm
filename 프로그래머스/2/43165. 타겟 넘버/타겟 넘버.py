a = 0

# 위 그림처럼 i번째 숫자에 대해 + or -를 붙여 계산하는 모든 경우의 수를 따진다.
# i가 마지막원소일 때 최종 합이 target 과 같다면, 전역변수 a의 값을 1 증가시킨다.
def dfs(i, result, numbers, target) :
    global a
    if i == len(numbers) :
        if result == target : 
            a+=1
            return
    else :
        dfs(i+1, result+numbers[i], numbers, target)
        dfs(i+1, result-numbers[i], numbers, target)

def solution(numbers, target):
    result = 0
    dfs(0, result, numbers, target)
    
    return a