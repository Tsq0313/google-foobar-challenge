from Queue import Queue

dirs = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
row = 8
col = 8

def solution(src, dest):
    if src == dest:
        return 0

    q = Queue()

    cnt = 0
    visited = set()
    q.put(src)
    visited.add(src)
    
    # Breath-First Search
    while not q.empty():
        size = q.qsize()
        while size > 0:
            curr_num = q.get()
            x = int(curr_num / 8)
            y = int(curr_num % 8)
            for d in dirs:
                cx = x + d[0]
                cy = y + d[1]
                if cx < 0 or cx >= row or cy < 0 or cy >= col:
                    continue
                next_num = cx * 8 + cy
                if next_num == dest:
                    return cnt + 1
                if next_num not in visited:
                    q.put(next_num)
                    visited.add(next_num)
            size -= 1
        cnt += 1

    return -1