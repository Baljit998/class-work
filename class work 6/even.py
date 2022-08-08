def even(num1,num2):
	if num1>num2:
          return
	print(num1,end=" ")
	return even(num1+2,num2)
num1=442;num2=622
even(num1,num2)


'''
def last_ind(L, e):

    if not L:
        return None
    if L[0] == e:
        return 0
    n = last_ind(L[1:],e)
    if n is not None:
        return 1 + n
    return None

’’’Return the largest index at which element e appears in the list L. If e is not in L, return None.

 >>> last_ind([1, 5, 3, 5, 4], 5)
'''
