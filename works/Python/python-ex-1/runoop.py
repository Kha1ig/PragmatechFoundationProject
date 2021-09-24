books=[]

class BOOK:
    def __init__(self, id, ad, yazar, sehife):
        self.id=id
        self.ad=ad
        self.yazar=yazar
        self.sehife=sehife
        
# USERS=users('xaliq', 'rehimov', 22, 'email')
    
    def addToList(self):
        books.append(self)
    def showbook(self):
        print(f'ID:{self.id},{self.ad},{self.yazar},{self.sehife}')

id=0
def createbook():
    global id
    id = id + 1
    ad=input('Ad: ')
    yazar=input('yazar: ')
    sehife=input('sehife: ')

    Books=BOOK(id,ad,yazar,sehife,)
    Books.addToList()


def removebook(id):
    for Books in books:
        if int(id) == Books.id:
            books.remove(Books)
            break
    

def showbyName(ad):
    for Books in books:
        if ad == Books.ad:
            Books.showbook()

def showbyPage(sehife):
    for Books in books:
        if int(sehife) == Books.sehife:
            print('salam')
            #Books.showbook()

def updatebook(id):
    for Books in books:
        if int(id)==Books.id:
            Books.ad= input(' yeni ad daxil et: ')
            Books.yazar= input(' yeni yazar daxil et: ')
            Books.sehife= input(' sehife sayini daxil et: ')
            Books.showbook()


while True:
    emr=input('Yeni kitab yarat(1)/Bütün kitab məlumatlarını goster(2)/ Kitabin id-ye gore silinmesi(3)/ ada gore kitabi tap(4)/ sehife say;na gore (5)/ kitabi upate etmek(6): ')

    if emr=='1':
        createbook()
    elif emr=="2":
        for Books in books:
            Books.showbook()
        
    elif emr=='3':
        id=input('hansi kitab silinecekse id daxil et: ')
        removebook(id)
    elif emr=='4':  
        ad= input('ada gore kitab axtarisi ucun ad daxil edin: ')
        showbyName(ad)
    elif emr=='5':
        sehife=input(' kitabi tapmaq ucun sehife sayini daxil edin: ')
        showbyPage(sehife)
    elif emr=='6':
        id=input('yeni kitab daxil etmek ucun id daxil et: ')
        updatebook(id)