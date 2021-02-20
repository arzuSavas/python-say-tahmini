# sayı tahmini oyunu
import random
secilenSayi = random.randint(1, 100)
#print(secilenSayi)
sayac = 0
hak = int(input("kaç seferde bilebilirsin"))
for i in range(hak):
 i += 1
 sayac += 1
 tahmin = int(input("tahmin ettiğiniz sayıyı giriniz"))
 puan = int(100 - ((100/hak)*(sayac-1)))
 if tahmin == secilenSayi:
    print(f"puanınız {puan}")
    print("kazandınız")
    break
 elif tahmin < secilenSayi:
   print("daha yukarıda bir tahmin yapmalısınız")
 else:
   print("daha aşşağıda bir tahmin yapmalısınız")
 if i == hak:
  print("hakkınız kalmadı kazanamadınız")
  print(f"tutulan sayi {secilenSayi}")

