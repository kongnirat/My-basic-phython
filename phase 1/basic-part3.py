#Part3
#string
#การเข้าถึงstr
name = "   kong นิราศ k   "#ข้อความใน"-"ถูกเรียกว่า index

print(name[0:8])#โดยข้อความตัวแรกจะเริ่มจาก 0 จะทำงานจนก่อนถึงจุดสุดท้ายนั้นก็คือหมายเลข 3
print(name[:8])#ไม่ต้องเขียนเลข 0 ก็ได้
print(name[:17])#กรณีที่มีเว้นวรรตก็จะนับเป็นหนึ่ง
print(name[-8:])#การอ่านข้อความย้อนหลัง

#strip function
name = name.strip()#ลบช่องว่างซ้ายขวา
name = name.lstrip()#ลบช่องว่างซ้าย
name = name.rstrip()#ลบช่องว่างขวา

#len function\
print(len(name))#การหาความยาวของ str

#แปลงตัวพิมพ์ใหญ่มั้งหมด
print(name.upper())

#แปลงตัวพิมพ์เล็กมั้งหมด
print(name.lower())

#ตัวแรกสุดเป็นตัวใหญ่
print(name.capitalize())

#การแทนที่
print(name.replace('kong' ,"mr."))
print(name.replace('kong' ,"mr." ,2))#กรณี k หลายตัว

#การเช็คข้อความ
x = "k" in name

if x:
    name.replace("k" , "last name")
    
else: 
    print("nothing")
    
print(name)

#การเปลี่ยนข้อความเฉพาะ
a = "Hello, World!"
print(a.replace("H", "J"))

#การต่่อ str
fname = "kong"
lname = "nirat"
age = "17"
money = 4000.50000

print(str("ชื่อ: " +fname+"\tนามสกุล: " +lname +"\tอายุ: " +age))

#การจัดรูปแบบแสดงผล
txt = "ชื่อ : {0}\tนามสกุล :{1} \tอายุ :{2} \tอาชีพ :{3} \tรายได้ :{4:.2f}  "#สามารถระบุตำแหน่งได้ด้วยการเขียนตัวเลข
print(txt.format(fname,lname,age,"นักเรียน",money))

#การนับจำนวนคำในประโยค
print(name.count("k"))

#เช็คคำนำขึ้นต้น/ลงท้าย
print(name.startswith("kong"))
print(name.endswith("k"))

#while loop จะทำงานเมื่อค่าเป็นจริง

i = 1
''''
while i<=3 :
    print("รอบที่ : " , i)
    i = i + 1
print("end")

#for loop จะทำงานเมื่อมีจำนวนลูปที่ชัดเจน
for k in range(1,3):#rangeคือตัวกำหนดรอบซึ่งจะเริ่มต้นที่ 0
    print("รอบที่ = " , k ,"hello world")
'''''    
#loop ซ้อน loop
while i<=3 : 
    j = 1 
    while j<=5:
        print("รอบที่ = " ,i, "ตำแหน่งที่ =", j)
        j+=1
    i+=1     
    
for i in range(1,5): 
    print("รอบที่ = " ,i)
    for j in range(1,6):
        print("ตำแหน่งที่ =", j)
 
    
     
    
    


