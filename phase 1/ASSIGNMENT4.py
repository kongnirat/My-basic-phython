#โปรแกรมแยกธนบัตร,เงิน

bank = int(input("พิมพ์จำนวนเงินของคุณ: "))

#ver.1
""" if bank==1 :
    print("เหรียญ 1 บาท")
elif bank==2 : 
        print("เหรียญ 2 บาท")
elif bank==5:
        print("เหรียญ 5 บาท")
elif bank==10:
        print("เหรียญ 10 บาท")
elif bank==20:
        print("แบงค์ 20 บาท")
elif bank==50:
        print("แบงค์ 50 บาท")
elif bank==100:
        print("แบงค์ 100 บาท")
elif bank==500:
        print("แบงค์ 500 บาท")
elif bank==1000:
        print("แบงค์ 1000 บาท")
    

else :
    print("คุณไม่มีเงิน")
 """

    
if bank>=1000 :
        print("1000 บาท" ,bank//1000,"ใบ")
        bank%=1000

if bank>=500 :
        print("500 บาท" ,bank//500,"ใบ")
        bank%=500

if bank>=100 :
        print("100 บาท" ,bank//100,"ใบ")
        bank%=100

if bank>=50 :
        print("50 บาท" ,bank//50,"ใบ")
        bank%=50

if bank>=20 :
        print("20 บาท" ,bank//20,"ใบ")
        bank%=20
        
if bank>=10 :
        print("10 บาท" ,bank//20,"ใบ")
        bank%=20
        
else :
    print("คุณไม่มีเงิน")
    
print("จบการทำงาน")