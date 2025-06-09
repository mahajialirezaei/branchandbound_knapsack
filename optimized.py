def upper_bound(profits, weights, start_index, capacity):
    items = []
    for i in range(start_index, len(profits)):
        if weights[i] > 0:
            x = profits[i] / weights[i]
            items.append((x, weights[i], profits[i]))
    items.sort(key=lambda x: x[0], reverse=True)
    b = 0
    r = capacity
    for x, weight, profit in items:
        if r <= 0:
            break
        if weight <= r:
            b += profit
            r -= weight
        else:
            b += x * r
            r = 0
    return b


def cal_product_ls(x: list, p: list):
    profit = sum(s * s1 for (s, s1) in zip(x, p))
    return profit


def recursive_func(x: list, p: list, w: list, l, b, cur_w):
    global x_opt, p_opt
    print(x_opt)
    print(p_opt)
    if l == len(x):
        p_cur = cal_product_ls(x, p)
        if p_cur > p_opt:
            p_opt = p_cur
            x_opt = x.copy()
    else:
        c = [0]
        if cur_w + w[l] <= b:
            c = [0, 1]
        for xl in c:
            x[l] = xl
            recursive_func(x, p, w, l + 1, b, cur_w + w[l] * xl)



x = [0, 0, 0]
p = [1, 2, 3]
w = [1, 2, 999]
b = 1000
x_opt = [0, 0, 0]
p_opt = 0
recursive_func(x, p, w, 0, b, 0)
print(x_opt)
print(p_opt)
