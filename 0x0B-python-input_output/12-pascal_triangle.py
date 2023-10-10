#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of integers represening the pascal's triangle of n"""
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        triangles.append(temp)
    return (triangles)
