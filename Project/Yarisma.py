import csv
import random 


soruvecevap = {}
sorular = []
dogrusayisi = 0

reader = csv.reader(open('yarisma.csv', 'r'))


for row in reader:
   k, v = row
   soruvecevap[k] = v
   
for i in soruvecevap.keys():
   sorular.append(i)
    
sorusayisi = len(sorular)
soruNo = random.sample(range(1, sorusayisi), 10)


print(" \n")
print("**************************************************************************")
print("--------------------------BILGI YARISMASI---------------------------------")
print(" \n")
print("Yarismayi kazanabilmek için 10 sorudan en az 5'ine dogru cevap vermiş olmalısınız.")
print("Soruların cevabı tek kelimedir.")
print(" \n")
print("Basarilar :)")


for i in range(10):
    print(" \n")
    print("**************************************************************************")
    print(str(i+1) + ". soru:  ")
    cevap = input(sorular[soruNo[i]] + ": ").upper().strip()
    x = str(soruvecevap[sorular[soruNo[i]]])[1:len(soruvecevap[sorular[soruNo[i]]])-1].upper().strip()
    if cevap == x:
        dogrusayisi += 1
        print(" \n")
        print("Tebrikler!  " +str(i+1)+ ". soruyu doğru bildiniz ")
    else:
        print(" \n")
        print("Yanlış!! Doğru cevap: " + x)
    
    
        
puan = dogrusayisi*10        

if 50 <= puan:
    print(" \n")
    print("Toplam puanınız: " + str(puan))
    print("Tebrikleeeer!! :) Kazandınız.")
    
else:
    print(" \n")
    print("Toplam puanınız: " + str(puan))
    print("Üzgünüz :( Kazanamadınız.")
    
        
