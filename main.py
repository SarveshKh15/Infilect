from fastapi import FastAPI
from typing import List

app = FastAPI()

def largest_rectangle(matrix):
    Row = len(matrix)
    Col = len(matrix[0])
    max_area = 1
    number = matrix[0][0]

    for r1 in range(Row):
        for r2 in range(r1, Row):
            for c1 in range(Col):
                for c2 in range(c1, Col):
                    flag = True

                    for i in range(r1 + 1, r2 + 1):
                        if matrix[i][c2] != matrix[i - 1][c2]:
                            flag = False
                            break

                    for j in range(c1 + 1, c2 + 1):
                        if matrix[r2][j] != matrix[r2][j - 1]:
                            flag = False
                            break

                    if flag:
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if max_area < area:
                            max_area = area
                            number = matrix[r1][c1]

    return max_area, number
    

@app.post("/calculate_area")
async def calculate_area(matrix: List[List[int]]):
    max_area, number = largest_rectangle(matrix)
    return {"max_area": max_area, "number": number}
