def solution(dishes):
    ings = {}
    for dish in dishes:
        dish_name = dish[0]
        for i in range(1,len(dish)):
            ings[dish[i]] = ings.get(dish[i],[]) + [dish_name]
    res = []
    for ing in sorted(ings.keys()):
        if len(ings[ing]) > 1:
            res.append([ing]+sorted(ings[ing]))
    return res