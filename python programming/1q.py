r= int(input("Enter the number for Rows :"))
c= int(input("Enter the number for column :"))
x= []
val=[]
for i in range (r) :
    for j in range(c):
        val.append(int(input("Enter the value -%d * %d- element :"%(i,j))))
    x.append(val)
    val=[]
y=[]
for i in range(r):
    for i in range(c):
        val.append(int(input("Enter the value -%d * %d- element :"%(i,j))))
    y.append(val)
    val=[]
sum =[]
for i in range(r):
    val=[]
    for j in range(c):
        val.append(x[i][j]+y[i][j])
    sum.append(val)
print(sum)
    