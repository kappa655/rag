import numpy as np
"""
def closest_point(points, target):
    if not points:
        return None
    dist_squared_list = []


    for point in points:
        dist_squared = 0
        for x1, x2 in zip(point, target):
            dist_squared = dist_squared + np.square(x2 - x1)
        dist_squared_list.append(dist_squared)

    min_dist = dist_squared_list[0]
    index = 0
    for i in range(1, len(dist_squared_list)):
        if min_dist > dist_squared_list[i]:
            index = index + 1
            min_dist = dist_squared_list[i]
        
    return min_dist, dist_squared_list, index
"""


def solution(A):
    counts = {}
    for num in A:
        counts[num] = counts.get(num, 0) + 1
        
    for count in counts.values():
        if count % 2 != 0:
            return False
            
    return True



a = [1,3,1,4,5,4,5,3]
res = solution(a)
print(res)