# -*- coding: utf-8 -*-
def triangles():
     N = [1]
     while True: #true表明该循环为无限循环
          yield N
          N.append(0)
          N = [N[i-1] + N[i] for i in range(len(N))]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles()：
     print(t)
     n = n + 1
     if n == 10:
          break
