
def ggt(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a

def kRechnen(z, phi):
    phiZahlen = []
    kZahlen = []
    for i in range(z):
        if(ggt(i, z) == 1):
            phiZahlen.append(i)
    for i in range(phi):
        if(phi%(i+1)==0):
            kZahlen.append(i+1)
    return phiZahlen, kZahlen

def main(z, phi):
    generierende = []
    phiZahlen, kZahlen = kRechnen(z, phi)
    for x in phiZahlen:
        generierend = True
        for k in kZahlen:
            if ((x**k)%z == 1):
                print("x: " , x , "k: ", k , "Ergebnis: " , x**k , "ord: ", k)
                generierend = False
                break
            else:
                print("x: " , x , "k: ", k , "Ergebnis: " , x**k)
        if(generierend == True):
            print(x , "ist generierend/erzeugend")
            generierend.append(x)
        else:
            print(x , "ist NICHT generierend/erzeugend")
    if(len(generierende) != 0):
        print("Die Gruppe ist zyklisch mit den Elementen: " , generierend)
    else:
        print("Die Gruppe ist NICHT zyklisch")
            


            
        
        
        
        
    
