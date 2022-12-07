

Rows = int(input("Give the number of rows:"))
Columns = int(input("Give the number of columns:"))
example_matrix = []
print("Please give the entries row-wise:")


for i in range(Rows):
    r = []
    for j in range(Columns):
        r.append(int(input()))
    example_matrix.append(r)

for i in range(Rows):
    for j in range(Columns):
        print(example_matrix[i][j], end=" ")
    print()