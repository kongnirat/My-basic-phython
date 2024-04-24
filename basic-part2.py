#Part2
#โครงสร้างควบคุม (Control Structure)_แบบเลือก
#โครงสร้าง if boolean Exception:
    #Statement
    
age = int(input("พิมพ์มอายุของคุณ: "))
name = str(input("ชื่อของคุณ: "))

if age>=15:#ระบุเงื่อนไขที่เป็นจริงจะทำงานในคำสั่ง if
    print("นาย/นางสาว" + name)
    print("จบการทำงานif")
    
else :
    print("เด็กชาย/เด็กหญิง" + name)

print("end")

