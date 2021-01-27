# 1. 모두 방문
def canCompleteCircuit(gas,cost):
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)

            can_travel = True

            fuel += gas[index]

            if fuel < cost[index]:
                can_travel = False
                break

            fuel -= cost[index]
        if can_travel:
            return start
    return -1

# 2. 한번 방문
def canCompleteCircuit(gas,cost):
    # 모든 주유소 방문 가능 여부 판별
    if sum(gas) < sum(cost):
        return False

    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start
