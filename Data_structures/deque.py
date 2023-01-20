from collections import deque


a = [35, 2, 4, 6, 12, 33, 1.2, 'Hello']
LL = deque(a)

LL.appendleft(3)
print(LL)

l_value = LL.popleft()
print(l_value)
