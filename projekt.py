
def sima(iz,velemeny,ar):
    fr = open("be1.txt", "r", encoding ="UTF=8")
    sor = fr.readline().strip()
    while sor != "":
        darab = sor.split()
        iz.append(darab[0])
        velemeny.append(float(darab[1]))
        ar.append(int(darab[2]))
        sor = fr.readline().strip()
    fr.close()


def mentes(iz,velemeny,ar):
    fr = open("be2.txt", "r", encoding ="UTF=8")
    sor = fr.readline().strip()
    while sor != "":
        darab = sor.split()
        iz.append(darab[0])
        velemeny.append(float(darab[1]))
        ar.append(int(darab[2]))
        sor = fr.readline().strip()
    fr.close()
    
    
def beolvas(iz,velemeny,ar):
    k = input("Melyik fájl?(sima/laktózmentes): ")
    if k == "sima":
        sima(iz,velemeny,ar)
    elif k == "laktózmentes":
        mentes(iz,velemeny,ar)
    else:
       beolvas(iz,velemeny,ar)

def otrating(velemeny):
    ossz = 0
    n = len(velemeny)
    for i in range(n):
        if velemeny[i] > 4.5:
            ossz += 1
    return ossz

def otratingfagyik(iz, velemeny, otratinglist):
    n = len(velemeny)
    for i in range(n):
        if velemeny[i] > 4.5:
            otratinglist.append(iz[i])
    return otratinglist        
  

def draga(ar,iz):
    n = len(ar)
    maxi = 0
    for i in range(1,n):
        if ar[i] > ar[maxi]:
            maxi = i
    return iz[maxi]
        
     
def atlag_rating(velemeny):
    s = 0
    n = len(velemeny)
    for i in range(n):
        s += velemeny[i]
    atlag = s / n
    return atlag
    
def novekvo(ar,iz):
    n = len(ar)
    for i in range(n):
        for j in range(n-1-i):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
    return ar

def intolcso(iz,ar):
    n = len(ar)
    mini = 0
    mine = 0 
    for i in range(1,n):
        if ar[i] < ar[mini]:
            mini = i
            mine = ar[i]
    return mine

def olcsoklista(ar, iz, legolcsobb, olcsofagyik):
    n = len(iz)
    i = 0
    for i in range(n):
        if legolcsobb == ar[i]:
            olcsofagyik.append(iz[i])
    return olcsofagyik
      
    
def iras_olvas():
    n = input("Mit szeretne a fájllal (statisztika/adatrögzítés): ")
    if n == "statisztika":
        return n 
    elif n == "adatrögzítés":
        return n 
    else:
        iras_olvas()


def mitakarsz():
    n = input("Vendégkönyv(írjon bármit): ")
    return n
def hozzairas():
    fa = open("ki.txt", "a", encoding = "UTF=8")
    fa.write(f"{mitakarsz()} \n",)
    print("Véleményét rögzítettük!")
    fa.close()


def statisztika(iz,velemeny, ar, olcsofagyik,otratinglist):
    # F1
    print(f"1.) Ennyi 4,5 csillag fölötti fagyi közül választhat: {otrating(velemeny)}")
    # F2
    otratingfagyi = otratingfagyik(iz, velemeny, otratinglist)
    print(f"2.) 4,5 csillag fölötti fagylaltjaink:", *otratingfagyi)
    # F3
    print("3.) A legdrágább fagyink:", draga(ar,iz))
    # F4
    legolcsobb = intolcso(iz,ar)
    olcsofagyik = olcsoklista(ar, iz, legolcsobb, olcsofagyik)
    print("4.)A legolcsóbb fagylaltjaink:", *olcsofagyik)  
    # F5
    print(f"5.) A fagyizó átlag véleménye: {round(atlag_rating(velemeny), 1)} ")
    # F6
    novekvok = novekvo(ar,iz)
    print("6.) Növekvő sorrendben a fagylaltjaink ára:", *novekvok, sep = " => ")
    
        


def main():
    iz,velemeny, ar= [], [], []
    beolvas(iz,velemeny,ar)
    kerdes = iras_olvas()
    olcsofagyik = []
    otratinglist = []
    if kerdes == "statisztika":
        statisztika(iz,velemeny, ar, olcsofagyik,otratinglist)
    else:
        hozzairas()
        
   
main()