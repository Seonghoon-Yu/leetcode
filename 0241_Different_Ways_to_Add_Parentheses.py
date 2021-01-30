# 분할 정복 풀이
def diffWaysToCompute(self, input):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l)+op+str(r)))
        return results

    if input.isdigit():
        return [int(input)]
    
    results = []
    for index, value in enumerate(input):
        if value in '-+*':
            L = diffWaysToCompute(input[:index])
            R = diffWaysToCompute(input[index+1:])
            results.extend(compute(L,R,value))
    return results
