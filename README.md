# StudyOfKaiban
프로그래밍 공부용

```
Step 1.

mv = mver(dx, dy)일 시 

nx, ny = mv(x, y, i)
는
nx, ny = x + dx[i], y + dy[i]
임

Step 2.

inRange(x, n)은 0<=x<n임.

Step 3.

dx, dy = direction(n, p=0)에서
dx == [-1, 1, 0, 0, -1, -1, 1, 1][:n+1]
dy == [0, 0, -1, 1, -1, 1, -1, 1][:n+1] 

dx, dy = direction(n, p=1)에서
dx == [-1, -1, 0, 1, 1, 1, 0, -1][:n+1]
dy == [0, 1, 1, 1, 0, -1, -1, -1][:n+1] 

dx, dy = direction(n, p=2)에서 
dx == [0, 1, 0, -1][:n+1]
dy == [1, 0, -1, 0][:n+1]

Step 4.

dx, dy, mv, check, RN = basic_tool(N, p = p)
은
dx, dy = direction(N, p=p)
mv = mver(dx, dy)
RN = range(N)
이고
check(x, y, n, m) == inRange(x, n) and inRange(y, m)
이다.
```