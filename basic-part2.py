#Part2
#โครงสร้างควบคุม (Control Structure)_แบบเลือก
#โครงสร้าง if boolean Exception:
    #Statement
#การใช้elif
#การใช้ and or not 
    
age = int(input("พิมพ์มอายุของคุณ: "))
name = str(input("ชื่อของคุณ: "))
gender = str(input("เพศของคุณ: "))

if age>=15 and age<=24 and gender==("ชาย") :#ระบุเงื่อนไขที่เป็นจริงจะทำงานในคำสั่ง if
    print("นาย" + name)
    print("วัยรุ่น")
    print("เพศชาย")   
    
elif age>=15 and age<=24 and gender==("หญิง"):
    print("นางสาว" + name)
    print("วัยรุ่น")
    print("เพศหญิง")

elif age>=15 and age<=24 and gender==("LGBTQ+"): 
    print("นาย/นางสาว" + name)
    print("วัยรุ่น")
    print("LGBTQ+")
     
elif age>=25 and age<=55 and gender==("ชาย"):#เป็นเงื่อนไขที่รองลงมาจากifเพื่อบังคับทำงานเคสเดียว
    print("นาย" + name)
    print("วัยทำงาน")
    print("เพศชาย")
    
elif age>=25 and age<=55 and gender==("หญิง"):
    print("นาง" + name)
    print("วัยทำงาน")
    print("เพศหญิง")
    
elif age>=25 and age<=55 and gender==("LGBTQ+"):
    print("นาย/นาง" + name)
    print("วัยทำงาน")
    print("LGBTQ+")
     
elif age>=56 and age<=70  and gender==("ชาย"):
    print("นาย" + name)
    print("วัยชรา")
    print("เพศชาย")
    
elif age>=56 and age<=70 and gender==("หญิง"):
    print("นาง" + name)
    print("วัยชรา")
    print("เพศหญิง")

elif age>=56 and age<=70 and gender==("LGBTQ+"):
    print("นาย/นางสาว" + name)
    print("วัยชรา")
    print("LGBTQ+")
      
else :
    print("เด็กชาย/เด็กหญิง " + name)
    print("วัยเด็ก")
    print("เพศ",gender)

print("end")

#if ซ้อน if
if age>=15 :   
    if age<=20:
            print("วัยรุ่น")
    elif age>=21 and age<=24:
            print("วัยมหาลัย")
    elif age==25:
            pass
    elif age<=30:
            print("วัยทำงาน")
else : 
    print("noting")