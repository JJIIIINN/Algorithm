def solution(s):
    stack = []
    
    if s[-1] == "(":
        return False
    
    for i in s:
        if i == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0
    