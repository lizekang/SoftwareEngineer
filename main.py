#! /usr/bin/python3
# -*- coding:utf-8 -*-


import math
import matplotlib.pyplot as plt
import turtle


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Edge(object):
    def __init__(self, point1, point2):
        self.A = point2.y - point1.y
        self.B = point1.x - point2.x
        self.C = point2.x*point1.y - point1.x*point2.y


class Circle1(object):
    def __init__(self, point, r):
        self.point = point
        self.r = r


def point_with_2edges(edge1, edge2):
    A1 = edge1.A
    A2 = edge2.A
    B1 = edge1.B
    B2 = edge2.B
    C1 = edge1.C
    C2 = edge2.C
    # print(A1, B1, C1)
    # print(A2, B2, C2)
    x = ((C1 * B2 - B1 * C2)/(A2 * B1 - A1 * B2) if C1 * B2 - B1 * C2 != 0 else 0)
    y = ((A1 * C2 - A2 * C1) / (A2 * B1 - A1 * B2) if A1 * C2 - A2 * C1 != 0 else 0)
    return Point(x, y)


def suround_by_2edges_and_1circle(edge1, edge2, circle):
    point1 = point_with_2edges(edge1, edge2)
    point2 = circle.point
    r = (point2point(point1, circle.point) - circle.r) / (1 + math.sqrt(2))
    point = Point(point1.x + math.sqrt(2)*(point2.x - point1.x)/(circle.r + (1+math.sqrt(2))*r)*r,
                  point1.y + math.sqrt(2)*(point2.y - point1.y)/(circle.r + (1+math.sqrt(2))*r)*r)
    print point.x, point.y
    return Circle1(point, r)


def point2point(point1, point2):
    return math.sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))


def point2edge(point, edge):
    return abs(edge.A * point.x + edge.B * point.y + edge.C) / math.sqrt(pow(edge.A, 2) + pow(edge.B, 2))


def surround_by_3circles(circle1, circle2, circle3):
    x1 = circle1.point.x
    y1 = circle1.point.y
    x2 = circle2.point.x
    y2 = circle2.point.y
    x3 = circle3.point.x
    y3 = circle3.point.y
    r1 = circle1.r
    r2 = circle2.r
    r3 = circle3.r
    A1 = (pow(x1, 2) - pow(x2, 2) + pow(y1, 2) - pow(y2, 2) + pow(r2, 2) - pow(r1, 2)) * (r1 - r3)
    A2 = (pow(x1, 2) - pow(x3, 2) + pow(y1, 2) - pow(y3, 2) + pow(r3, 2) - pow(r1, 2)) * (r1 - r2)
    B1 = (pow(x2, 2) - pow(x3, 2) + pow(y2, 2) - pow(y3, 2) + pow(r3, 2) - pow(r2, 2)) * (r1 - r3)
    B2 = (pow(x1, 2) - pow(x3, 2) + pow(y1, 2) - pow(y3, 2) + pow(r3, 2) - pow(r1, 2)) * (r2 - r3)
    Dx = (x3 - x1) * (r1 - r2) - (x2 - x1) * (r1 - r3)
    Dy = (y3 - y1) * (r1 - r2) + (y2 - y1) * (r1 - r3)
    Ex = (x3 - x1) * (r2 - r3) - (x3 - x2) * (r1 - r3)
    Ey = (y3 - y1) * (r2 - r3) + (y3 - y2) * (r1 - r3)
    print x1,y1,x2,y2,x3,y3
    print r1,r2,r3
    print Dy,Ex,Ey,Dx
    # print r
    y = ((A1 - A2) * Ex - (B1 - B2) * Dx) / (Dy * Ex - Ey * Dx) / 2
    x = ((A1 - A2) - 2 * y * Dy) / (2 * Dx)
    r = math.sqrt(pow(x - x1, 2) + pow(y - y1, 2)) - r1

    return Circle1(Point(x, y), r)


def surround_by_2circles_and_1edge(circle1, circle2, edge2):
    A = edge2.A
    B = edge2.B
    C = edge2.C
    r1 = circle1.r
    r2 = circle2.r
    x1 = circle1.point.x
    y1 = circle1.point.y
    x2 = circle2.point.x
    y2 = circle2.point.y
    print A,B,C
    r = pow((math.sqrt(r1 * r2) / (math.sqrt(r1) + math.sqrt(r2))), 2)
    theta1 = (pow(r1, 2) - pow(r2, 2) + 2 * r * (r1 - r2) - pow(x1, 2) + pow(x2, 2) - pow(y1, 2) + pow(y2, 2)) / 2
    theta2 = r * math.sqrt(pow(A, 2) + pow(B, 2)) - C
    if C == 0 and (B == -1 or A == -1):
        theta2 = -theta2
    y = (theta2 * (x2 - x1) - theta1 * A) / (B * (x2 - x1) - A * (y2 - y1))
    x = (theta1 - y*(y2-y1))/(x2-x1)
    print x,y
    return Circle1(Point(x, y), r)


class suroundings(object):
    def __init__(self, type, edges, circles):
        self.type = type
        self.edges = edges
        self.circles = circles
        self.circle = self.new_circle()

    def new_circle(self):
        if self.type == 1:
            return suround_by_2edges_and_1circle(self.edges[0], self.edges[1], self.circles[0])
        elif self.type == 2:
            return surround_by_2circles_and_1edge(self.circles[0], self.circles[1], self.edges[0])
        else:
            return surround_by_3circles(self.circles[0], self.circles[1], self.circles[2])

    def new_surroundings(self):
        if self.type == 1:
            return [suroundings(1, [self.edges[0], self.edges[1]], [self.circle]),
                    suroundings(2, [self.edges[0]], [self.circles[0], self.circle]),
                    suroundings(2, [self.edges[1]], [self.circles[0], self.circle])]
        elif self.type == 2:
            return [suroundings(2, [self.edges[0]], [self.circles[0], self.circle]),
                    suroundings(2, [self.edges[0]], [self.circles[1], self.circle]),
                    suroundings(3, [], [self.circles[0], self.circles[1], self.circle])]
        else:
            return [suroundings(3, [], [self.circle, self.circles[1], self.circles[2]]),
                    suroundings(3, [], [self.circles[0], self.circle, self.circles[2]]),
                    suroundings(3, [], [self.circles[0], self.circles[1], self.circle])]


def main(N):
    queue = []
    result = list()
    circle0 = Circle1(Point(0.5, 0.5), 0.5)
    edge1 = Edge(Point(0, 0), Point(1, 0))
    edge2 = Edge(Point(0, 0), Point(0, 1))
    edge3 = Edge(Point(0, 1), Point(1, 1))
    edge4 = Edge(Point(1, 1), Point(1, 0))
    result.append(circle0)
    queue.append(suroundings(1, [edge1, edge2], [circle0]))
    queue.append(suroundings(1, [edge2, edge3], [circle0]))
    queue.append(suroundings(1, [edge3, edge4], [circle0]))
    queue.append(suroundings(1, [edge4, edge1], [circle0]))
    while len(queue) > 0 and N >= 0:
        surrounding = queue.pop(0)
        print surrounding.type
        newCircle = surrounding.circle
        for surround in surrounding.new_surroundings():
            for i in range(len(queue)-1, -1, -1):
                if surround.circle.r < queue[i].circle.r:
                    if i == 0:
                        queue.append(surround)
                else:
                    queue.insert(i, surround)
                    break
        result.append(newCircle)
        N -= 1
        # print(newCircle.point.x, newCircle.point.y)
    return result


def plot(result):
    turtle.penup()
    turtle.goto(0, 300)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.penup()
    for item in result:
        turtle.penup()
        turtle.goto(item.point.x*300, (item.point.y-item.r)*300)
        turtle.pendown()
        turtle.circle(item.r*300)
    turtle.exitonclick()

plot(main(4))
