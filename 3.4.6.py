hat_list = [1, 2, 3, 4, 5]

# 1. Adım: Kullanıcıdan bir sayı alıp ortadaki eleman ile değiştiriyoruz
yeni_sayi = int(input("Bir sayı giriniz: "))
hat_list[2] = yeni_sayi

# 2.Adım: Listenin son elemanını siliyoruz
del hat_list[-1]

# 3.Adım: Listenin uzunluğunu ekrana yazdırıyoruz
print(len(hat_list))

print(hat_list)
