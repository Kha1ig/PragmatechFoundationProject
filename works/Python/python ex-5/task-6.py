x=3
y=50

def bolunme3():
    
    for i in range(x,y):
        
        if i%3==0:
           print("three: ", [i])

bolunme3()

def bolunme5():
    
    for i in range(x,y):
        
        if i%5==0:
           print("Five: ", [i])

bolunme5()

def bolunme3ve5():
    
    for i in range(x,y):
        
        if i%3==0 and i%5==0:
           print("threeFive: ", [i])

bolunme3ve5()

def bolunmur():
    
    for i in range(x,y):
        
        if i%3!=0 and i%5!=0:
           print( '3e ve 5e bolunmeyen ededler: ', [i])

bolunmur()