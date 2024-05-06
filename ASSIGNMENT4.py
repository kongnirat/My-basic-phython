#โปรแกรมแยกธนบัตร,เงิน

bank = int(input("พิมพ์จำนวนเงินของคุณ: "))

if bank==1 :
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
    
print("จบการทำงาน")