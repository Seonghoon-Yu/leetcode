def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, t in T:
        while stack and T[stack[-1]] < t:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer
