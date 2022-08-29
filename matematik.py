print("Matematiksel Hesaplama Programi-0031")

while True:
    print("\n\t1 => Dort islem \n\t2 => Uslu sayi hesaplamak \n\t3 => Bolumden kalani bulmak icin")
    
    karar = input("Hangi islem yapacaksaniz kodunu giriniz: ")
    
    if karar == "1":
        
        while True:
            print("\n4-Toplama \n5-Cikartma \n6-Carpma \n7-Bolme")
            dort_islem = input("Hangi dort islemi yapacaksaniz kodunu giriniz: ")
                
            if dort_islem == "4":
             a = int(input("Toplanacak ilk sayiyi giriniz."))   
             b = int(input("Toplanacak ikinci sayiyi giriniz."))
             print("Toplama isleminin sonucu ",a+b ,"dir.")
             break
             
            elif dort_islem == "5":
                a = int(input("Cikartilacak ilk sayiyi giriniz."))   
                b = int(input("Cikartilacak ikinci sayiyi giriniz."))
                print("Cikartma isleminin sonucu ",a-b ,"dir.")
                break
                
            elif dort_islem == "6":
                a = int(input("Carpilacak ilk sayiyi giriniz."))   
                b = int(input("Carpilacak ikinci sayiyi giriniz."))
                print("Carpma isleminin sonucu ",a*b ,"dir.")
                break
            
            elif dort_islem == "7":
                    a = int(input("Bolunecek ilk sayiyi giriniz."))   
                    b = int(input("Bolunecek ikinci sayiyi giriniz."))
                    print("Bolme isleminin sonucu",a/b ,"dir.")
                    break
            
            else:
                    print("Bari sayiyi dogru gir herseyi ben yapiyorum..")
                    break
    
    elif karar == "2":
        
        a = int(input("Ustlu sistemin tabanini yaziniz."))
        b = int(input("Ustlu sistemin kuvvetini giriniz."))
        print("Ustlu isleminizin sonucu ",a**b , "dir.")
        break
    
    elif karar == "3":
        
        a=int(input("Bolunen sayiyi yaziniz."))
        b=int(input("Bolen sayiyi yaziniz."))
        print("Kalan", a%b ,"dir.")
        break
    
    else:
            print("Kodu bari dogru gir herseyi ben yapiyorum zaten.")
            break

    karar2 = input("Tekrar denemek ister misin? (Cikmak icin "x" yaziniz)")
        if karar2 == "x":
            print("Asta la vista beybi...")
            break
        else:
            print("DEVAMKEEE")