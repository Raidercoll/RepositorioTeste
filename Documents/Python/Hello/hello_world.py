a = [57,21,8,9,1,65,84,51,32,20]
for i in range(len(a)):
    if a[i] > a[i+1]:
        aux = a[i]
        a[i] = a[i+1]
        a[i+1] = aux