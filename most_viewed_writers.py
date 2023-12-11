def solution(topicIds, answerIds, views):
    topics_map = {}
    views_map = {}
    for qix, tids in enumerate(topicIds):
        for tid in tids:
            topics_map[tid] = topics_map.get(tid,[]) + answerIds[qix]
    for views_item in views:
        views_map[views_item[0]] = [views_item[1],views_item[2]]
    res = []
    for tid in sorted(topics_map.keys()):
        users_map = {}
        for aid in topics_map[tid]:
            user_id = views_map[aid][0]
            views_count = views_map[aid][1]
            users_map[user_id] = users_map.get(user_id,0) + views_count
        mvw = []
        for user_id in sorted(users_map.keys()):
            mvw.append([user_id, users_map[user_id]])
        res.append(sorted(mvw, key=lambda u:u[1], reverse=True))
    return res