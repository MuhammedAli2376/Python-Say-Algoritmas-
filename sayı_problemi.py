#yorum satırı
import random
dizi=[]
for i in range(0,5):
    dizi.append(random.randrange(0,9))
dizi.append(random.randrange(10,90,10))
print(dizi)

sayı=int(input("aranacak sayıyı giriniz:"))
aranan_sayı=8
sayac=0
t_dizi=[]
ç_dizi=[]
c_dizi=[]
g_dizi=[]
çarpılmış_dizi=[]
ç_t_dizi=[]
t_sözlük={}
ç_sözlük={}
çarpılmış_sözlük={}
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
def cıkarma():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a-b not in  c_dizi:
            c_dizi.append(a-b)
def çarp():
    for i in range(0,100):
        a=random.choice(g_dizi)
        if a*en_büyük not in  çarpılmış_dizi:
            çarpılmış_dizi.append(a*en_büyük)
            çarpılmış_sözlük[a*en_büyük]=f"{a}*{en_büyük}"
    for k in t_dizi:
        if k*en_büyük not in ç_t_dizi:
            ç_t_dizi.append(k*en_büyük)
            çarpılmış_sözlük[a*en_büyük]=f"{a}*{en_büyük}"
def cıkarma_işlemi(ç_sayı):
    for j in t_dizi:
        if ç_sayı-j==sayı:
            print(ç_sayı-j)
            if sayı+j in çarpılmış_dizi:
                print(f"{çarpılmış_sözlük[sayı+j]}={sayı+j}")
                print(f"{sayı+j}-{j}={sayı}")
            return ç_sayı-j
    for k in ç_dizi:
        if ç_sayı-k==sayı:
            print(f"{ç_sayı-j}={ç_sayı}")
            if ç_sayı+j in çarpılmış_dizi:
                print(f"{çarpılmış_sözlük[sayı+k]}={sayı+k}")
                print(f"{sayı+k}-{k}={sayı}")
            return ç_sayı-k
def toplama_işlemi(t_sayı):
    global sayı
    for j in t_dizi:
        if j+t_sayı==sayı:
            if sayı-j in çarpılmış_dizi:
                print(f"{çarpılmış_sözlük[sayı-j]}={sayı-j}")
                print(f"{sayı-j}+{j}={sayı}")
            return j+t_sayı
    for k in ç_dizi:
        if k+t_sayı==sayı:
            if sayı-k in çarpılmış_dizi:
                print(f"{çarpılmış_sözlük[sayı-k]}={sayı-k}")
                print(f"{sayı-k}+{k}={sayı}")
            return k+t_sayı                          
def kontrol():
    global aranan_sayı
    global sayac
    if sayı in çarpılmış_dizi:
        print("1 defa")
        sayac=1000
        print(f"{çarpılmış_sözlük[sayı]}")
        aranan_sayı=sayı
        return
    elif sayı in ç_t_dizi:
        print("2 defa")
        sayac=1000
        aranan_sayı=sayı
        return
    else:
        for i in çarpılmış_dizi:
            if i>sayı:
                if cıkarma_işlemi(i)==sayı:
                    aranan_sayı=cıkarma_işlemi(i)
                    sayac=1000
                    print("içerde1")
                    return
            if sayı>i:
                a=toplama_işlemi(i)
                if a==sayı:
                    aranan_sayı=a
                    #asamalar(f"{sözlük[b]}={b}")
                    #asamalar(f"{b}*{en_büyük}={b*en_büyük }") 
                    sayac=1000
                    print("içerde2")
                    return
        for i in ç_t_dizi:
            if i>sayı:
                if cıkarma_işlemi(i)==sayı:
                    aranan_sayı=cıkarma_işlemi(i)
                    sayac=1000
                    print("içerde3")
                    return
            if sayı>i:
                a=toplama_işlemi(i)
                if a==sayı:
                    aranan_sayı=a
                    #asamalar(f"{sözlük[b]}={b}")
                    #asamalar(f"{b}*{en_büyük}={b*en_büyük }") 
                    sayac=1000   
                    print("içerde4")
                    return
        else:
            if sayı in ç_t_dizi:
                sayac=1000
                aranan_sayı=sayı
                return
            for i in t_dizi:
                if i*en_büyük>sayı:
                    a=cıkarma_işlemi(i*en_büyük)
                if sayı>i*en_büyük :
                    a=toplama_işlemi(i*en_büyük)
                elif a==sayı:
                    asamalar(f"{sözlük[i]}={i}")
                    asamalar(f"{i}*{en_büyük}={i*en_büyük }") 
                    aranan_sayı=a
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
cıkarma()
çarp()
ana()
if(aranan_sayı==8):
    print("sayı bulunamadı")
else:
    print(f"bulunan sayı:{aranan_sayı}")
#print(t_sözlük)
#print(ç_sözlük)
#print(çarpılmış_sözlük)
print(f"toplama {t_dizi}")
print(f"çarpma dizi {ç_dizi}")
print(f"cıkarma dizi {c_dizi}")
print(f"çarpılmış_dizi: {çarpılmış_dizi}")
print(f"c_t_dizi{ç_t_dizi}")
