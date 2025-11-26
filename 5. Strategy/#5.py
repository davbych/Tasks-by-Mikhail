def greedy_knapsack(items, time_limit, weight_limit):
    sorted_items = sorted(
        items,
        key=lambda x: x[0] / (x[1] + x[2]),
        reverse=True
    )
    
    total_value = 0
    total_time = 0
    total_weight = 0
    selected = []

    for value, time, weight in sorted_items:
        if total_time + time <= time_limit and total_weight + weight <= weight_limit:
            selected.append((value, time, weight))
            total_value += value
            total_time += time
            total_weight += weight

    return total_value, selected



items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

for i, (items, t_lim, w_lim) in enumerate([
    (items_1, time_limit_1, weight_limit_1),
    (items_2, time_limit_2, weight_limit_2),
    (items_3, time_limit_3, weight_limit_3),
    (items_4, time_limit_4, weight_limit_4)
], 1):
    value, selected = greedy_knapsack(items, t_lim, w_lim)
    print(f"Тест {i}:")
    print(f"  Выбрано: {selected}")
    print(f"  Суммарная стоимость: {value}")
    print()
