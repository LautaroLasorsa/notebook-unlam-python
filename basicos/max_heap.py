from heapq import heappush, heappop
def push_inv(h, x):
    heappush(h, -x)

def pop_inv(h):
    return -heappop(h)

def get_inv(h):
    return -h[0]