list=[8,2,3,-1,7]

def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x
    return result

print(multiplyList(list))