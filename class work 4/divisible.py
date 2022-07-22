nl=[]
for x in range(1200, 3000):
    if (x%4==0) and (x%8==0) and (x%6!=0):
        nl.append(str(x))
print (','.join(nl))
