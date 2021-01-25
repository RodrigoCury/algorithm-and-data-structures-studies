"""
        Matrix is a way to store data in an organized form in the form of rows and columns. 
    Matrices are usually used in computer graphics to project 3-dimensional space onto a 2-dimensional screen.
    Matrices in the form of arrays are used to store data in an organized form.

    A matrix is a representation of certain rows and columns, to persist homogeneous data. It can also be called as double-dimensioned array.

    Uses:
        - To represent class hierarchy using Boolean square matrix
        - For data encryption and decryption
        - To represent traffic flow and plumbing in a network
        - To implement graph theory of node representation 
    """

matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

for row in matrix:
    sum = 0
    for col in row:
        sum += col
        print(col, end=', ')
    print(sum)

student_score = [
    ['joão', 8, 7, 6],
    ['pedro', 4.5, 9, 10],
    ['marcos', 6, 6, 8],
]

for row in student_score:
    sum = 0
    for grade in range(1, len(row)):
        sum += row[grade]
    avg = sum/(len(row) - 1)
    print(f"{row[0]} average is {avg:.2f}")
    if avg >= 7:
        print(f"{row[0]} has passed")
    else:
        print(f"{row[0]} hasn't passed")
