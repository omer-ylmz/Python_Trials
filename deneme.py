
# ****************** PLAKA SORUSU **************

plaka = str(input("Plakayı boşluk bırakmadan giriniz..."))
# Plakada integer ve string ifadeler olduğu için tek bir input'ta
# alabilmek için tüm girdiyi stringe çeviriyoruz.


# isalpha() metodu bir karakterin alfabetik bir karakter olup olmadığını
# gösteriyor. Bunu kullanarak plakamızın ilk 2 ve son 2 karakterlerini
# sayı olması şartını kontrol ediyoruz.
if (plaka[0].isalpha() or plaka[1].isalpha() == True):
    print("Uygunsuz plaka!")
elif (len(plaka)>8 or len(plaka)<7):
    print("Uygunsuz plaka uzunluğu!")
# plakakamız belirli uzunluğu geçmemesi gerekiyor.
else:
    if (int(plaka[0:2])>81 or int(plaka[0:2])<1):
        print("01 ile 81 arasında sayılar girmelisiniz!")
    # 81 ilimiz olduğu için ilk 2 karakter integer olarak bu aralıkta olmalı.
    elif (plaka[2].isalpha() == False):
        print("Uygunsuz plaka!")
    # plakamızın 3. karakteri mutlaka harf olmalı
    elif (len(plaka) == 7):
        # plakanın 7 karakterden oluşma durumu
        if (plaka[-1].isalpha() or plaka[-2].isalpha() == True):
            # plakanın son 2 karakteri sayı olmalı
            print("Uygunsuz plaka!")
        else:
            print(plaka.upper())
    elif (len(plaka) == 8):
        # plakanın 8 karakterden oluşma durumu
        if (plaka[-1].isalpha() or plaka[-2].isalpha() or plaka[-3].isalpha()== True):
            # plakanın son 3 karakteri sayı olmalı
            print("Uygunsuz plaka!")
        else:
            print(plaka.upper())

