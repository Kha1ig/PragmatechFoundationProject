import math
numberone=input('birinci ededi daxil edin: ')
A = 1
# create a result list
result = []
for i in range(0, len(numberone), A):
       
    result.append(int(numberone[i : i + A]))
  
result1 = math.prod(result)
print("The resultant list : " + str(result1))
