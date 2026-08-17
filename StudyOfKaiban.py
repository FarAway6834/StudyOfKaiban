from collections import deque

def asserter(p, /, msg = None, *, work = None):
    if msg == None: assert p
    else: assert p, msg
    if work != None: return work()

mver = lambda dx, dy : lambda x, y, i : (x + dx[i], y + dy[i])
in_range = lambda x, n : (0 <= x < n)
direction = lambda n, p = 0 : ([[-1, 1, 0, 0, -1, -1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 0, -1]][p][:n + 1], [[0, 0, -1, 1, -1, 1, -1, 1], [0, 1, 1, 1, 0, -1, -1, -1], [1, 0, -1, 0]][p][:n + 1])
check = lambda *argv : (lambda Q, R : asserter(R == 0, "check get even number of arguments", work = (lambda : in_range(argv[0], argv[Q]) and checker(*argv[1:Q], *argv[Q + 1:]))))(*divmod(len(argv), 2))
under = lambda x, *argv : is_range(x, argv[-1]) and under(*argv) if len(argv) else True

basic_tool = lambda dx, dy, N = None : (dx, dy, mver(dx, dy), range(len(dx) if N == None else N))

direc_tool = lambda N, p = 0 : (lambda dx, dy : basic_tool(dx, dy, N = N))(*direction(N, p = p))

from subpr.lib import martialaw as _clsr
from subpr.lib import comp as _comp

hanten = _comp(list, _clsr(map)(list), zip)
turn90 = lambda x : hanten(*x[::-1])
