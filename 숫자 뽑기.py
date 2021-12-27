a = [1, 8, 1, 3, 1, 11, 7, 9, 0, 5, 3, 2, 1]
#a = [1, 2]
c = 0
print("start:", a)
for nn in a:
    #print (nn)
    #if nn==1:
     #   a[c] = 0
    if nn==1:
        print(c+1)
    else:
        a[c] = "*"
    c+=1
print("e n d:", a)