# highest profit
def max_supply_profit_map(num_suppliers, inventory, order):
    profit = dict()
    for price in inventory:
        profit[price] = profit.get(price, 0) + 1

    curr_max = max(profit.items(), key=lambda x: x[0])[0]

    ret = 0
    while order > 0:
        maxi = min(order, profit[curr_max])
        ret += curr_max * maxi
        order -= maxi
        profit[curr_max] -= maxi
        profit[curr_max - 1] = profit.get(curr_max - 1, 0) + maxi
        if profit[curr_max] == 0:
            del profit[curr_max]
            curr_max -= 1

    return ret