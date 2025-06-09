def cal_product_ls(x: list, p: list):
    profit = sum(s * s1 for (s, s1) in zip(x, p))
    return profit

