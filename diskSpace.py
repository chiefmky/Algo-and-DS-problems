from collections import deque

def largestMinima(hardDiskSpace, numComputer, segmentLength):
    largest = min(hardDiskSpace[:segmentLength])
    dq = deque()
    for i in range(numComputer):
        if dq and dq[0] < i-segmentLength+1:
            dq.popleft()
        while dq and hardDiskSpace[dq[-1]] > hardDiskSpace[i]:
            dq.pop()
        dq.append(i)
        if i >= segmentLength-1:
            largest = max(largest, hardDiskSpace[dq[0]])
    return largest