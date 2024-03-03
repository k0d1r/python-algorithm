#Kullanıcıdan iki sayı alarak bunların toplamını ve 
#ortalamasını ekrana yazan programı yazınız ?

x = input("birinci sayi = ")
y = input("ikinci sayi = ")

x = int(x)
y = int(y)

toplam = x + y
ortalama = toplam / 2

print("toplam = ", toplam)
print("ortalama = ", ortalama)
