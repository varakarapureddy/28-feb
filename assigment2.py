# finding non repating elements in list
i=[1,2,1,3,2,4,2,5,4,6,5,7,6,4]
for n in i:
    if i.count(n) == 1:
        print(n," ") 
