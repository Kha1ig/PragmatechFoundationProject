list=[1,2,3,4,5,6,7,8,9]

def listdouble():
    for i in range(len(list)):
        if list[i]%2==1:
            print('tek ededleri goster: ', list[i] )
        else:
            print('cut ededleri goster: ', list[i])
listdouble()