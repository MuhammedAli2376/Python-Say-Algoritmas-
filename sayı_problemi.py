import random
dizi=[]
for i in range(0,5):
    dizi.append(random.randrange(0,9))
dizi.append(random.randrange(10,90,10))
print(dizi)

say�=int(input("aranacak say�y� giriniz:"))
aranan_say�=8
sayac=0
t_dizi=[]
�_dizi=[]
c_dizi=[]
g_dizi=[]
�arp�lm��_dizi=[]
�_t_dizi=[]
t_s�zl�k={}
�_s�zl�k={}
�arp�lm��_s�zl�k={}
def dizi_aktarma():
    for i in dizi:
        g_dizi.append(i)
dizi_aktarma()
g_dizi.pop()
en_b�y�k=max(dizi)
def toplama():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a+b not in  t_dizi:
            t_dizi.append(a+b)
            t_s�zl�k[a+b]=f"{a}+{b}"
def �arpma():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a*b not in  �_dizi:
            �_dizi.append(a*b)
            �_s�zl�k[a*b]=f"{a}*{b}"
def c�karma():
    for i in range(0,100):
        a=random.choice(g_dizi)
        b=random.choice(g_dizi)
        if a-b not in  c_dizi:
            c_dizi.append(a-b)
def �arp():
    for i in range(0,100):
        a=random.choice(g_dizi)
        if a*en_b�y�k not in  �arp�lm��_dizi:
            �arp�lm��_dizi.append(a*en_b�y�k)
            �arp�lm��_s�zl�k[a*en_b�y�k]=f"{a}*{en_b�y�k}"
    for k in t_dizi:
        if k*en_b�y�k not in �_t_dizi:
            �_t_dizi.append(k*en_b�y�k)
            �arp�lm��_s�zl�k[a*en_b�y�k]=f"{a}*{en_b�y�k}"
def c�karma_i�lemi(�_say�):
    for j in t_dizi:
        if �_say�-j==say�:
            print(�_say�-j)
            if say�+j in �arp�lm��_dizi:
                print(f"{�arp�lm��_s�zl�k[say�+j]}={say�+j}")
                print(f"{say�+j}-{j}={say�}")
            return �_say�-j
    for k in �_dizi:
        if �_say�-k==say�:
            print(f"{�_say�-j}={�_say�}")
            if �_say�+j in �arp�lm��_dizi:
                print(f"{�arp�lm��_s�zl�k[say�+k]}={say�+k}")
                print(f"{say�+k}-{k}={say�}")
            return �_say�-k
def toplama_i�lemi(t_say�):
    global say�
    for j in t_dizi:
        if j+t_say�==say�:
            if say�-j in �arp�lm��_dizi:
                print(f"{�arp�lm��_s�zl�k[say�-j]}={say�-j}")
                print(f"{say�-j}+{j}={say�}")
            return j+t_say�
    for k in �_dizi:
        if k+t_say�==say�:
            if say�-k in �arp�lm��_dizi:
                print(f"{�arp�lm��_s�zl�k[say�-k]}={say�-k}")
                print(f"{say�-k}+{k}={say�}")
            return k+t_say�                          
def kontrol():
    global aranan_say�
    global sayac
    if say� in �arp�lm��_dizi:
        print("1 defa")
        sayac=1000
        print(f"{�arp�lm��_s�zl�k[say�]}")
        aranan_say�=say�
        return
    elif say� in �_t_dizi:
        print("2 defa")
        sayac=1000
        aranan_say�=say�
        return
    else:
        for i in �arp�lm��_dizi:
            if i>say�:
                if c�karma_i�lemi(i)==say�:
                    aranan_say�=c�karma_i�lemi(i)
                    sayac=1000
                    print("i�erde1")
                    return
            if say�>i:
                a=toplama_i�lemi(i)
                if a==say�:
                    aranan_say�=a
                    #asamalar(f"{s�zl�k[b]}={b}")
                    #asamalar(f"{b}*{en_b�y�k}={b*en_b�y�k }") 
                    sayac=1000
                    print("i�erde2")
                    return
        for i in �_t_dizi:
            if i>say�:
                if c�karma_i�lemi(i)==say�:
                    aranan_say�=c�karma_i�lemi(i)
                    sayac=1000
                    print("i�erde3")
                    return
            if say�>i:
                a=toplama_i�lemi(i)
                if a==say�:
                    aranan_say�=a
                    #asamalar(f"{s�zl�k[b]}={b}")
                    #asamalar(f"{b}*{en_b�y�k}={b*en_b�y�k }") 
                    sayac=1000   
                    print("i�erde4")
                    return
        else:
            if say� in �_t_dizi:
                sayac=1000
                aranan_say�=say�
                return
            for i in t_dizi:
                if i*en_b�y�k>say�:
                    a=c�karma_i�lemi(i*en_b�y�k)
                if say�>i*en_b�y�k :
                    a=toplama_i�lemi(i*en_b�y�k)
                elif a==say�:
                    asamalar(f"{s�zl�k[i]}={i}")
                    asamalar(f"{i}*{en_b�y�k}={i*en_b�y�k }") 
                    aranan_say�=a
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
�arpma()
c�karma()
�arp()
ana()
if(aranan_say�==8):
    print("say� bulunamad�")
else:
    print(f"bulunan say�:{aranan_say�}")
#print(t_s�zl�k)
#print(�_s�zl�k)
#print(�arp�lm��_s�zl�k)
print(f"toplama {t_dizi}")
print(f"�arpma dizi {�_dizi}")
print(f"c�karma dizi {c_dizi}")
print(f"�arp�lm��_dizi: {�arp�lm��_dizi}")
print(f"c_t_dizi{�_t_dizi}")