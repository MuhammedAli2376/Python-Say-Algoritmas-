import random
dizi=[]
for i in range(0,5):
    dizi.append(random.randrange(0,9))
dizi.append(random.randrange(10,90,10))
print(dizi)

sayý=int(input("aranacak sayýyý giriniz:"))
aranan_sayý=8
sayac=0
t_dizi=[]
ç_dizi=[]
c_dizi=[]
g_dizi=[]
çarpýlmýþ_dizi=[]
ç_t_dizi=[]
t_sözlük={}
ç_sözlük={}
çarpýlmýþ_sözlük={}
def dizi_aktarma():
    for i in dizi:
        g_dizi.append(i)
dizi_aktarma()
g_dizi.pop()
en_büyük=max(dizi)
def toplama():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a+b not in  t_dizi:
            t_dizi.append(a+b)
            t_sözlük[a+b]=f"{a}+{b}"
def çarpma():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a*b not in  ç_dizi:
            ç_dizi.append(a*b)
            ç_sözlük[a*b]=f"{a}*{b}"
def cýkarma():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a-b not in  c_dizi:
            c_dizi.append(a-b)
def çarp():
    for i in range(0,100):
        a=random.choice(g_dizi)
        if a*en_büyük not in  çarpýlmýþ_dizi:
            çarpýlmýþ_dizi.append(a*en_büyük)
            çarpýlmýþ_sözlük[a*en_büyük]=f"{a}*{en_büyük}"
    for k in t_dizi:
        if k*en_büyük not in ç_t_dizi:
            ç_t_dizi.append(k*en_büyük)
            çarpýlmýþ_sözlük[a*en_büyük]=f"{a}*{en_büyük}"
def cýkarma_iþlemi(ç_sayý):
    for j in t_dizi:
        if ç_sayý-j==sayý:
            print(ç_sayý-j)
            if sayý+j in çarpýlmýþ_dizi:
                print(f"{çarpýlmýþ_sözlük[sayý+j]}={sayý+j}")
                print(f"{sayý+j}-{j}={sayý}")
            return ç_sayý-j
    for k in ç_dizi:
        if ç_sayý-k==sayý:
            print(f"{ç_sayý-j}={ç_sayý}")
            if ç_sayý+j in çarpýlmýþ_dizi:
                print(f"{çarpýlmýþ_sözlük[sayý+k]}={sayý+k}")
                print(f"{sayý+k}-{k}={sayý}")
            return ç_sayý-k
def toplama_iþlemi(t_sayý):
    global sayý
    for j in t_dizi:
        if j+t_sayý==sayý:
            if sayý-j in çarpýlmýþ_dizi:
                print(f"{çarpýlmýþ_sözlük[sayý-j]}={sayý-j}")
                print(f"{sayý-j}+{j}={sayý}")
            return j+t_sayý
    for k in ç_dizi:
        if k+t_sayý==sayý:
            if sayý-k in çarpýlmýþ_dizi:
                print(f"{çarpýlmýþ_sözlük[sayý-k]}={sayý-k}")
                print(f"{sayý-k}+{k}={sayý}")
            return k+t_sayý                          
def kontrol():
    global aranan_sayý
    global sayac
    if sayý in çarpýlmýþ_dizi:
        print("1 defa")
        sayac=1000
        print(f"{çarpýlmýþ_sözlük[sayý]}")
        aranan_sayý=sayý
        return
    elif sayý in ç_t_dizi:
        print("2 defa")
        sayac=1000
        aranan_sayý=sayý
        return
    else:
        for i in çarpýlmýþ_dizi:
            if i>sayý:
                if cýkarma_iþlemi(i)==sayý:
                    aranan_sayý=cýkarma_iþlemi(i)
                    sayac=1000
                    print("içerde1")
                    return
            if sayý>i:
                a=toplama_iþlemi(i)
                if a==sayý:
                    aranan_sayý=a
                    #asamalar(f"{sözlük[b]}={b}")
                    #asamalar(f"{b}*{en_büyük}={b*en_büyük }") 
                    sayac=1000
                    print("içerde2")
                    return
        for i in ç_t_dizi:
            if i>sayý:
                if cýkarma_iþlemi(i)==sayý:
                    aranan_sayý=cýkarma_iþlemi(i)
                    sayac=1000
                    print("içerde3")
                    return
            if sayý>i:
                a=toplama_iþlemi(i)
                if a==sayý:
                    aranan_sayý=a
                    #asamalar(f"{sözlük[b]}={b}")
                    #asamalar(f"{b}*{en_büyük}={b*en_büyük }") 
                    sayac=1000   
                    print("içerde4")
                    return
        else:
            if sayý in ç_t_dizi:
                sayac=1000
                aranan_sayý=sayý
                return
            for i in t_dizi:
                if i*en_büyük>sayý:
                    a=cýkarma_iþlemi(i*en_büyük)
                if sayý>i*en_büyük :
                    a=toplama_iþlemi(i*en_büyük)
                elif a==sayý:
                    asamalar(f"{sözlük[i]}={i}")
                    asamalar(f"{i}*{en_büyük}={i*en_büyük }") 
                    aranan_sayý=a
                    sayac=1000
                    return
al_d=[]
def asamalar(al):
    if al not in al_d:
        al_d.append(al)
        print(al_d)
def ana():
    global sayac
    while True:
        #print(sayac)
        kontrol()
        if sayac>=1000:
            break
        sayac=sayac+1
        
toplama()
çarpma()
cýkarma()
çarp()
ana()
if(aranan_sayý==8):
    print("sayý bulunamadý")
else:
    print(f"bulunan sayý:{aranan_sayý}")
#print(t_sözlük)
#print(ç_sözlük)
#print(çarpýlmýþ_sözlük)
print(f"toplama {t_dizi}")
print(f"çarpma dizi {ç_dizi}")
print(f"cýkarma dizi {c_dizi}")
print(f"çarpýlmýþ_dizi: {çarpýlmýþ_dizi}")
print(f"c_t_dizi{ç_t_dizi}")