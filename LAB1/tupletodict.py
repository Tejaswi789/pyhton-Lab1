t=int(input("enter number of tuples"))
lt=[]
for i in range(t):
    name = input("\nEnter the name\t-")
    subject = input("\nEnter the subject\t-")
    marks = input("\nEnter the marks\t-")
    tp = (name, ((subject), int(marks)))
    lt.append(tp)
di={}
for a,b in lt:
    di.setdefault(a, []).append(b)
print(di)