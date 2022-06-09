####print patterns
print('\n\n\n\n\n*******program to print pyramid pattern*******\n')
y=int(input('Enter the number of rows you wan to see'))
r='*'
e=' '
k=y
for i in range(1,y+1):
    print(e*(k-1),end=" ")
    for j in range(1,i+1):
        print(r,end=" ")
    print('\r')
    k=k-1
    


    

