#Part3
#string
#การเข้าถึงstr
name = "   kong นิราศ   "#ข้อความใน"-"ถูกเรียกว่า index

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

#