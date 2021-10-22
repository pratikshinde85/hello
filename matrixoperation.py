def create_matrix():
    R = int(input("Enter the number of rows of matrix 1:"));
    C = int(input("Enter the number of columns of matrix 1:"));
    matrix1 = []
    print("Enter the entries row wise in matrix1:")

    for i in range(R):		 
        a =[]
        for j in range(C):	
            a.append(int(input()))
        matrix1.append(a)
    R = int(input("Enter the number of rows of matrix 2:"));
    C = int(input("Enter the number of columns of matrix 2:"));
    matrix2 = []
    print("Enter the entries row wise in matrix2:")
    for i in range(R):		 
        a =[]
        for j in range(C):	
            a.append(int(input()))
        matrix2.append(a)
    print("Matrix 1 is:");
    for i in range(R):
        for j in range(C):
            print(matrix1[i][j], end = " ")
        print()
    print("Matrix2 is:");
    for i in range(R):
        for j in range(C):
            print(matrix2[i][j], end = " ")
        print()
    add = [[0,0,0], [0,0,0], [0,0,0]];
    print("Addition of Two Matrix:");
    for i in range(R):
        for j in range(C):
            add[i][j]=matrix1[i][j]+matrix2[i][j];
            print(add[i][j],end=" ");
        print()
    print("Substraction of Two Matrix:");
    sub = [[0,0,0], [0,0,0], [0,0,0]];
    for i in range(R):
        for j in range(C):
            sub[i][j]=matrix1[i][j]-matrix2[i][j];
            print(sub[i][j],end=" ");
        print()
    mul = [[0,0,0], [0,0,0], [0,0,0]];
    print("multiplication of Two Matrix:");
    for i in range(R):
        for j in range(C):
            mul[i][j]=matrix1[i][j]*matrix2[i][j];
            print(mul[i][j],end=" ");
        print()
    print("transepose  of  Matrix 1:");
    trans1= [[0,0,0], [0,0,0], [0,0,0]];
    for i in range(R):
        for j in range(C):
            trans1[i][j]=matrix1[j][i];
            print(trans1[i][j],end=" ");
        print()
    print("transepose  of  Matrix 2:");
    trans2= [[0,0,0], [0,0,0], [0,0,0]];
    for i in range(R):
        for j in range(C):
            trans2[i][j]=matrix2[j][i];
            print(trans2[i][j],end=" ");
        print()

    
create_matrix();



