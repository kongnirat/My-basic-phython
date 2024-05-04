#Part2
#โครงสร้างควบคุม (Control Structure)_แบบเลือก
#โครงสร้าง if boolean Exception:
    #Statement
#การใช้elif
#การใช้ and or not 
    
age = int(input("พิมพ์มอายุของคุณ: "))
name = str(input("ชื่อของคุณ: "))
gender = str(input("เพศของคุณ: "))


#if ซ้อน if
if age>=15 :   
    if age<=20:
            print("นาย/นางสาว" + name)
            print("วัยรุ่น")
            print("เพศชาย")   
else : 
    print("noting")