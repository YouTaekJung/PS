flag = False
res = []


def solution(tickets):
    d = {}
    for t in tickets:
        s, e = t
        if s in d:
            d[s].append(e)
        else:
            d[s] = [e]
    for s in d:
        d[s] = sorted(d[s])

    print(d)
    def dfs(start, cur, check):
        global flag, res
        if flag:
            return
        if len(cur) == len(tickets) + 1:
            flag = True
            res.append(cur)
            return res
        else:
            res.append(cur)

            if start in d:
                for end in d[start]:
                    if [start, end] in tickets:
                        li = [i for i, v in enumerate(tickets) if v == [start, end]]
                        idx = tickets.index([start, end])
                        if check[idx] == 1:
                            for l in li:
                                if check[l] == 0:
                                    idx = l
                                    break
                        if check[idx] == 0:
                            temp = check[:]
                            temp[idx] = 1
                            dfs(end, cur + [end], temp)

        return

    dfs('ICN', ['ICN'], [0] * len(tickets))
    return res[-1]

solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']])