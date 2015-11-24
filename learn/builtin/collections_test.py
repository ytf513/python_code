#!/usr/bin/env python
#-*- encoding=utf-8  -*-

'collections'

__all__=("Alex Yean","2015-11-09")

from collections import namedtuple
Point=namedtuple("Point",["x","y"])
p=Point(1,2)
print p.x,p.y

from collections import deque
q=deque(["a","b","c"])
q.append("d")
q.appendleft("y")
print q


