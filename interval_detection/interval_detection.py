INTERVALS = [[0, 2],
             [1, 4],
             [2, 3],
             [5, 7],
             [5, 11],
             [6, 15],
             [6, 8],
             [2, 12],
             [13, 19]]

import numpy as np
def cal_intersects(intervals):
    sorted_intervals = np.array(sorted(intervals))
    print(sorted_intervals)
    # lefts = [("l", interval) for interval in sorted_intervals[..., 0]]
    # rights = [("r", interval) for interval in sorted_intervals[..., 1]]
    # print(lefts)
    # print(rights)
    res = []
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            if (sorted_intervals[i][0], min(sorted_intervals[i-1][1], sorted_intervals[i][1])) not in res:
                res.append((sorted_intervals[i][0], min(sorted_intervals[i-1][1], sorted_intervals[i][1])))
    print(res)
    return res





cal_intersects(INTERVALS)