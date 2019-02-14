import copy
sentence= input("enter the string")
substr=[]
substr2=[]
max=0
for i in range(len(sentence)):
    if sentence[i] not in substr:
        substr.append(sentence[i])
    else:
        if len(substr)>max:
            substr2.clear()
            substr2=copy.deepcopy(substr)
            substr.clear()
            substr.append(sentence[i])
            max=len(substr2)
        else:
            substr.clear()
if len(substr)>max:
    substr2.clear()
    substr2 = copy.deepcopy(substr)
    max=len(substr2)
print(substr2," ",max)