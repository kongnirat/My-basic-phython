#Part2
#โครงสร้างควบคุม (Control Structure)_แบบเลือก
#โครงสร้าง if boolean Exception:
    #Statement
#การใช้elif
#การใช้ and or not 
    
age = int(input("พิมพ์มอายุของคุณ: "))
name = str(input("ชื่อของคุณ: "))
gender = str(input("เพศของคุณ: "))

if age>=15 or age<=24 and gender==("ชาย") :#ระบุเงื่อนไขที่เป็นจริงจะทำงานในคำสั่ง if
    print("นาย/นางสาว" + name)
    print("วัยรุ่น")
    print("เพศชาย")   
    
elif age>=15 or age<=24 and gender==("หญิง"):
    print("นาย/นางสาว" + name)
    print("วัยรุ่น")
    print("เพศหญิง")

elif age>=15 or age<=24 and gender==("LGBTQ+"): 
    print("นาย/นางสาว" + name)
    print("วัยรุ่น")
    print("LGBTQ+")
     
elif age>=25 or age<=55 and gender==("ชาย"):#เป็นเงื่อนไขที่รองลงมาจากifเพื่อบังคับทำงานเคสเดียว
    print("นาย/นางสาว" + name)
    print("วัยทำงาน")
    print("เพศชาย")
    
elif age>=25 or age<=55 and gender==("หญิง"):
    print("นาย/นางสาว" + name)
    print("วัยทำงาน")
    print("เพศหญิง")
    
elif age>=25 or age<=55 and gender==("LGBTQ+"):
    print("นาย/นางสาว" + name)
    print("วัยทำงาน")
    print("LGBTQ+")
     
elif not age<=56 and gender==("ชาย"):
    print("นาย/นางสาว" + name)
    print("วัยชรา")
    print("เพศชาย")
    
elif not age<=56 and gender==("หญิง"):
    print("นาย/นางสาว" + name)
    print("วัยชรา")
    print("เพศหญิง")

elif not age<=56 and gender==("LGBTQ+"):
    print("นาย/นางสาว" + name)
    print("วัยชรา")
    print("LGBTQ+")
      
else :
    print("เด็กชาย/เด็กหญิง " + name)
    print("วัยเด็ก")
    print("เพศ",gender)

print("end")

