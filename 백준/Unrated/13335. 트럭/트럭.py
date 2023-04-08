def is_terminated():
    for i in range(W):
        if bridge[i] != -1:
            return False
    return True

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [-1] * W
time = 1
bridge[0] = 0
next_truck = 1
cur_weight = truck[0]

while not is_terminated():
    if bridge[W-1] != -1:
        cur_weight -= truck[bridge[W-1]]
        bridge[W-1] = -1

    for i in range(W-1, 0, -1):
        bridge[i] = bridge[i-1]
    
    if next_truck < N and cur_weight + truck[next_truck] <= L:
        bridge[0] = next_truck
        cur_weight += truck[next_truck]
        next_truck += 1
    else:
        bridge[0] = -1
    
    time += 1

print(time)