r= int(input("Enter the number of rows:"))
c= int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")
for i in range(r):		 
	a =[]
	for j in range(c):	 
		a.append(int(input()))
	matrix.append(a)

for i in range(r):
	for j in range(c):
		print(matrix[i][j], end = " ")
	print()

spar = []
for i in range(r):
        for j in range(c):
            if matrix[i][j] != 0 :
                var =[]
                var.append(i)
                var.append(j)
                var.append(matrix[i][j])
                spar.append(var)

print(spar)
