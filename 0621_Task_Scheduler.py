def leastInterval(self, tasks, n):
    counts = collections.Counter(tasks)
    result = 0

    while counts:
        sub_count = 0
        
        # 개수 순 추출
        for task, _ in counts.most_common(n+1):
            counts.subtract(task)
            
            # 0 이하인 아이템을 목록에서 완전히 제거
            counts += collections.Counter()
            
            sub_count += 1
            result += 1
            
        if not counts:
            break

        result += n - sub_count + 1
    return result
