"""
https://binarysearch.com/problems/Task-Run
"""

def solve(tasks, k):
    last_t = ''

    l = len(tasks)
    i = 0
    total_cost = 0
    m = {}
    while i < l:
        #print('choosing i', i , l)
        cur_task = tasks[i]
        if cur_task in m:
            cost_until = m[cur_task]
            if cost_until < k:
                extra_cost = (k - cost_until) + 1 # 1 for executing cur_task
            else:
                extra_cost = 1
        else:
            extra_cost = 1 # for executing the current task

        total_cost += extra_cost

        # update all tasks until now
        #print(m)
        for key, val in m.items():
            if key != cur_task: # current one will reset to zero anyhow
                m[key] = val + extra_cost
        m[cur_task] = 0
        i += 1
    return total_cost

tasks = [0, 0, 1, 1]
k = 1

res = solve(tasks, k)

print(res)

tasks = [0, 1, 0, 1]
k = 2

res = solve(tasks, k)

print(res)

tasks = [0, 1, 2, 3]
k = 2

res = solve(tasks, k)

print(res)

tasks = [0, 0, 0, 0]
k = 2

res = solve(tasks, k)

print(res)