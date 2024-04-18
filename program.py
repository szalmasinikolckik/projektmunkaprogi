

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
    return iz[i]
        
def olcso(iz,ar):
    n = len(ar)
    mini = 0 
    for i in range(1,n):
        if ar[i] < ar[mini]:
            mini = i
    return iz[i]
     
def main():
    iz,velemeny, ar= [], [], []
    beolvas(iz,velemeny,ar)
    # F1
    print(f"ennyi 4,5 csillag fölötti fagyi közül választhat: {otrating(velemeny)}")
    # F2
    print(f"legdrágább fagyink: {draga(ar,iz)}")
    # F3
    print(f"legolcsóbb fagyink: {olcso(iz,ar)}")
    print(iz,velemeny,ar)
main()