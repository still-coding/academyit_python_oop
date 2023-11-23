from collections import deque

deq = deque([1, 2, 3])

print(deq)

deq.append(42)
deq.appendleft(24)

print(deq)
