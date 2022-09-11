#!/usr/bin/env python3
from turtle import *

SIZE = 10
DEPTH = 4

def fractal(l, t=1, a=1):
	if not a:
		right(90*t)
	if(l != 0):
		fractal(l-1, -t, 0)
		forward(SIZE)
		fractal(l-1, t, 0)
		forward(SIZE)
		fractal(l-1, t, 1)
		forward(SIZE)
		fractal(l-1, -t, 1)
	if a:
		right(90*t)

speed('fastest')
penup()
goto(-100,-100)
pendown()

begin_fill()
fractal(DEPTH)
end_fill()

input()
