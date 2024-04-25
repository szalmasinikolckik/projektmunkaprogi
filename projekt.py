from random import randint


def darabolas(iz, velemeny, ar, fr):
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
        fr = open("be1.txt", "r", encoding ="UTF=8")
        darabolas(iz, velemeny, ar, fr)
    elif k == "laktózmentes":
        fr = open("be2.txt", "r", encoding ="UTF=8")
        darabolas(iz, velemeny, ar, fr)
    else:
       beolvas(iz,velemeny,ar)


def finomfagyik(velemeny):
    ossz = 0
    n = len(velemeny)
    for i in range(n):
        if velemeny[i] > 4.5:
            ossz += 1
    return ossz


def finomfagyik_list(iz, velemeny, finomlista):
    n = len(velemeny)
    for i in range(n):
        if velemeny[i] > 4.5:
            finomlista.append(iz[i])
    return finomlista       
  

def dragafagyi(ar,iz):
    n = len(ar)
    maxi = 0
    for i in range(1,n):
        if ar[i] > ar[maxi]:
            maxi = i
    return iz[maxi]
        
     
def atlag_velemeny(velemeny):
    s = 0
    n = len(velemeny)
    for i in range(n):
        s += velemeny[i]
    atlag = s / n
    return atlag


def novekvo(ar):
    n = len(ar)
    for i in range(n):
        for j in range(n-1-i):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
    return ar


def intolcso(ar):
    n = len(ar)
    mini = 0
    for i in range(1, n):
        if ar[i] < ar[mini]:
            mini = i  
    return ar[mini]


def olcsoklista(ar, iz, legolcsobb, olcsofagyik):
    n = len(ar)
    for i in range(n):
        if legolcsobb == ar[i]:
            olcsofagyik.append(iz[i])
    return olcsofagyik

    
def iras_olvas():
    n = input("Mit szeretne a fájllal (statisztika/adatrögzítés): ")
    if n == "statisztika" or n == "adatrögzítés":
       return n
    else:
        return iras_olvas()
          

def mitakarsz():
    n = input("Vendégkönyv (írjon bármit): ")
    return n


def hozzairas():
    fa = open("ki.txt", "a", encoding = "UTF=8")
    fa.write(f"{mitakarsz()} \n")
    print("Véleményét rögzítettük!")
    fa.close()


def akcio(legolcsobb):
    r = randint(10, 30)
    akciosar = int(legolcsobb - (r / 100 * legolcsobb))
    return akciosar


def nyil(novekvok):
    for i in range(len(novekvok)-1):
        print(novekvok[i], "=>", end=(" "))
    print(novekvok[len(novekvok)-1])


def statisztika(iz,velemeny, ar, olcsofagyik, finomlista):
    print()
    print("Bim-Bam Fagyizó információk:")
    # F1
    print(f"1.) Ennyi 4,5 csillag fölötti fagyi közül választhat: {finomfagyik(velemeny)}")
    # F2
    finomfagyi = finomfagyik_list(iz, velemeny, finomlista)
    print(f"2.) 4,5 csillag fölötti fagylaltjaink:", *finomfagyi)
    # F3
    print("3.) A legdrágább fagyink:", dragafagyi(ar,iz))
    # F4
    print(f"4.) A fagyizó átlag véleménye: {round(atlag_velemeny(velemeny), 1)} ")
    # F5
    legolcsobb = intolcso(ar)
    olcsofagyik = olcsoklista(ar, iz, legolcsobb, olcsofagyik)
    print("5.) A legolcsóbb fagylaltjaink:", *olcsofagyik)  
    # F6
    print("6.) Mai akciónkkal a legolcsóbb fagylaltjaink/fagylaltunk ára:", akcio(legolcsobb))
    #F7
    novekvok = novekvo(ar)
    print("7.) Fagylaltjaink ára növekvő sorrendben:", end=(" "))
    nyil(novekvok)
         

def main():
    iz,velemeny, ar= [], [], []
    beolvas(iz,velemeny,ar)
    kerdes = iras_olvas()
    olcsofagyik = []
    finomlista = []
    if kerdes == "statisztika":
        statisztika(iz,velemeny, ar, olcsofagyik, finomlista)
    else:
        hozzairas()
        
   
main()