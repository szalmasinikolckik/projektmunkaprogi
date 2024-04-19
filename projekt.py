

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
    k = input("Melyik fájl(sima/laktózmentes): ")
    if k == "sima":
        sima(iz,velemeny,ar)
    elif k == "laktózmentes":
        mentes(iz,velemeny,ar)
    else:
        k = input("Melyik fájl(sima/laktózmentes):") 

def otrating(velemeny):
    ossz = 0
    n = len(velemeny)
    for i in range(n):
        if velemeny[i] >= 4.5:
            ossz += 1
    return ossz
        

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

def olcsoklista(ar, iz, legolcsobb, olcsok):
    n = len(iz)
    i = 0
    for i in range(n):
        if legolcsobb == ar[i]:
            olcsok.append(iz[i])
    return olcsok        



    
def main():
    iz,velemeny, ar= [], [], []
    beolvas(iz,velemeny,ar)
    olcsok = []
    print(ar)
    # F1
    print(f"ennyi 4,5 csillag fölötti fagyi közül választhat: {otrating(velemeny)}")
    # F2
    print(f"legdrágább fagyink: {draga(ar,iz)}")
    # F3
    print(intolcso(iz, ar))
    legolcsobb = intolcso(iz,ar)
    olcsok = olcsoklista(ar, iz, legolcsobb, olcsok)
    print("a legolcsóbb fagyik:", *olcsok)  
    # F4
    print(f"a fagyizó átlag véleménye:{round(atlag_rating(velemeny), 1)} ")
    # F5
    novekvok = novekvo(ar,iz)
    print("növekvő sorrendben a fagylaltjaink ára:", *novekvok, sep = " => ")
    # F6
   
main()