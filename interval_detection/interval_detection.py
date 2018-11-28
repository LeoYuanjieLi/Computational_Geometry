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


    temp = []
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            if (sorted_intervals[i][0], min(sorted_intervals[i-1][1], sorted_intervals[i][1])) not in temp:
                temp.append((sorted_intervals[i][0], min(sorted_intervals[i-1][1], sorted_intervals[i][1])))

    res = []
    for begin, end in temp:
        if res and res[-1][1] >= begin:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([begin, end])

    return res

cal_intersects(INTERVALS)


