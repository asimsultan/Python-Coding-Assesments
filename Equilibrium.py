#Find an index in an array such that its prefix sum equals its suffix sum.
lis = [2,3,5,6,-1,12]

def get_equi(lis):
    equis = []
    for l in range(len(lis)):
        if l == 0:
            if lis[l] == sum(lis[1:]):
                equis.append(lis[l])
        elif l == len(lis)-1:
            if lis[l] == sum(lis[:-1]):
                equis.append(lis[l])
        else:
            if (lis[l] == lis[l-1]+lis[l-2]) and (lis[l] == lis[l+1]+lis[l+2]):
                equis.append(lis[l])
    return equis

result = get_equi(lis)
print('Result:',result)










