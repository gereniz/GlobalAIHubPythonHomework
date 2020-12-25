import random as rnd
username = input("User Name : ")
count = 0
print("Hoşgeldiniz {} :) ".format(username))
print("Eğer 100 üzerinden 50 alırsanız kazanırsınız :)")

for i in range(10):
    a = rnd.randint(1,10)
    b = rnd.randint(1,10)
    print("{} x {} = ? ".format(a,b))
    sonuc = int(input())
    if sonuc == a*b:
        count+=10
    if(count > 50):
        print("Tebrikler. Kazandınız . Puanınız : {} ".format(count))
    else:
        print("Kazanamadınız. Puanınız : {} ".format(count))

 
