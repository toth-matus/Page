x = int(input("Pocet stlpcov aj s |b"))
y = int(input("Pocet riadkov"))
pole=[x]*y

def hladaj(p):
    if pole[p][p]==0:
        for i in range(0,y):
            if pole[i][p]!=0:
                for j in range(p,x):
                    pole[p][j],pole[i][j] = pole[i][j],pole[p][j]
def hore(p):
    for i in range(p):
        if pole[p][p]!=0:
            pom = pole[i][p]/pole[p][p]
            for j in range(p,x):
                pole[i][j]=pole[i][j]-pom*pole[p][j]
def dole(p):
    for i in range(p+1,y):
        if pole[p][p]!=0:
            pom = pole[i][p]/pole[p][p]
            for j in range(p,x):
                pole[i][j]=pole[i][j]-pom*pole[p][j]
def vydel():
    for i in range(y):
        dell = pole[i][i]
        if dell !=0:
            for j in range(i,x):
                pom = pole[i][j]/dell
                if abs(pom)<10**(-10):
                    pom=0
                pole[i][j]=pom
def vypis():
    for i in range(y):
        print(pole[i])

for i in range(y):
    pom = input(f"zadaj {i+1}. riadok aj s |b")
    pole[i] = pom.split()

for i in range(y):
    for j in range(x):
        pole[i][j]=float(pole[i][j])

for i in range (y):
    hladaj(i)
    hore(i)
    dole(i)
vydel()
vypis()





