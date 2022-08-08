# 3x2 matrix
X = [ [1,2],[3,4],[4,5] ]
# 2x3 matrix
Y = [ [1,2,3],[4,5,6] ]

# resultant matrix
result = [ [0,0,0],[0,0,0],[0,0,0] ]

my_list = []
# iterating rows of X matrix
for i in range( len(X) ):
   # iterating columns of Y matrix
   for j in range(len(Y[0])):
       # iterating rows of Y matrix
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
  

for r in result:
   print(r)

