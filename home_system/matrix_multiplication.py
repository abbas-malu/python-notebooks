row1 = int(input('Enter No of rows for first matrix: '))
col1 = int(input('Enter No of columns for first matrix: '))
row2 = int(input('Enter No of rows for second matrix: '))
col2 = int(input('Enter No of columns for second matrix: '))
if col1==row2:
    mat1 = []
    for i in range(row1):
        col = []
        for j in range(col1):
            x = int(input(f'Enter the number for a{i+1}.{j+1}: '))
            col.append(x)
        mat1.append(col)
    mat2 = []
    for i in range(row2):
        col = []
        for j in range(col2):
            x = int(input(f'Enter the number for b{i+1}.{j+1}: '))
            col.append(x)
        mat2.append(col)
else:
    print('Mismatch in matrix dimension')
final_mat = []
for row_index in range(len(mat1)):
    final_mat.append([])
    row_mul = mat1[row_index]
    for i in range(len(mat2[0])):
        col_mul = []
        for j in mat2:
            col_mul.append(j[i])
        num = 0
        for x in range(len(row_mul)):
            num += row_mul[x]*col_mul[x]
        final_mat[row_index].append(num)
print(f'\nThe product of  {mat1}   and    {mat2} is\n')
for i in final_mat:
    print(i)
